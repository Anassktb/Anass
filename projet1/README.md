# Quiz à Choix Multiples (QCM) - README

Ce projet Python consiste en un Quiz à Choix Multiples (QCM) qui permet de poser des questions à l'utilisateur et d'évaluer ses réponses. Le projet est composé de trois fichiers principaux :

# Fichiers du Projet

# 1. main.py

Le fichier `main.py` est le point d'entrée du projet. Il orchestre le déroulement du QCM en ajoutant des questions, démarrant le quiz et enfin en affichant le score.

- **Fonctionnalités :**
  - Demande à l'utilisateur de répondre aux questions en entrant `a`, `b`, ou `c`.
  - Évalue les réponses et calcule le score.
  - Affiche le score final et les réponses correctes/incorrectes.

# 2. qcm.py

Le fichier `qcm.py` contient la classe `QCM` qui gère le déroulement du quiz. Il inclut également des fonctions pour mélanger les questions et les options de réponses.

- **Fonctionnalités :**
  - Initialisation d'un quiz en créant une liste de questions et en initialisant le score.
  - Ajout de questions au quiz.
  - Démarrage du quiz en affichant les questions dans un ordre aléatoire.
  - Mélangage des options de réponses.
  - Gestion des réponses de l'utilisateur et mise à jour du score.
  - Affichage du score final et de la correction.

# 3. question.py

Le fichier `question.py` contient la classe `Question` qui représente une question du QCM. Chaque instance de cette classe est une question avec ses options de réponses et une réponse correcte.

- **Fonctionnalités :**
  - Création d'une question avec son texte, ses options de réponses et la réponse correcte.
  - Vérification de la validité des réponses de l'utilisateur.
  - Récupération du texte de la question et de ses options de réponses.


