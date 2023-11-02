import pytest

from FIRST.panier_achat import PanierAchat

class TestPanierAchat:
    PRIX_ARTICLE = 100.0
    PRIX_ARTICLE_2 = 50.0
    PRIX_ARTICLE_3 = 75.0
    POURCENTAGE_REMISE = 20.0
    PRIX_REMISE_ATTENDU = PRIX_ARTICLE - (PRIX_ARTICLE * POURCENTAGE_REMISE / 100)
    COUT_TOTAL_ATTENDU_ZERO = 0.0
    COUT_TOTAL_ATTENDU = PRIX_ARTICLE + PRIX_ARTICLE_2 + PRIX_ARTICLE_3

    NOM_ARTICLE = "Article X"
    NOM_ARTICLE_2 = "Article Y"
    NOM_ARTICLE_3 = "Article Z"

    def setup_method(self):
        self.panier = PanierAchat()

    def test_etant_donne_articles_quand_ajouter_article_alors_articles_sont_ajoutes_au_panier(self):
        # Action
        self.panier.ajouter_article(self.NOM_ARTICLE, self.PRIX_ARTICLE)
        self.panier.ajouter_article(self.NOM_ARTICLE_2, self.PRIX_ARTICLE)

        # Validation
        nombre_attendu = 2
        assert len(self.panier.req_articles()) == nombre_attendu

    def test_etant_donne_panier_avec_article_quand_appliquer_remise_alors_remise_est_appliquee(self):
        # Étant donné
        self.panier.ajouter_article(self.NOM_ARTICLE, self.PRIX_ARTICLE)

        # Action
        self.panier.appliquer_remise(self.NOM_ARTICLE, self.POURCENTAGE_REMISE)

        # Validation
        articles = self.panier.req_articles()
        article_remise = next(article for article in articles if article['nom'] == self.NOM_ARTICLE)
        assert article_remise['prix'] == pytest.approx(self.PRIX_REMISE_ATTENDU)

    def test_etant_donne_panier_vide_quand_req_cout_total_alors_cout_total_est_zero(self):
        # Action
        cout_total = self.panier.req_cout_total()

        # Validation
        assert cout_total == self.COUT_TOTAL_ATTENDU_ZERO

    def test_etant_donne_panier_avec_articles_quand_req_cout_total_alors_cout_total_est_somme_du_prix_des_articles(self):
        # Étant donné
        self.panier.ajouter_article(self.NOM_ARTICLE, self.PRIX_ARTICLE)
        self.panier.ajouter_article(self.NOM_ARTICLE_2, self.PRIX_ARTICLE_2)
        self.panier.ajouter_article(self.NOM_ARTICLE_3, self.PRIX_ARTICLE_3)

        # Action
        cout_total = self.panier.req_cout_total()

        # Validation
        assert cout_total == pytest.approx(self.COUT_TOTAL_ATTENDU)

    def test_etant_donne_panier_avec_article_quand_retirer_article_alors_article_est_retire(self):
        # Étant donné
        self.panier.ajouter_article(self.NOM_ARTICLE, self.PRIX_ARTICLE)

        # Action
        self.panier.retirer_article(self.NOM_ARTICLE)

        # Validation
        articles = self.panier.req_articles()
        assert len(articles) == 0

    def test_etant_donne_panier_vide_quand_retirer_article_alors_exception_est_levee(self):
        # Action + Validation
        with pytest.raises(ValueError):
            self.panier.retirer_article(self.NOM_ARTICLE)

    def test_etant_donne_panier_vide_quand_vider_panier_alors_panier_est_vide(self):
        # Étant donné
        self.panier.ajouter_article(self.NOM_ARTICLE, self.PRIX_ARTICLE)
        self.panier.ajouter_article(self.NOM_ARTICLE_3, self.PRIX_ARTICLE_2)
        self.panier.ajouter_article(self.NOM_ARTICLE_3, self.PRIX_ARTICLE_3)

        # Action
        self.panier.vider_panier()

        # Validation
        articles = self.panier.req_articles()
        assert len(articles) == 0

    def test_etant_donne_panier_avec_article_existants_quand_article_existe_alors_retourne_vrai(self):
        # Étant donné
        self.panier.ajouter_article(self.NOM_ARTICLE, self.PRIX_ARTICLE)

        # Action
        article_existe = self.panier.article_existe(self.NOM_ARTICLE)

        # Validation
        assert article_existe is True

    def test_etant_donne_panier_vide_quand_article_existe_alors_retourne_faux(self):
        # Action
        article_existe = self.panier.article_existe(self.NOM_ARTICLE)

        # Validation
        assert article_existe is False
