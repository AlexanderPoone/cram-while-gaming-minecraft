'''
Copyleft Alexander Poone 2024.

Learn languages by checking out Minecraft villager names. Requires `Villager Names` mod installed.

File replaced on Windows:    %USERPROFILE%/curseforge/minecraft/Instances/1.20.6/config/collective
'''

from json import dumps
from os.path import expanduser

VERSION_TO_BE_CHANGED = '1.20.6'
REPLACE_PATH = expanduser(f"~/curseforge/minecraft/Instances/{VERSION_TO_BE_CHANGED}/config/collective/entity_names.json")

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
"Le guépard",
"Le léopard",
"La luciole",
"Le moustique",
"La girafe",
"La puce",
"Le phoque",
"Le lion de mer",
"L'épaulard",
"L'anguille électrique",
"Le zèbre",
"Le raton laveur",
"Le mendiant",
"L'escroc",
"Le flemmard",
"Le paresseux",
"Le casse-cou"
"Le clochard",
"Le radin",
"Le séduisant",
"Le décontracté",
"L'insaisissable",
"Le misanthrope",
"Le bourgeois gentilhomme",
"Le retardataire",
"L'expéditeur",
"Le destinataire",
"Le bénéficiare",
"Le chef de clan",
"Le glouton",
"Le gourmand",
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
"André Malraux - La Condition Humaine",
"Alain Delon - Le Samouraï",
"Jules Verne - Voyage au centre de la Terre",
"Francis Poulenc - Concert champêtre",
"Henri Matisse - Papier découpé",
"Ingres - La Grande Odalisque",
"Nicolas Poussin - L'Enlèvement des Sabines",
"Caravage - La nature morte",
"Léonard de Vinci - L'Homme de Vitruve",
"Thierry Hermès - La marque de luxe française qui porte son nom",
  ]
}

open(REPLACE_PATH, 'w', encoding='utf-8').write(dumps(OUT, indent=2))