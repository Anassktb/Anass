import random
import string
import math

class PasswordUtils:  # Classe utilitaire pour la gestion des mots de passe.

    @staticmethod
    def calculate_entropy(password):
        """
        Calcule l'entropie d'un mot de passe.
        
        :param password: Le mot de passe dont l'entropie doit être calculée.
        :return: La valeur d'entropie calculée.
        """
        total_characters = len(password)
        if total_characters == 0:
            return 0

        character_set = string.printable
        base = len(character_set)
        entropy = math.log(base, 2) * total_characters
        return entropy

    @staticmethod
    def evaluate_password_strength(password):
        """
        Évalue la force d'un mot de passe en fonction de son entropie.
        
        :param password: Le mot de passe à évaluer.
        :return: Une indication de la force du mot de passe (Fort, Moyen, Faible).
        """
        entropy = PasswordUtils.calculate_entropy(password)
        if entropy >= 80:
            return "Fort"
        elif entropy >= 60:
            return "Moyen"
        else:
            return "Faible"

    @staticmethod
    def generate_random_password(length, num_lowercase, num_uppercase, num_digits, num_special):
        """
        Génère un mot de passe aléatoire en fonction des critères donnés.
        
        :param length: La longueur du mot de passe à générer.
        :param num_lowercase: Le nombre de caractères minuscules à inclure.
        :param num_uppercase: Le nombre de caractères majuscules à inclure.
        :param num_digits: Le nombre de chiffres à inclure.
        :param num_special: Le nombre de caractères spéciaux à inclure.
        :return: Le mot de passe généré.
        """
        characters = string.ascii_lowercase * num_lowercase + \
                    string.ascii_uppercase * num_uppercase + \
                    string.digits * num_digits + \
                    string.punctuation * num_special

        if len(characters) < length:
            raise ValueError("Pas assez de caractères pour générer le mot de passe.")
        
        password = ''.join(random.sample(characters, length))
        return password