import pytest

from StructureTests.manipulateur_de_chaines import ManipulateurDeChaines, ExceptionChaineVide


class TestManipulateurDeChaine:
    CHAINE_VIDE = ""
    CHAINE_NON_VIDE = "Bonjour, le Monde !"
    CHAINE_AVEC_ESPACES = "Bonjour, le Monde !"
    CHAINE_SANS_ESPACES = "Bonjour,leMonde!"
    CHAINE_EN_MAJUSCULES = "BONJOUR, LE MONDE !"
    CHAINE_EN_MINUSCULES = "bonjour, le monde !"
    CHAINE_AVEC_CARACTERES_SPECIAUX = "Bonjour,;le Monde!"

    def setup(self):
        self.manipulateur_de_chaines = ManipulateurDeChaines()

    def test_etant_donne_chaine_vide_quand_compter_caracteres_alors_resultat_est_zero(self):
        # Étant donné
        chaine = self.CHAINE_VIDE

        # Quand
        nombre_caracteres = self.manipulateur_de_chaines.compter_caracteres(chaine)

        # Alors
        assert nombre_caracteres == 0

    def test_etant_donne_chaine_non_vide_quand_compter_caracteres_alors_resultat_est_correct(self):
        # Étant donné
        chaine = self.CHAINE_NON_VIDE

        # Quand
        nombre_caracteres = self.manipulateur_de_chaines.compter_caracteres(chaine)

        # Alors
        assert nombre_caracteres == 19

    def test_etant_donne_chaine_avec_espaces_quand_supprimer_espaces_alors_espaces_sont_supprimes(self):
        # Étant donné
        chaine = self.CHAINE_AVEC_ESPACES

        # Quand
        resultat = self.manipulateur_de_chaines.supprimer_espaces(chaine)

        # Alors
        assert resultat == self.CHAINE_SANS_ESPACES

    def test_etant_donne_chaine_sans_espaces_quand_supprimer_espaces_alors_chaine_reste_inchangee(self):
        # Étant donné
        chaine = self.CHAINE_SANS_ESPACES

        # Quand
        resultat = self.manipulateur_de_chaines.supprimer_espaces(chaine)

        # Alors
        assert resultat == self.CHAINE_SANS_ESPACES

    def test_etant_donne_chaine_avec_lettres_majuscules_quand_convertir_en_minuscules_alors_chaine_convertie_en_minuscules(self):
        # Étant donné
        chaine = self.CHAINE_EN_MAJUSCULES

        # Quand
        resultat = self.manipulateur_de_chaines.convertir_en_minuscules(chaine)

        # Alors
        assert resultat == self.CHAINE_EN_MINUSCULES

    def test_etant_donne_chaine_en_minuscules_quand_convertir_en_minuscules_alors_chaine_reste_inchangee(self):
        # Étant donné
        chaine = self.CHAINE_EN_MINUSCULES

        # Quand
        resultat = self.manipulateur_de_chaines.convertir_en_minuscules(chaine)

        # Alors
        assert resultat == self.CHAINE_EN_MINUSCULES

    def test_etant_donne_chaine_vide_quand_compter_nombre_de_mots_alors_exception_est_levee(self):
        # Étant donné
        chaine = self.CHAINE_VIDE

        # Quand + Alors
        with pytest.raises(ExceptionChaineVide):
            self.manipulateur_de_chaines.compter_nombre_de_mots(chaine)

    def test_etant_donne_chaine_non_vide_quand_compter_nombre_de_mots_alors_compte_est_un(self):
        # Étant donné
        chaine = self.CHAINE_NON_VIDE

        # Quand
        nombre_de_mots = self.manipulateur_de_chaines.compter_nombre_de_mots(chaine)

        # Alors
        assert nombre_de_mots == 3

    def test_etant_donne_chaine_avec_mots_separes_par_espaces_quand_compter_nombre_de_mots_alors_compte_est_correct(self):
        # Étant donné
        chaine = self.CHAINE_AVEC_ESPACES

        # Quand
        nombre_de_mots = self.manipulateur_de_chaines.compter_nombre_de_mots(chaine)

        # Alors
        assert nombre_de_mots == 3

    def test_etant_donne_chaine_avec_mots_separes_par_caracteres_speciaux_quand_compter_nombre_de_mots_alors_compte_est_correct(self):
        # Étant donné
        chaine = self.CHAINE_AVEC_CARACTERES_SPECIAUX

        # Quand
        nombre_de_mots = self.manipulateur_de_chaines.compter_nombre_de_mots(chaine)

        # Alors
        assert nombre_de_mots == 3
