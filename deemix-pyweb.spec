# -*- mode: python ; coding: utf-8 -*-
import sys
from datetime import date
import subprocess

today = date.today().strftime("%Y.%m.%d")
commit = str(subprocess.check_output(['git', 'rev-parse', 'HEAD'])[:10])
version = f"{today}-{commit}"
with open('version.txt', 'w') as f:
    f.write(version)

block_cipher = None

sys.modules['FixTk'] = None

a = Analysis(['deemix-pyweb.py'],
             binaries=[],
             datas=[('webui/public', 'webui'), ('icon.ico', '.'), ('version.txt', '.')],
             hiddenimports=['engineio.async_drivers.threading', 'pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter', 'mkl', 'whl'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
if sys.platform.startswith('darwin'):
    exe = EXE(pyz,
              a.scripts,
              [],
              exclude_binaries=True,
              name='deemix-pyweb',
              debug=False,
              bootloader_ignore_signals=False,
              strip=False,
              upx=True,
              console=False,
              icon="icon.icns")
    coll = COLLECT(exe,
                   a.binaries,
                   a.zipfiles,
                   a.datas,
                   strip=False,
                   upx=True,
                   upx_exclude=[],
                   name='deemix-pyweb')
    app = BUNDLE(coll,
                 name='deemix-pyweb.app',
                 icon="icon.icns",
                 bundle_identifier=None)
elif '--onefile' in sys.argv or '-F' in sys.argv:
    exe = EXE(pyz,
              a.scripts,
              a.binaries,
              a.zipfiles,
              a.datas,
              [],
              name='deemix-pyweb',
              debug=False,
              bootloader_ignore_signals=False,
              strip=False,
              upx=True,
              upx_exclude=[],
              runtime_tmpdir=None,
              console=False , icon='icon.ico')
else:
    exe = EXE(pyz,
              a.scripts,
              [],
              exclude_binaries=True,
              name='deemix-pyweb',
              debug=False,
              bootloader_ignore_signals=False,
              strip=False,
              upx=True,
              console=False,
              icon="icon.ico")
    coll = COLLECT(exe,
                   a.binaries,
                   a.zipfiles,
                   a.datas,
                   strip=False,
                   upx=True,
                   upx_exclude=[],
                   name='deemix-pyweb')
