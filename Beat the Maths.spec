# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['beat_the_maths\\__main__.py'],
    pathex=['.'],
    binaries=[],
    datas=[('beat_the_maths\\data', 'beat_the_maths\\data')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Beat the Maths',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['beat_the_maths\\assets\\app.ico'],
)
