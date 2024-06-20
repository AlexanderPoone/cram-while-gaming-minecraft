'''
Copyleft Alexander Poone 2024 Edutainment.

Main script. Outputs Minecraft resource pack for language learning while gaming.
'''

from glob import glob
from json import *
from os.path import exists, expanduser
from pickle import dump, load
from re import finditer, sub
from zipfile import ZipFile

CURSEFORGE_INSTALLED = exists(expanduser('~/curseforge/minecraft'))
VERSION_TO_BE_CHANGED = '1.20.6'
LEAPFROG = '1.21'						        # Leapfrog to the latest translation, e.g., 1.20.6 using 1.21's updated translation.
SUPPORTED_MOD_LIST = ('advancementframes',		# It doesn't matter if some mods are not installed, the script will skip them.
            'betterlily',
            'betterpvp',
            'biomesoplenty',
            'cfm',
            'comforts',
            'croptopia',
            'curios',
            'dummmmmmy',
            'explorerscompass',
            'farmersdelight',
            'goated',
            'hauntedharvest',
            'heartstone',
            'jade',
            'jeed',
            'jei',
            'labels',
            'map_atlases',
            'mcw-bridges',
            'mcw-doors',
            'mcw-fences',
            'mcw-lights',
            'mcw-paintings',
            'mcw-paths',
            'mcw-roofs',
            'mcw-trapdoors',
            'mcw-windows',
            'modmenu',
            'moonlight',
            'moyai',
            'naturescompass',
            'oculus',
            'polytone',
            'sereneseasons',
            'sleep_tight',
            'smarterfarmers',
            'snowyspirit',
            'supplementaries',
            'suppsquared',
            'terralith',
            'toughasnails',
            'wthit',
            'xaeros_minimap',)

if CURSEFORGE_INSTALLED:
    MC_HOME = expanduser('~/curseforge/minecraft/Install')
    MC_MODS = expanduser(
        f'~/curseforge/minecraft/Instances/{VERSION_TO_BE_CHANGED}')
else:
    MC_HOME = MC_MODS = expanduser('~/AppData/Roaming/.minecraft')

# TODO: Tkinter GUI
lang = 'ja_jp'      # e.g., 'fr_fr', 'fr_be', 'es_es', 'es_ar', 'ja_jp', 'de_de'

# TODO: find latest file, not hardcoding '5' and '1.20'
# hash = loads(open(expanduser('~/AppData/Roaming/.minecraft/assets/indexes/1.19.json'), 'r', encoding='utf-8').read())['objects']['minecraft/lang/en_gb.json']['hash']
hash = loads(open(f'{MC_HOME}/assets/indexes/16.json', 'r',
             encoding='utf-8').read())['objects'][f'minecraft/lang/{lang}.json']['hash']
print('Hash found: ', hash)

trans = loads(open(
    f'{MC_HOME}/assets/objects/{hash[:2]}/{hash}', 'r', encoding='utf-8').read())
out = loads(ZipFile(f'{MC_HOME}/versions/{LEAPFROG}/{LEAPFROG}.jar').open(
    'assets/minecraft/lang/en_us.json').read())

# print(set([trans[k].split(' ')[0].lower() for k in trans if k.startswith('item.minecraft') or k.startswith('block.minecraft')]))
worddict = None
if exists(f'mc_{lang}.pickle'):
    with open(f'mc_{lang}.pickle', 'rb') as f:
        worddict = load(f)

for k in trans:
    if k in out:
        if lang.startswith('es_'):
            out[k] = sub('(?<!C|S|P|c|s|p)h', '<h>', trans[k].replace('iencio', '`iencio').replace('iencia', '`iencia').replace('ienso', '`ienso').replace('iensa', '`iensa').replace('iense', '`iense').replace('iento', '`iento').replace('ienta', '`ienta').replace('iente', '`iente').replace(
                'iende', '`iende').replace('iando', '`iando').replace('ianda', '`ianda').replace('uevo', '`uevo').replace('ueva', '`ueva').replace('ueve', '`ueve').replace('ier', '`ier').replace('uer', '`uer').replace('v', 'v(b)').replace('H', '<H>').replace('V', 'V(B)')) + ' / ' + out[k].replace('%s', '●')
        elif lang.startswith('fr_'):
            if worddict is not None:            # if the grammar file for that language exists
                if k.startswith('item.minecraft') or k.startswith('block.minecraft') or k.startswith('entity.minecraft'):
                    spl = trans[k].split(' ')
                    firstword = spl[0].lower()
                    rest = ' '.join(spl[1:])
                    if firstword in worddict:
                        if worddict[firstword] == 'm':
                            trans[k] = f'Un {firstword} {rest}'
                        if worddict[firstword] == 'f':
                            trans[k] = f'Une {firstword} {rest}'
                        if worddict[firstword] == 'p':
                            trans[k] = f'Des {firstword} {rest}'
            tmp = sub(r'iz(?=$| )', 'i<z>', sub(r'mp(?=$| )', '<mp>', sub(r'(?<!C|S|P|c|s|p)h', '<h>', sub(
                r'(?<!C|S|P|c|s|p)H', '<H>', trans[k])))).replace('ufs', '<ufs>')
            foo = finditer(r' qui (se )?[a-zéèç"]+nt(?= |$|\.)', tmp)
            for bar in foo:
                # print(bar.group(), sub('nt$', '<nt>', bar.group()))
                tmp = tmp.replace(bar.group(), sub('nt$', '<nt>', bar.group()))
            if out[k] != tmp:
                out[k] = tmp + ' / ' + out[k].replace('%s', '●')
        else:
            out[k] = trans[k] + ' / ' + out[k].replace('%s', '●')

