# -*- mode: python -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['C:\\Users\\ronasen\\Desktop\\juli_space\\cdj_acc\\web'],
             binaries=[],
             datas=[('templates', 'templates'), ('sqlite', 'sqlite'), ('static', 'static')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='app',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )