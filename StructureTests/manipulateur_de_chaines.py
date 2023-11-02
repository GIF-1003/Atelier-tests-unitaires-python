class ExceptionChaineVide(Exception):
    def __init__(self, message="La chaine est vide"):
        super().__init__(message)

class ManipulateurDeChaines:
    @staticmethod
    def compter_caracteres(s):
        return len(s)

    @staticmethod
    def supprimer_espaces(s):
        return "".join(c for c in s if not c.isspace())

    @staticmethod
    def convertir_en_minuscules(s):
        return s.lower()

    @staticmethod
    def compter_nombre_de_mots(s):
        if not s:
            raise ExceptionChaineVide()

        nombre_de_mots = 0
        a_linterieur_du_mot = False

        for c in s:
            if c.isalnum():
                if not a_linterieur_du_mot:
                    nombre_de_mots += 1
                    a_linterieur_du_mot = True
            else:
                a_linterieur_du_mot = False

        return nombre_de_mots
