import random

class DicePassphraseGenerator:
    @staticmethod
    def generate_passphrase(number_of_words=6, word_list=None):
        """
        Génère une passphrase en utilisant une liste de mots (par défaut, une liste de fruits).
        
        :param number_of_words: Le nombre de mots dans la passphrase.
        :param word_list: La liste de mots parmi lesquels choisir (par défaut, une liste de fruits).
        :return: La passphrase générée.
        """
        if not word_list:
            word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig",
                         "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange",
                         "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]

        if number_of_words <= 0:
            return ""
        
        # Sélectionne de manière aléatoire un nombre spécifié de mots de la liste pour former une passphrase.
        passphrase = ' '.join(random.choice(word_list) for _ in range(number_of_words))
        return passphrase