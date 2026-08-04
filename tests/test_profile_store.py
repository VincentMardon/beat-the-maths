import json
from pathlib import Path

from beat_the_maths.core.services.profile_store import (
    PROFILE_VERSION,
    load_profile,
    save_profile,
)
from beat_the_maths.core.user_profile import AchievementId, UserProfile


def test_loads_empty_profile_when_file_does_not_exist(tmp_path: Path):
    profile = load_profile(tmp_path / "profile.json")

    assert profile == UserProfile()


def test_saves_and_loads_profile(tmp_path: Path):
    path = tmp_path / "profile.json"
    profile = UserProfile(
        unlocked_achievements={
            AchievementId.ONE_QUESTION,
        }
    )

    saved = save_profile(profile, path)
    loaded_profile = load_profile(path)

    assert saved is True
    assert loaded_profile == profile


def test_saved_profile_contains_format_version(tmp_path: Path):
    path = tmp_path / "profile.json"

    save_profile(UserProfile(), path)

    data = json.loads(path.read_text(encoding="utf-8"))

    assert data["version"] == PROFILE_VERSION


def test_loads_empty_profile_from_invalid_json(tmp_path: Path):
    path = tmp_path / "package.json"
    path.write_text("{invalid json", encoding="utf8")

    profile = load_profile(path)

    assert profile == UserProfile()


def test_ignores_unknown_achievement_ids(tmp_path: Path):
    path = tmp_path / "profile.json"
    path.write_text(
        json.dumps(
            {
                "version": PROFILE_VERSION,
                "unlocked_achievements": [
                    "one_question",
                    "unknown_achievement",
                ],
            }
        ),
        encoding="utf-8",
    )

    profile = load_profile(path)

    assert profile.unlocked_achievements == {
        AchievementId.ONE_QUESTION,
    }
