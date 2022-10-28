# -*- mode: python -*-

block_cipher = pyi_crypto.PyiBlockCipher(key='123')
curdir = ".."

hidden_imports = [
	"os"
]

datas = [
	(os.path.join(curdir, "Data"), os.path.join(".", "Data")),
	(os.path.join(curdir, "platforms"), os.path.join(".", "platforms")),

]

pathex = [
]


a = Analysis(
	['../main.py'],
	pathex=pathex,
	binaries=[],
	datas=datas,
	hiddenimports=hidden_imports,
	hookspath=[],
	runtime_hooks=[],
	excludes=[],
	win_no_prefer_redirects=False,
	win_private_assemblies=False,
	cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
	pyz,
	a.scripts,
	exclude_binaries=True,
	name='Beans',
	debug=False,
	strip=False,
	upx=True,
	console=False, uac_admin=False,
	version='file_version_info.txt',
	icon=os.path.join(curdir, "Res", "logo.ico")
	)

coll = COLLECT(
	exe,
	a.binaries,
	a.zipfiles,
	a.datas,
	strip=False,
	upx=True,
	name='Beans')
