class Question:
    def __init__(self, question, options, correct_answer):
        # Le constructeur de la classe Question est appelé lors de la création d'une nouvelle instance de la classe.
        # Il prend trois paramètres : question, options et correct_answer, pour initialiser les attributs de l'objet.
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.user_answer = None

    def is_correct(self):
        # La méthode is_correct est utilisée pour vérifier si la réponse de l'utilisateur (user_answer) est correcte.
        # Elle retourne True si user_answer est défini et égal à correct_answer (en ignorant la casse), sinon False.
        return self.user_answer and self.user_answer.lower() == self.correct_answer

    def get_question(self):
        # La méthode get_question est utilisée pour obtenir le texte de la question.
        return self.question

    def get_options(self):
        # La méthode get_options est utilisée pour obtenir la liste des options de réponse.
        return self.options
