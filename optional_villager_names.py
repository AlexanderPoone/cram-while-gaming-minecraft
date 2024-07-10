'''
Copyleft Alexander Poone 2024 Edutainment.

Learn languages by checking out Minecraft villager names. Requires the `Villager Names` mod by Serilum: https://www.curseforge.com/minecraft/mc-mods/villager-names

e.g., on Windows, folder containing replaced file (replace 1.21 w/ any version) is:    %USERPROFILE%/curseforge/minecraft/Instances/1.21/config/collective
'''

from json import dumps
from os.path import expanduser
from re import sub

OUT = {                         # Customise for your own needs. This works like flashcards, content can be Incoterms, Docker commands or whatever.
    "female_names": [
        "La m`ouette",
        "Une autruche",
        "La luciole",
        "La girafe - originaire d'Afrique",
        "La limace",
        "La puce",
        "U{ne an}guille électrique",
        "Sarah Bernhardt - La Voi<x> d'or",
        "Surya Bonaly - patineuse artistique",
    ],
    "male_names": [
        "Le pic",
        "Le corbeau",
        "Le moineau",
        "Le martin-pêcheur",
        "Le rouge-gorge",
        "Le guépar<d>",
        "Le léopar<d>",
        "Le moustique",
        "LE zèbre - originaire d'Afrique",
        "Le phoque",
        "Le lion de mer",
        "L'épaular<d>",
        "Le raton laveur",
        "Le mendiant",
        "L'escroc",
        "Le flemmar<d>",
        "Le paresseux",
        "Le casse-cou"
        "Le clochar<d>",
        "Le radin",
        "Le séduisant",
        "Le décontracté",
        "L'insaisissable",
        "L'incendiaire",
        "L'agent provocateur",
        "Le casse-pie<ds>",
        "L'agaçant",
        "Le fatigant",
        "Le pénible",
        "Le misant<h>rope",
        "Le bourgeois gentil<h>omme - Comédie-ballet de Molière",
        "Le retardataire",
        "L'expéditeur",
        "Le destinataire",
        "Le bénéficiare",
        "Le chef de clan",
        "Le mercenaire",
        "Le condescendant",
        "Le bavar<d> (comme une pie), le moulin | à paroles",
        "Le maladif/chétif",
        "Le glouton",
        "Le gourman<d>",
        "L'écervelé",
        "Le rusé",
        "Le parvenu",
        "L'excentrique",
        "L'exténué",
        "Le taquin",
        "Le misogyne beauf",
        "Le pyromane",
        "La rouille",
        "Le détenteur du titre",
        "Le coupable",
        "Le timbré",
        "Le balayeur",
        "Le grassouillet",
        "Le maigrichon",
        "Le qui parle d'une manière affectée",
        "Le qui se mêle de tout",
        "Le qui ronfle fort/bruyamment",
        "Le qui claque des doi<gts>",
        "Le qui se gratte le visage",
        "L'homme des cavernes",
        "Christophe Colomb - colon, capitaine, adventurier",
        "Johnny Hallyday - Le rock",
        "Platon - Le Banquet",
        "Jean Renoir - La règle du jeu",
        "Arthur Rimbaud - Le Bateau ivre",
        "Gustave Flaubert - Madame Bovary",
        "André Malraux - La Condition <H>umaine",
        "Alain Delon - Le Samouraï",
        "Jules Verne I - Le voyage au centre de la Terre",
        "Jules Verne II - Le tour du monde en quatre-vingts jours",
        "Guy de Maupassant I - La parure (cette nouvelle est connu pour retournement final)",
        "Guy de Maupassant II - Boule de suif",
        "Alexandre Dumas père - Le Comte de Monte-Cristo",
        "Alexandre Dumas fils - La Dame aux camélias",
        "Francis Poulenc - Concert champêtre",
        "Henri Matisse - Papier découpé",
        "Ingre<s> - La Grande Odalisque",
        "Nicolas Poussin - L'Enlèvement des Sabines",
        "Caravage - La nature morte",
        "Léonard de Vinci - L'Homme de Vitruve",
        "Thierry Hermès - La marque de luxe française qui porte son nom",
        "Jean Cocteau - Orphée",
        "Romain Rollan<d> - Jean-Christophe",
        "Bourvil - La Grande Vadrouille",
        "Les Grandes Espérances",
        "Révolution de Juillet porte sur le trône un nouveau roi, Louis-Philippe Ier - Trois Glorieuses - La Liberté guidant le peuple",
        "Le Printemps - Grand magasin",
        "Les Galeries Lafayette <H>aussmann[Osman] - Le boulevard <H>aussmann",
        "Georges-Eugène <H>aussmann[Osman] - transformations de Paris sous le 2d(<t) Em>pire: espaces ver<ts>, mobilier urbain, égou<ts>",
    ]
}

def patch_villager_names(VERSION_TO_BE_PATCHED = '1.20.6'):
    print('##################################################')
    print('Patching Villager Names...')
    REPLACE_PATH = expanduser(
        f"~/curseforge/minecraft/Instances/{VERSION_TO_BE_PATCHED}/config/collective/entity_names.json")

    # Change configuration
    content = None
    with open(expanduser(f"~/curseforge/minecraft/Instances/1.21/config/villagernames.json5"), 'r+', encoding='utf-8') as f:
        content = f.read()
        content = sub('(?<="shouldCapitalizeNames": ).*', 'false', content)
        # print(content)
    with open(expanduser(f"~/curseforge/minecraft/Instances/1.21/config/villagernames.json5"), 'w', encoding='utf-8') as f:
        f.write(content)

    open(REPLACE_PATH, 'w', encoding='utf-8').write(dumps(OUT, indent=2))


if __name__ == '__main__':
    patch_villager_names()