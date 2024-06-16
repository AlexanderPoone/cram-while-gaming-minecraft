'''
Copyleft Alexander Poone 2024 Edutainment.

Learn languages by checking out Minecraft villager names. Requires the `Villager Names` mod by Serilum: https://www.curseforge.com/minecraft/mc-mods/villager-names

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
        "Le beauf",
        "Le pyromane",
        "La rouille",
        "Le détenteur du titre",
        "Le qui parle d'une manière affectée",
        "Le qui se mêle de tout",
        "L'homme des cavernes",
        "Christophe Colomb - colon, capitaine, adventurier",
        "Johnny Hallyday - Le rock",
        "Sarah Bernhardt - La Voi<x> d'or",
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
        "Bourvil - La Grande Vadrouille",
        "Les Grandes Espérances",
        "Révolution de Juillet - Trois Glorieuses - La Liberté guidant le peuple",
        "Le Printemps - Grand magasin",
        "Les Galeries Lafayette <H>aussmann[Osman] - Le boulevard <H>aussmann",
        "Georges-Eugène <H>aussmann[Osman] - transformations de Paris sous le 2d(<t) Em>pire: espaces ver<ts>, mobilier urbain, égou<ts>",
        "Surya Bonaly - patineuse artistique",
    ]
}

open(REPLACE_PATH, 'w', encoding='utf-8').write(dumps(OUT, indent=2))