for mod in SUPPORTED_MOD_LIST:
    try:
        mod_trans_json_str = sub('//.*', '', ZipFile(glob(f'{MC_MODS}/mods/{mod}*.jar')[0]).open(f'assets/{mod.replace("-", "").replace("trap", "trp").replace(
            "wthit", "waila").replace("xaeros_", "xaero").replace("betterpvp", "xaerobetterpvp").replace("oculus", "iris")}/lang/{lang}.json').read().decode('utf-8'))
        mod_trans = loads(mod_trans_json_str)
        mod_en = loads(ZipFile(glob(f'{MC_MODS}/mods/{mod}*.jar')[0]).open(f'assets/{mod.replace("-", "").replace("trap", "trp").replace(
            "wthit", "waila").replace("xaeros_", "xaero").replace("betterpvp", "xaerobetterpvp").replace("oculus", "iris")}/lang/en_us.json').read().decode('utf-8'))

        for k in mod_trans:
            if k in mod_en:
                if lang.startswith('es_'):
                    mod_en[k] = sub('(?<!C|S|P|c|s|p)h', '<h>', mod_trans[k].replace('iencio', '`iencio').replace('iencia', '`iencia').replace('ienso', '`ienso').replace('iensa', '`iensa').replace('iense', '`iense').replace('iento', '`iento').replace('ienta', '`ienta').replace('iente', '`iente').replace(
                        'iende', '`iende').replace('iando', '`iando').replace('ianda', '`ianda').replace('uevo', '`uevo').replace('ueva', '`ueva').replace('ueve', '`ueve').replace('ier', '`ier').replace('uer', '`uer').replace('v', 'v(b)').replace('H', '<H>').replace('V', 'V(B)')) + ' / ' + mod_en[k].replace('%s', '●')
                elif lang.startswith('fr_'):
                    if worddict is not None:            # if the grammar file for that language exists
                        if k.startswith('item.') or k.startswith('block.') or k.startswith('entity.'):
                            spl = mod_trans[k].split(' ')
                            firstword = spl[0].lower()
                            rest = ' '.join(spl[1:])
                            if firstword in worddict:
                                if worddict[firstword] == 'm':
                                    mod_trans[k] = f'Un {firstword} {rest}'
                                if worddict[firstword] == 'f':
                                    mod_trans[k] = f'Une {firstword} {rest}'
                                if worddict[firstword] == 'p':
                                    mod_trans[k] = f'Des {firstword} {rest}'

                        tmp = sub(r'iz(?=$| )', 'i<z>', sub(r'mp(?=$| )', '<mp>', sub(r'(?<!C|S|P|c|s|p)h', '<h>', sub(r'(?<!C|S|P|c|s|p)H', '<H>', mod_trans[k].replace(
                            'éé', 'é'))))).replace(' de vérification', ' à damiers').replace('Block ', 'Bloc ').replace('ufs', '<ufs>').replace('Pattes', 'Pâtes')
                        foo = finditer(r' qui (se )?[a-zéèç"]+nt(?= |$|\.)', tmp)
                        for bar in foo:
                            print(bar.group(), sub('nt$', '<nt>', bar.group()))
                            tmp = tmp.replace(bar.group(), sub(
                                'nt$', '<nt>', bar.group()))
                        if mod_en[k] != tmp:
                            mod_en[k] = tmp + ' / ' + mod_en[k].replace('%s', '●')
                else:
                    mod_en[k] = mod_trans[k] + ' / ' + \
                        mod_en[k].replace('%s', '●')
        for k in mod_en:
            out[k] = mod_en[k]
        print(mod, ' ' * (30-len(mod)), '☑️ Done.')
    except KeyError as e:
        print(mod, ' ' * (30-len(mod)), 'Translation file not found, skipping...')
    except IndexError as e:
        print(mod, ' ' * (30-len(mod)), 'Mod not found, skipping...')
    except Exception as e:
        # Get another Spanish translation file if there's no Rioplatense Spanish.
        if lang == 'es_ar':
            try:
                mod_trans = loads(ZipFile(glob(f'{MC_MODS}/mods/{mod}*.jar')[0]).open(f'assets/{mod.replace("-", "").replace("trap", "trp").replace(
                    "wthit", "waila").replace("xaeros_", "xaero").replace("betterpvp", "xaerobetterpvp").replace("oculus", "iris")}/lang/es_mx.json').read().decode('utf-8'))
                mod_en = loads(ZipFile(glob(f'{MC_MODS}/mods/{mod}*.jar')[0]).open(f'assets/{mod.replace("-", "").replace("trap", "trp").replace(
                    "wthit", "waila").replace("xaeros_", "xaero").replace("betterpvp", "xaerobetterpvp").replace("oculus", "iris")}/lang/en_us.json').read().decode('utf-8'))

                for k in mod_trans:
                    if k in mod_en:
                        if lang.startswith('es_'):
                            mod_en[k] = sub('(?<!C|c)h', '<h>', mod_trans[k].replace('iencio', '`iencio').replace('iencia', '`iencia').replace('ienso', '`ienso').replace('iensa', '`iensa').replace('iense', '`iense').replace('iento', '`iento').replace('ienta', '`ienta').replace('iente', '`iente').replace(
                                'iende', '`iende').replace('iando', '`iando').replace('ianda', '`ianda').replace('uevo', '`uevo').replace('ueva', '`ueva').replace('ueve', '`ueve').replace('ier', '`ier').replace('uer', '`uer').replace('v', 'v(b)').replace('H', '<H>').replace('V', 'V(B)')) + ' / ' + mod_en[k].replace('%s', '●')
                        else:
                            mod_en[k] = mod_trans[k] + ' / ' + \
                                mod_en[k].replace('%s', '●')
                for k in mod_en:
                    out[k] = mod_en[k]
                print(mod, ' ' * (30-len(mod)), '☑️ Done.')
            except:
                try:
                    mod_trans = loads(ZipFile(glob(f'{MC_MODS}/mods/{mod}*.jar')[0]).open(f'assets/{mod.replace("-", "").replace("trap", "trp").replace(
                        "wthit", "waila").replace("xaeros_", "xaero").replace("betterpvp", "xaerobetterpvp").replace("oculus", "iris")}/lang/es_es.json').read().decode('utf-8'))
                    mod_en = loads(ZipFile(glob(f'{MC_MODS}/mods/{mod}*.jar')[0]).open(f'assets/{mod.replace("-", "").replace("trap", "trp").replace(
                        "wthit", "waila").replace("xaeros_", "xaero").replace("betterpvp", "xaerobetterpvp").replace("oculus", "iris")}/lang/en_us.json').read().decode('utf-8'))

                    for k in mod_trans:
                        if k in mod_en:
                            if lang.startswith('es_'):
                                mod_en[k] = sub('(?<!C|c)h', '<h>', mod_trans[k].replace('iencio', '`iencio').replace('iencia', '`iencia').replace('ienso', '`ienso').replace('iensa', '`iensa').replace('iense', '`iense').replace('iento', '`iento').replace('ienta', '`ienta').replace('iente', '`iente').replace(
                                    'iende', '`iende').replace('iando', '`iando').replace('ianda', '`ianda').replace('uevo', '`uevo').replace('ueva', '`ueva').replace('ueve', '`ueve').replace('ier', '`ier').replace('uer', '`uer').replace('v', 'v(b)').replace('H', '<H>').replace('V', 'V(B)')) + ' / ' + mod_en[k].replace('%s', '●')
                            else:
                                mod_en[k] = mod_trans[k] + ' / ' + \
                                    mod_en[k].replace('%s', '●')
                    for k in mod_en:
                        out[k] = mod_en[k]
                    print(mod, ' ' * (30-len(mod)), '☑️ Done.')
                except Exception as ee:
                    print(mod, ' ' * (30-len(mod)), f'❎ {ee}')
        else:
            print(mod, ' ' * (30-len(mod)), f'❎ {e}')

open(f'cm_{"ar" if lang == "es_ar" else lang[:2]}.json',
     'w', encoding='utf-8').write(dumps(out, indent=2))
