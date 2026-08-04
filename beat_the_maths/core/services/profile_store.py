import json
import logging
from pathlib import Path

from platformdirs import user_data_path

from ..user_profile import AchievementId, UserProfile

LOGGER = logging.getLogger(__name__)

PROFILE_VERSION = 1
APP_NAME = "Beat the Maths"
APP_AUTHOR = "Les Productions Majeures"


def get_profile_path() -> Path:
    return (
        user_data_path(
            appname=APP_NAME,
            appauthor=APP_AUTHOR,
        )
        / "profile.json"
    )


def load_profile(path: Path) -> UserProfile:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return UserProfile()
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        LOGGER.warning(
            "Unable to laod profile from %s",
            path,
            exc_info=True,
        )
        return UserProfile()

    if not isinstance(data, dict):
        return UserProfile()

    if data.get("version") != PROFILE_VERSION:
        return UserProfile()

    achievement_values = data.get("unlocked_achievements", [])

    if not isinstance(achievement_values, list):
        return UserProfile()

    unlocked_achievements: set[AchievementId] = set()

    for value in achievement_values:
        try:
            unlocked_achievements.add(AchievementId(value))
        except (TypeError, ValueError):
            # Ignore invalid or unknown badges
            continue

    return UserProfile(
        unlocked_achievements=unlocked_achievements,
    )


def save_profile(profile: UserProfile, path: Path) -> bool:
    temporary_path = path.with_suffix(f"{path.suffix}.tmp")

    data = {
        "version": PROFILE_VERSION,
        "unlocked_achievements": sorted(
            achievement.value for achievement in profile.unlocked_achievements
        ),
    }

    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        temporary_path.replace(path)
    except OSError:
        LOGGER.warning(
            "Unable to save profile to %s",
            path,
            exc_info=True,
        )

        try:
            temporary_path.unlink(missing_ok=True)
        except OSError:
            pass

        return False

    return True
