from json import *
from os.path import expanduser
from glob import glob
from zipfile import ZipFile
from re import sub

lang = 'ja_jp'

hash = loads(open(expanduser('~/AppData/Roaming/.minecraft/assets/indexes/4.json'), 'r', encoding='utf-8').read())['objects'][f'minecraft/lang/{lang}.json']['hash']
# hash = loads(open(expanduser('~/AppData/Roaming/.minecraft/assets/indexes/1.19.json'), 'r', encoding='utf-8').read())['objects']['minecraft/lang/en_gb.json']['hash']
print(hash)

trans = loads(open(expanduser(f'~/AppData/Roaming/.minecraft/assets/objects/{hash[:2]}/{hash}'), 'r', encoding='utf-8').read())
out = loads(ZipFile(expanduser('~/AppData/Roaming/.minecraft/versions/23w14a/23w14a.jar')).open('assets/minecraft/lang/en_us.json').read())

for k in trans:
	if k in out:
		if lang.startswith('es_'):
			out[k] = sub('(?<!C|S|c|s)h', '<h>', trans[k].replace('iencio','`iencio').replace('iencia','`iencia').replace('ienso','`ienso').replace('iensa','`iensa').replace('iense','`iense').replace('iento','`iento').replace('ienta','`ienta').replace('iente','`iente').replace('iende','`iende').replace('iando','`iando').replace('ianda','`ianda').replace('uevo','`uevo').replace('ueva','`ueva').replace('ueve','`ueve').replace('ier','`ier').replace('uer','`uer').replace('v','v(b)').replace('H','<H>').replace('V','V(B)')) + ' / ' + out[k].replace('%s','')
		elif lang.startswith('fr_'):
			out[k] = sub('(?<!C|S|c|s)h', '<h>', trans[k]) + ' / ' + out[k].replace('%s','')
		else:
			out[k] = trans[k] + ' / ' + out[k].replace('%s','')

