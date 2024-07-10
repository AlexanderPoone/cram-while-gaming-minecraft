'''
Copyleft Alexander Poone 2024 Edutainment.

Main script. Outputs Minecraft resource pack for language learning while gaming.
'''

from glob import glob
from json import *
from os.path import exists, expanduser
from pickle import dump, load
from re import finditer, sub
from shutil import copytree, copy2
from zipfile import ZipFile

from optional_village_names import patch_village_names
from optional_villager_names import patch_villager_names

##################################################
#    User Config              TODO: Tkinter GUI
##################################################

LANGUAGES_TO_BE_PATCHED = ('fr_fr', 'es_es', 'es_ar', 'ja_jp', 'de_de')
VERSION_TO_BE_PATCHED = '1.21'

##################################################
#    Constants
##################################################
CURSEFORGE_INSTALLED = exists(expanduser('~/curseforge/minecraft'))
LEAPFROG = '1.21'						        # Leapfrog to the latest translation, e.g., 1.20.6 using 1.21's updated translation.
SUPPORTED_MOD_LIST = ('advancementframes',		# It doesn't matter if some mods are not installed, the script will skip them.
            'areas',
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
        f'~/curseforge/minecraft/Instances/{VERSION_TO_BE_PATCHED}')
else:
    MC_HOME = MC_MODS = expanduser('~/AppData/Roaming/.minecraft')

out = loads(ZipFile(f'{MC_HOME}/versions/{LEAPFROG}/{LEAPFROG}.jar').open(
    'assets/minecraft/lang/en_us.json').read())


