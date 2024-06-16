'''
Copyleft Alexander Poone 2024 Edutainment.

Learn languages by checking out Minecraft villager names. Requires `Villager Names` mod installed.

e.g., on Windows, path of replaced file (replace 1.20.6 w/ any version) is:    %USERPROFILE%/curseforge/minecraft/Instances/1.20.6/config/collective
'''

from json import dumps
from os.path import expanduser

VERSION_TO_BE_CHANGED = '1.20.6'
REPLACE_PATH = expanduser(
    f"~/curseforge/minecraft/Instances/{VERSION_TO_BE_CHANGED}/config/collective/entity_names.json")

OUT = {
    "female_names": [
    ],
    "male_names": [
        "Le pic",
        "Le corbeau",
        "Le moineau",
        "La mouette",
        "Le martin-pêcheur",
        "Le rouge-gorge",
        "Une autruche",
        "Le guépar<d>",
        "Le léopar<d>",
        "La luciole",
        "Le moustique",
        "La girafe - originaire d'Afrique",
        "LE zèbre - originaire d'Afrique",
        "La puce",
        "Le phoque",
        "Le lion de mer",
        "L'épaular<d>",
        "L'anguille électrique",
        "Le raton laveur",
        "Le mendiant",
        "L'escroc",
        "Le flemmar<d>",
        "Le paresseux",
        "Le casse-cou"
        "Le clochard",
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
        "Le glouton",
        "Le gourman<d>",
        "L'écervelé",
        "Le rusé",
        "Le parvenu",
        "L'excentrique",
        "L'exténué",
        "Le taquin",
        "Le beauf",
        "Le pyromane",
        "La rouille",
        "Le détenteur du titre",
        "On qui se mêle de tout",
        "Christophe Colomb",
        "Johnny Hallyday - Le rock",
        "Sarah Bernhardt - La Voix d'or",
        "Platon - Le Banquet",
        "Jean Renoir - La règle du jeu",
        "Arthur Rimbaud - Le Bateau ivre",
        "Gustave Flaubert - Madame Bovary",
        "André Malraux - La Condition <H>umaine",
        "Alain Delon - Le Samouraï",
        "Jules Verne - Voyage au centre de la Terre",
        "Francis Poulenc - Concert champêtre",
        "Henri Matisse - Papier découpé",
        "Ingre<s> - La Grande Odalisque",
        "Nicolas Poussin - L'Enlèvement des Sabines",
        "Caravage - La nature morte",
        "Léonard de Vinci - L'Homme de Vitruve",
        "Thierry Hermès - La marque de luxe française qui porte son nom",
        "Jean Cocteau - Orphée",
        "Bourvil - La Grande Vadrouille",
        "Les Grandes Espérances",
        "Le Printemps - Grand magasin",
        "Les Galeries Lafayette <H>aussmann - Le boulevard <H>aussmann",
        "Georges-Eugène <H>aussmann - transformations de Paris sous le Second Empire: espaces verts, mobilier urbain, égouts",
        "Surya Bonaly - patineuse artistique",
    ]
}

open(REPLACE_PATH, 'w', encoding='utf-8').write(dumps(OUT, indent=2))
