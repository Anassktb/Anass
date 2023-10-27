from qcm import QCM
from question import Question

if __name__ == "__main__":
    questions = [
        Question("Quelle est la capitale de la France?", ["Marseille", "Lyon", "Paris"], "Paris"),
        Question("Quelle est la capitale du Maroc?", ["Rabat", "Casablanca", "Ahfir"], "Rabat"),
        Question("Quelle est la capitale de  l'Angleterre?", ["Londres", "Manchester", "Liverpool"], "Londre"),
        Question("Quelle est la capitale de l'Italie?", ["Turin", "Rome", "Milan"], "Rome"),
        Question("Quelle est la capitale de l'Algerie?", ["Alger", "Oran", "Blida"], "Alger"),
        Question("Quelle est la capitale de la Tunisie?", ["Tunis", "Hammamet", "Sfax"], "Tunis"),
        Question("Quelle est la capitale de l'Espagne?", ["Barcelone", "Madrid", "Bilbao"], "Madrid"),
        Question("Quelle est la capitale du Portugal?", ["Lisbonne", "Braga", "Porto"], "Lisbonne"),
        Question("Quel est le seul club français a avoir gagné la Ligue des Champions", ["Paris Saint Germain", "Olympique de Marseille", "As Monaco"], "Olympique de Marseille"),
        Question("Quel est le club le plus titré de l'Histoire de la Ligue des Champions", ["Liverpool", "Real de Madrid", "Creil"], "Real de Madrid"),
    ]

    qcm = QCM()
    for question in questions:
        qcm.add_question(question)

    qcm.start_quiz()
    qcm.show_score()