##################################################
#    Translation
##################################################
def main():
    for LANG in LANGUAGES_TO_BE_PATCHED:
        latestHashInt = sorted([int(x.split('.')[0].split('\\')[-1]) for x in glob(f'{MC_HOME}/assets/indexes\\*')])[-1]
        hash = loads(open(f'{MC_HOME}/assets/indexes/{latestHashInt}.json', 'r',
                     encoding='utf-8').read())['objects'][f'minecraft/lang/{LANG}.json']['hash']
        print('Hash found: ', hash)

        trans = loads(open(
            f'{MC_HOME}/assets/objects/{hash[:2]}/{hash}', 'r', encoding='utf-8').read())

        # print(set([trans[k].split(' ')[0].lower() for k in trans if k.startswith('item.minecraft') or k.startswith('block.minecraft')]))
        kbase = None
        if exists(f'knowledgebase/mc_{LANG}.pickle'):
            with open(f'knowledgebase/mc_{LANG}.pickle', 'rb') as f:
                kbase = load(f)

        ##################################################
        #    Payload
        ##################################################
        for k in trans:
            if k in out:
                if LANG.startswith('es_'):
                    out[k] = sub('(?<!C|S|P|c|s|p)h', '<h>', trans[k].replace('iencio', '`iencio').replace('iencia', '`iencia').replace('ienso', '`ienso').replace('iensa', '`iensa').replace('iense', '`iense').replace('iento', '`iento').replace('ienta', '`ienta').replace('iente', '`iente').replace(
                        'iende', '`iende').replace('iando', '`iando').replace('ianda', '`ianda').replace('uevo', '`uevo').replace('ueva', '`ueva').replace('ueve', '`ueve').replace('ier', '`ier').replace('uer', '`uer').replace('v', 'v(b)').replace('H', '<H>').replace('V', 'V(B)')) + ' / ' + out[k].replace('%s', '●')
                elif LANG.startswith('fr_'):
                    if kbase is not None:            # if the grammar file for that language exists
                        if k.startswith('item.minecraft') or k.startswith('block.minecraft') or k.startswith('entity.minecraft') or k.startswith('biome.') or k.startswith('container.'):
                            spl = trans[k].split(' ')
                            firstword = spl[0].lower()
                            rest = ' '.join(spl[1:])
                            if rest != '':
                                rest = f' {rest}'
                            if firstword in kbase:
                                if kbase[firstword] == 'm':
                                    trans[k] = f'Un {firstword}{rest}'
                                if kbase[firstword] == 'f':
                                    trans[k] = f'Une {firstword}{rest}'
                                if kbase[firstword] == 'p':
                                    trans[k] = f'Des {firstword}{rest}'
                    tmp = sub(r'iz(?=$| )', 'i<z>', sub(r'mp(?=$| )', '<mp>', sub(r'(?<!C|S|P|c|s|p)h', '<h>', sub(
                        r'(?<!C|S|P|c|s|p)H', '<H>', trans[k])))).replace('ufs', '<ufs>')
                    foo = finditer(r' qui (se )?[a-zéèç"]+nt(?= |$|\.)', tmp)
                    for bar in foo:
                        # print(bar.group(), sub('nt$', '<nt>', bar.group()))
                        tmp = tmp.replace(bar.group(), sub('nt$', '<nt>', bar.group()))
                    if out[k] != tmp:
                        out[k] = tmp + ' / ' + out[k].replace('%s', '●')
                elif LANG.startswith('de_'):
                    if kbase is not None:            # if the grammar file for that language exists
                        if k.startswith('item.minecraft') or k.startswith('block.minecraft') or k.startswith('entity.minecraft') or k.startswith('biome.') or k.startswith('container.'):
                            spl = trans[k].split(' ')
                            firstword = spl[0]
                            rest = ' '.join(spl[1:])
                            if rest != '':
                                rest = f' {rest}'
                            if firstword in kbase:
                                if kbase[firstword] == 'm':
                                    trans[k] = f'Der {firstword}{rest}'
                                if kbase[firstword] == 'f':
                                    trans[k] = f'Die {firstword}{rest}'
                                if kbase[firstword] == 'n':
                                    trans[k] = f'Das {firstword}{rest}'
                                if kbase[firstword] == 'p':
                                    trans[k] = f'(pl.) {firstword}{rest}'
                    if out[k] != trans[k]:
                        out[k] = trans[k] + ' / ' + out[k].replace('%s', '●')
                else:
                    if out[k] != trans[k]:
                        out[k] = trans[k] + ' / ' + out[k].replace('%s', '●')

        for mod in SUPPORTED_MOD_LIST:
            try:
                mod_trans_json_str = sub('//.*', '', ZipFile(glob(f'{MC_MODS}/mods/{mod}*.jar')[0]).open(f'assets/{mod.replace("-", "").replace("trap", "trp").replace(
                    "wthit", "waila").replace("xaeros_", "xaero").replace("betterpvp", "xaerobetterpvp").replace("oculus", "iris")}/lang/{LANG}.json').read().decode('utf-8'))
                mod_trans = loads(mod_trans_json_str)
                mod_en = loads(ZipFile(glob(f'{MC_MODS}/mods/{mod}*.jar')[0]).open(f'assets/{mod.replace("-", "").replace("trap", "trp").replace(
                    "wthit", "waila").replace("xaeros_", "xaero").replace("betterpvp", "xaerobetterpvp").replace("oculus", "iris")}/lang/en_us.json').read().decode('utf-8'))

                for k in mod_trans:
                    if k in mod_en:
                        if LANG.startswith('es_'):
                            mod_en[k] = sub('(?<!C|S|P|c|s|p)h', '<h>', mod_trans[k].replace('iencio', '`iencio').replace('iencia', '`iencia').replace('ienso', '`ienso').replace('iensa', '`iensa').replace('iense', '`iense').replace('iento', '`iento').replace('ienta', '`ienta').replace('iente', '`iente').replace(
                                'iende', '`iende').replace('iando', '`iando').replace('ianda', '`ianda').replace('uevo', '`uevo').replace('ueva', '`ueva').replace('ueve', '`ueve').replace('ier', '`ier').replace('uer', '`uer').replace('v', 'v(b)').replace('H', '<H>').replace('V', 'V(B)')) + ' / ' + mod_en[k].replace('%s', '●')
                        elif LANG.startswith('fr_'):
                            if kbase is not None:            # if the grammar file for that language exists
                                if k.startswith('item.') or k.startswith('block.') or k.startswith('entity.') or k.startswith('biome.'):
                                    spl = mod_trans[k].split(' ')
                                    firstword = spl[0].lower()
                                    rest = ' '.join(spl[1:])
                                    if rest != '':
                                        rest = f' {rest}'
                                    if firstword in kbase:
                                        if kbase[firstword] == 'm':
                                            mod_trans[k] = f'Un {firstword}{rest}'
                                        if kbase[firstword] == 'f':
                                            mod_trans[k] = f'Une {firstword}{rest}'
                                        if kbase[firstword] == 'p':
                                            mod_trans[k] = f'Des {firstword}{rest}'

                                tmp = sub(r'iz(?=$| )', 'i<z>', sub(r'mp(?=$| )', '<mp>', sub(r'(?<!C|S|P|c|s|p)h', '<h>', sub(r'(?<!C|S|P|c|s|p)H', '<H>', mod_trans[k].replace(
                                    'éé', 'é'))))).replace(' de vérification', ' à damiers').replace('Block ', 'Bloc ').replace('ufs', '<ufs>').replace('Pattes', 'Pâtes')
                                foo = finditer(r' qui (se )?[a-zéèç"]+nt(?= |$|\.)', tmp)
                                for bar in foo:
                                    print(bar.group(), sub('nt$', '<nt>', bar.group()))
                                    tmp = tmp.replace(bar.group(), sub(
                                        'nt$', '<nt>', bar.group()))
                                if mod_en[k] != tmp:
                                    mod_en[k] = tmp + ' / ' + mod_en[k].replace('%s', '●')
                        elif LANG.startswith('de_'):
                            if kbase is not None:            # if the grammar file for that language exists
                                if k.startswith('item.') or k.startswith('block.') or k.startswith('entity.') or k.startswith('biome.'):
                                    spl = mod_trans[k].split(' ')
                                    firstword = spl[0].replace('Kokusnuss', 'Kokosnuss')
                                    rest = ' '.join(spl[1:])
                                    if rest != '':
                                        rest = f' {rest}'
                                    if firstword in kbase:
                                        if kbase[firstword] == 'm':
                                            mod_trans[k] = f'Der {firstword}{rest}'
                                        if kbase[firstword] == 'f':
                                            mod_trans[k] = f'Die {firstword}{rest}'
                                        if kbase[firstword] == 'n':
                                            mod_trans[k] = f'Das {firstword}{rest}'
                                        if kbase[firstword] == 'p':
                                            mod_trans[k] = f'(pl.) {firstword}{rest}'
                            if mod_en[k] != mod_trans[k]:
                                mod_en[k] = mod_trans[k] + ' / ' + mod_en[k].replace('%s', '●')
                        else:
                            if mod_en[k] != mod_trans[k]:
                                mod_en[k] = mod_trans[k] + ' / ' + mod_en[k].replace('%s', '●')
                for k in mod_en:
                    out[k] = mod_en[k]
                print(mod, ' ' * (30-len(mod)), '☑️ Done.')
            except KeyError as e:
                print(mod, ' ' * (30-len(mod)), 'Translation file not found, skipping...')
            except IndexError as e:
                print(mod, ' ' * (30-len(mod)), 'Mod not found, skipping...')
            except Exception as e:
                # Get the Peninsular Spanish translation file if there's no Rioplatense Spanish.
                if LANG == 'es_ar':
                    try:
                        mod_trans = loads(ZipFile(glob(f'{MC_MODS}/mods/{mod}*.jar')[0]).open(f'assets/{mod.replace("-", "").replace("trap", "trp").replace(
                            "wthit", "waila").replace("xaeros_", "xaero").replace("betterpvp", "xaerobetterpvp").replace("oculus", "iris")}/lang/es_mx.json').read().decode('utf-8'))
                        mod_en = loads(ZipFile(glob(f'{MC_MODS}/mods/{mod}*.jar')[0]).open(f'assets/{mod.replace("-", "").replace("trap", "trp").replace(
                            "wthit", "waila").replace("xaeros_", "xaero").replace("betterpvp", "xaerobetterpvp").replace("oculus", "iris")}/lang/en_us.json').read().decode('utf-8'))

                        for k in mod_trans:
                            if k in mod_en:
                                if LANG.startswith('es_'):
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
                                    if LANG.startswith('es_'):
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

        outfilename = f'resourcepacks/crammese/assets/minecraft/lang/cm_{"ar" if LANG == "es_ar" else LANG[:2]}.json'
        open(outfilename, 'w', encoding='utf-8').write(dumps(out, indent=2))

        # If resourcepack folder is not present under installation, copy local resourcepack folder to destination
        if not exists(f'{MC_MODS}/resourcepacks'):
            copytree('resourcepacks', f'{MC_MODS}/resourcepacks')
        elif not exists(f'{MC_MODS}/resourcepacks/crammese'):
            copytree('resourcepacks/crammese', f'{MC_MODS}/resourcepacks/crammese')
        elif not exists(f'{MC_MODS}/{outfilename}'):
            copy2(outfilename, f'{MC_MODS}/{outfilename}')
        else:
            open(f'{MC_MODS}/{outfilename}', 'w', encoding='utf-8').write(dumps(out, indent=2))

if __name__ == '__main__':
    main()
    patch_village_names(VERSION_TO_BE_PATCHED)
    patch_villager_names(VERSION_TO_BE_PATCHED)