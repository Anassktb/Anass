# Générateur de Mot de Passe et Passphrase - README

Ce projet Python propose des fonctionnalités pour tester la force d'un mot de passe, générer des mots de passe aléatoires et créer des passphrases basées sur des mots.

# main.py

Le fichier main.py est le point d'entrée du projet. Il permet à l'utilisateur de choisir parmi plusieurs options.
Fonctionnalités de main.py :

    Affiche un menu interactif pour choisir l'action souhaitée.
    Teste la force d'un mot de passe en calculant son entropie.
    Génère un mot de passe aléatoire en respectant les critères spécifiés.
    Génère une passphrase basée sur une liste de mots.
    Affiche les résultats des tests et des générations.

# password.py

Le fichier password.py contient la classe PasswordUtils, une classe utilitaire pour la gestion des mots de passe.
Fonctionnalités de password.py :

    Calcule l'entropie d'un mot de passe en fonction de sa longueur et de l'ensemble de caractères utilisés.
    Évalue la force d'un mot de passe en fonction de son entropie.
    Génère un mot de passe aléatoire en respectant les critères de longueur, de minuscules, de majuscules, de chiffres et de caractères spéciaux.

# passphrase.py

Le fichier passphrase.py contient la classe DicePassphraseGenerator, qui permet de générer des passphrases basées sur une liste de mots.
Fonctionnalités de passphrase.py :

    Génère une passphrase en utilisant une liste de mots (par défaut, une liste de fruits).
    Permet de spécifier le nombre de mots dans la passphrase.
    Retourne la passphrase générée.

* Utilisation

Pour utiliser ce projet :

    Assurez-vous d'avoir Python installé sur votre système.
    Téléchargez les fichiers main.py, password.py, et passphrase.py dans le même répertoire.
    Exécutez main.py avec Python pour commencer à tester et générer des mots de passe.