for mod in ('comforts', 'biomesoplenty','cfm','jei','sereneseasons','mcw-paths','mcw-roofs','mcw-bridges','mcw-trapdoors','mcw-doors','mcw-windows','mcw-fences','mcw-lights','mcw-paintings','wthit','xaeros_minimap','moonlight','betterpvp','jade'):
	try:
		mod_trans = loads(ZipFile(glob(expanduser(f'~/AppData/Roaming/.minecraft/mods/{mod}*.jar'))[0]).open(f'assets/{mod.replace("-","").replace("trap","trp").replace("wthit","waila").replace("xaeros_","xaero").replace("betterpvp","xaerobetterpvp")}/lang/{lang}.json').read().decode('utf-8'))
		mod_en = loads(ZipFile(glob(expanduser(f'~/AppData/Roaming/.minecraft/mods/{mod}*.jar'))[0]).open(f'assets/{mod.replace("-","").replace("trap","trp").replace("wthit","waila").replace("xaeros_","xaero").replace("betterpvp","xaerobetterpvp")}/lang/en_us.json').read().decode('utf-8'))

		for k in mod_trans:
			if k in mod_en:
				if lang.startswith('es_'):
					mod_en[k] = sub('(?<!C|S|c|s)h', '<h>', mod_trans[k].replace('iencio','`iencio').replace('iencia','`iencia').replace('ienso','`ienso').replace('iensa','`iensa').replace('iense','`iense').replace('iento','`iento').replace('ienta','`ienta').replace('iente','`iente').replace('iende','`iende').replace('iando','`iando').replace('ianda','`ianda').replace('uevo','`uevo').replace('ueva','`ueva').replace('ueve','`ueve').replace('ier','`ier').replace('uer','`uer').replace('v','v(b)').replace('H','<H>').replace('V','V(B)')) + ' / ' + mod_en[k].replace('%s','')
				elif lang.startswith('fr_'):
					out[k] = sub('(?<!C|S|c|s)h', '<h>', mod_trans[k]) + ' / ' + mod_en[k].replace('%s','')
				else:
					mod_en[k] = mod_trans[k] + ' / ' + mod_en[k].replace('%s','')
		for k in mod_en:
			out[k] = mod_en[k]
	except Exception as e:
		if lang == 'es_ar':
			try:
				mod_trans = loads(ZipFile(glob(expanduser(f'~/AppData/Roaming/.minecraft/mods/{mod}*.jar'))[0]).open(f'assets/{mod.replace("-","").replace("trap","trp").replace("wthit","waila").replace("xaeros_","xaero").replace("betterpvp","xaerobetterpvp")}/lang/es_mx.json').read().decode('utf-8'))
				mod_en = loads(ZipFile(glob(expanduser(f'~/AppData/Roaming/.minecraft/mods/{mod}*.jar'))[0]).open(f'assets/{mod.replace("-","").replace("trap","trp").replace("wthit","waila").replace("xaeros_","xaero").replace("betterpvp","xaerobetterpvp")}/lang/en_us.json').read().decode('utf-8'))

				for k in mod_trans:
					if k in mod_en:
						if lang.startswith('es_'):
							mod_en[k] = sub('(?<!C|c)h', '<h>', mod_trans[k].replace('iencio','`iencio').replace('iencia','`iencia').replace('ienso','`ienso').replace('iensa','`iensa').replace('iense','`iense').replace('iento','`iento').replace('ienta','`ienta').replace('iente','`iente').replace('iende','`iende').replace('iando','`iando').replace('ianda','`ianda').replace('uevo','`uevo').replace('ueva','`ueva').replace('ueve','`ueve').replace('ier','`ier').replace('uer','`uer').replace('v','v(b)').replace('H','<H>').replace('V','V(B)')) + ' / ' + mod_en[k].replace('%s','')
						else:
							mod_en[k] = mod_trans[k] + ' / ' + mod_en[k].replace('%s','')
				for k in mod_en:
					out[k] = mod_en[k]
			except:
				try:
					mod_trans = loads(ZipFile(glob(expanduser(f'~/AppData/Roaming/.minecraft/mods/{mod}*.jar'))[0]).open(f'assets/{mod.replace("-","").replace("trap","trp").replace("wthit","waila").replace("xaeros_","xaero").replace("betterpvp","xaerobetterpvp")}/lang/es_es.json').read().decode('utf-8'))
					mod_en = loads(ZipFile(glob(expanduser(f'~/AppData/Roaming/.minecraft/mods/{mod}*.jar'))[0]).open(f'assets/{mod.replace("-","").replace("trap","trp").replace("wthit","waila").replace("xaeros_","xaero").replace("betterpvp","xaerobetterpvp")}/lang/en_us.json').read().decode('utf-8'))

					for k in mod_trans:
						if k in mod_en:
							if lang.startswith('es_'):
								mod_en[k] = sub('(?<!C|c)h', '<h>', mod_trans[k].replace('iencio','`iencio').replace('iencia','`iencia').replace('ienso','`ienso').replace('iensa','`iensa').replace('iense','`iense').replace('iento','`iento').replace('ienta','`ienta').replace('iente','`iente').replace('iende','`iende').replace('iando','`iando').replace('ianda','`ianda').replace('uevo','`uevo').replace('ueva','`ueva').replace('ueve','`ueve').replace('ier','`ier').replace('uer','`uer').replace('v','v(b)').replace('H','<H>').replace('V','V(B)')) + ' / ' + mod_en[k].replace('%s','')
							else:
								mod_en[k] = mod_trans[k] + ' / ' + mod_en[k].replace('%s','')
					for k in mod_en:
						out[k] = mod_en[k]
				except Exception as ee:
					print(64, ee)		
		else:
			print(66, e)

open(f'cm_{"ar" if lang == "es_ar" else lang[:2]}.json', 'w', encoding='utf-8').write(dumps(out, indent=2))
