import pytest
from NommageTests.calculateur import Calculateur

class TestCalculateur:

    def setup(self):
        self.calculateur = Calculateur()

    def test_etant_donne_deux_nombres_quand_addition_alors_resultat_est_correct(self):
        # Étant donné
        premierNombre = 5
        deuxiemeNombre = 10

        # Quand
        resultat = self.calculateur.addition(premierNombre, deuxiemeNombre)

        # Alors
        assert resultat == 15

    def test_etant_donne_deux_nombres_quand_soustraction_alors_resultat_est_correct(self):
        # Étant donné
        premierNombre = 10
        deuxiemeNombre = 5

        # Quand
        resultat = self.calculateur.soustraction(premierNombre, deuxiemeNombre)

        # Alors
        assert resultat == 5

    def test_etant_donne_deux_nombres_quand_multiplication_alors_resultat_est_correct(self):
        # Étant donné
        premierFacteur = 5
        deuxiemeFacteur = 10

        # Quand
        resultat = self.calculateur.multiplication(premierFacteur, deuxiemeFacteur)

        # Alors
        assert resultat == 50

    def test_etant_donne_deux_nombres_quand_division_alors_quotient_est_correct(self):
        # Étant donné
        dividende = 10
        diviseur = 2

        # Quand
        resultat = self.calculateur.division(dividende, diviseur)

        # Alors
        assert resultat == 5

    def test_etant_donne_denominateur_egal_a_zero_quand_division_alors_exception_est_levee(self):
        # Étant donné
        dividende = 10
        diviseur = 0

        # Quand + Alors
        with pytest.raises(ValueError):
            self.calculateur.division(dividende, diviseur)
