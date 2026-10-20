# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

tkinter_modules = collect_submodules('tkinter')

a = Analysis(
    ['ObreCarpetaID.py'],
    pathex=[],
    binaries=[],
    datas=[('img', 'img')],
    hiddenimports=tkinter_modules,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter.ttk', 'PIL',
        'numpy', 'scipy', 'pandas', 'matplotlib',
        'pytest', 'IPython', 'notebook',
        'setuptools', 'distutils', 'pkg_resources',
        'asyncio', 'email', 'xml', 'sqlite3',
        'unittest', 'pydoc', 'doctest',
        'multiprocessing', 'concurrent',
        'bz2', 'lzma', 'gzip', 'tarfile',
        'ssl', 'http', 'urllib', 'socketserver',
        'json', 'csv', 'logging',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ObreCarpetaID',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='img\\logo.ico',
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
