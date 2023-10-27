import random  # Importe le module random pour mélanger les questions
from question import Question  # Importe la classe Question depuis le module question


class QCM:
    def __init__(self):        
        # Le constructeur de la classe QCM initialise deux attributs : questions et score.
        # questions est une liste vide pour stocker les questions du QCM.
        # score est initialisé à 0.
        self.questions = []
        self.score = 0

    def add_question(self, question):
         # Méthode pour ajouter une question à la liste de questions du QCM.
        self.questions.append(question)

    def start_quiz(self):
        # Méthode pour démarrer le quiz.
        # Les questions sont mélangées pour être affichées dans un ordre aléatoire.
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions, 1):
            random.shuffle(question.options) # Mélange les options de réponse de chaque question.
            print(f"Question {i}: {question.get_question()}\n") # Affiche le texte de la question.
            options = question.get_options() # Obtient la liste des options de réponse.
            for j, option in enumerate(options, 1):
                print(f"{chr(96 + j)}) {option}") # Affiche les options de réponse avec des lettres (a, b, c)
            while True:
                user_answer = input("Réponse (a/b/c) : ").lower()  # Demande à l'utilisateur de répondre.

                if user_answer in ["a", "b", "c"]:
                    user_option_index = ord(user_answer) - ord("a")   # Convertit la réponse en index.
                    question.user_answer = options[user_option_index]  # Stocke la réponse de l'utilisateur dans l'objet Question.
                    if question.user_answer == question.correct_answer:
                        self.score += 1  # Incrémente le score si la réponse est correcte.
                    break
                else:
                    print("Veuillez répondre avec 'a', 'b' ou 'c'.")  # Message d'erreur si la réponse n'est pas valide.

    def show_score(self):
         # Méthode pour afficher le score final et la correction.
        print("\nScore final 😊")
        print(f"Vous avez obtenu {self.score} sur {len(self.questions)} questions.\n") # Affiche le score
        print("Correction 😊")
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question.get_question()}")
            if question.user_answer:
                user_answer = question.user_answer.lower()
                correct_answer = question.correct_answer.lower()
                if user_answer == correct_answer:
                    print(f"Votre réponse : {question.user_answer} (Correcte)")
                else:
                    print(f"Votre réponse : {question.user_answer} (Incorrecte)")  # Affiche la réponse de l'utilisateur (incorrecte).
                print(f"Réponse correcte : {question.correct_answer}\n")  # Affiche la réponse correcte.
