'''
Copyleft Alexander Poone 2024 Edutainment.

Learn languages by checking out Minecraft villager names. Requires the `Random Village Names` mod by Serilum: https://www.curseforge.com/minecraft/mc-mods/random-village-names

e.g., on Windows, folder containing replaced file (replace 1.21 w/ any version) is:    %USERPROFILE%/curseforge/minecraft/Instances/1.21/config/collective
'''

from json import dumps
from re import sub
from os.path import expanduser

OUT = {                         # Customise for yourself, e.g., Incoterms or Docker commands, I don't know
    "area_names": [
        "Vitry",
        "Créteil",
        "Asnières",
        "Courbevoie",
        "Versailles",
        "Colombes",
        "Aulnay-sous-Bois",
        "Rueil-Malmaison",
        "Aubervilliers",
        "Champigny",
        "Saint-Maur-des-Fossés",
        "Drancy",
        "Issy-les-Moulineaux",
        "Levallois-Perret",
        "Noisy-le-Grand",
        "Neuilly",
        "Antony",
        "Cergy",
        "Clichy",
        "Ivry",
        "Sarcelles",
        "Villejuif",
        "Épinay",
        "Maisons-Alfort",
        "Meaux",
        "Chelles",
        "Pantin",
        "Évry",
        "Fontenay-sous-Bois",
        "Bondy",
        "Le Blanc-Mesnil",
        "Clamart",
        "Sartrouville",
        "Bobigny",
        "Vincennes",
        "Montrouge",
        "Sevran",
        "Suresnes",
        "Corbeil-Essonnes",
        "Saint-Ouen",
        "Massy",
        "Mantes-la-Jolie",
        "Meudon",
        "Alfortville",
        "Puteaux",
        "Rosny-sous-Bois",
        "Gennevilliers",
        "Livry-Gargan",
        "Choisy-le-Roi",
        "Garges-lès-Gonesse",
        "Noisy-le-Sec",
        "La Courneuve",
        "Melun",
        "Saint-Germain-en-Laye",
        "Gagny",
        "Bagneux",
        "Pontault-Combault",
        "Poissy",
        "Savigny",
        "Stains",
        "Bagnolet",
        "Châtillon",
        "Sainte-Geneviève-des-Bois",
        "Villepinte",
        "Conflans-Sainte-Honorine",
        "Neuilly",
        "Tremblay-en-France",
        "Montigny-le-Bretonneux",
        "Le Perreux",
        "Franconville",
        "Châtenay-Malabry",
        "Villeneuve-Saint-Georges",
        "Houilles",
        "Les Mureaux",
        "Nogent",
        "Plaisir",
        "Palaiseau",
        "Goussainville",
        "L'Haÿ-les-Roses",
        "Viry-Châtillon",
        "Vigneux",
        "Chatou",
        "Trappes",
        "Clichy-sous-Bois",
        "Charenton-le-Pont",
        "Malakoff",
        "Athis-Mons",
        "Savigny-le-Temple",
        "Pontoise",
        "Cachan",
        "Thiais",
        "Villemomble",
        "Saint-Cloud",
        "Yerres",
        "Draveil",
        "Le Chesnay",
        "Bois-Colombes",
        "Le Plessis-Robinson",
        "La Garenne-Colombes",
        "Pierrefitte",
        "Villiers",
        "Vanves",
        "Ermont",
        "Bezons",
        "Grigny",
        "Guyancourt",
    ]
}

def patch_village_names(VERSION_TO_BE_PATCHED = '1.20.6'):
    print('##################################################')
    print('Patching Village Names...')
    REPLACE_PATH = expanduser(
        f"~/curseforge/minecraft/Instances/{VERSION_TO_BE_PATCHED}/config/collective/area_names.json")

    # Change configuration
    content = None
    with open(expanduser(f"~/curseforge/minecraft/Instances/1.21/config/areas.json5"), 'r+', encoding='utf-8') as f:
        content = f.read()
        content = sub('(?<="sendChatMessages": ).*?(?=,)', 'true', content)
        content = sub('(?<="enterPrefix": ").*?(?=")', 'Vous entrez à ', content)
        content = sub('(?<="leavePrefix": ").*?(?=")', 'Vous quittez ', content)
        # print(content)
    with open(expanduser(f"~/curseforge/minecraft/Instances/1.21/config/areas.json5"), 'w', encoding='utf-8') as f:
        f.write(content)

    open(REPLACE_PATH, 'w', encoding='utf-8').write(dumps(OUT, indent=2))

if __name__ == '__main__':
    patch_village_names()