from json import *
from os.path import expanduser
from glob import glob
from zipfile import ZipFile

lang = 'fr_fr'

hash = loads(open(expanduser('~/AppData/Roaming/.minecraft/assets/indexes/2.json'), 'r', encoding='utf-8').read())['objects'][f'minecraft/lang/{lang}.json']['hash']
# hash = loads(open(expanduser('~/AppData/Roaming/.minecraft/assets/indexes/1.19.json'), 'r', encoding='utf-8').read())['objects']['minecraft/lang/en_gb.json']['hash']
print(hash)

trans = loads(open(expanduser(f'~/AppData/Roaming/.minecraft/assets/objects/{hash[:2]}/{hash}'), 'r', encoding='utf-8').read())
out = loads(ZipFile(expanduser('~/AppData/Roaming/.minecraft/versions/1.19.3/1.19.3.jar')).open('assets/minecraft/lang/en_us.json').read())

for k in trans:
	if k in out:
		out[k] = trans[k] + ' / ' + out[k]

for mod in ('comforts', 'biomesoplenty','cfm','jei','sereneseasons','mcw-paths','mcw-roofs','mcw-bridges','mcw-trapdoors','mcw-doors','mcw-windows','mcw-fences','mcw-lights','mcw-paintings','wthit','xaeros_minimap','moonlight'):
	try:
		mod_trans = loads(ZipFile(glob(expanduser(f'~/AppData/Roaming/.minecraft/mods/{mod}*.jar'))[0]).open(f'assets/{mod.replace("-","").replace("trap","trp").replace("wthit","waila").replace("xaeros_","xaero")}/lang/{lang}.json').read().decode('utf-8'))
		mod_en = loads(ZipFile(glob(expanduser(f'~/AppData/Roaming/.minecraft/mods/{mod}*.jar'))[0]).open(f'assets/{mod.replace("-","").replace("trap","trp").replace("wthit","waila").replace("xaeros_","xaero")}/lang/en_us.json').read().decode('utf-8'))

		for k in mod_trans:
			if k in mod_en:
				mod_en[k] = mod_trans[k] + ' / ' + mod_en[k]
		for k in mod_en:
			out[k] = mod_en[k]
	except Exception as e:
		print(e)

open(f'cm_{lang[:2]}.json', 'w', encoding='utf-8').write(dumps(out, indent=2))
