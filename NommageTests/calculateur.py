class Calculateur:
    @staticmethod
    def addition(premierNombre, deuxiemeNombre):
        return premierNombre + deuxiemeNombre

    @staticmethod
    def soustraction(premierNombre, deuxiemeNombre):
        return premierNombre - deuxiemeNombre

    @staticmethod
    def multiplication(premierFacteur, deuxiemeFacteur):
        return premierFacteur * deuxiemeFacteur

    @staticmethod
    def division(dividende, diviseur):
        if diviseur == 0:
            raise ValueError("La division par zéro n'est pas autorisée.")
        return dividende // diviseur
