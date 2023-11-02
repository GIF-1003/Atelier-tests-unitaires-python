class PanierAchat:
    def __init__(self):
        self.articles = []

    def ajouter_article(self, nom_article, prix):
        self.articles.append({'nom': nom_article, 'prix': prix})

    def appliquer_remise(self, nom_article, pourcentage_remise):
        for article in self.articles:
            if article['nom'] == nom_article:
                article['prix'] = article['prix'] - (article['prix'] * pourcentage_remise / 100)
                break

    def req_cout_total(self):
        total = 0.0
        for article in self.articles:
            total += article['prix']
        return total

    def req_articles(self):
        return self.articles

    def retirer_article(self, nom_article):
        article_trouve = False
        for article in self.articles:
            if article['nom'] == nom_article:
                self.articles.remove(article)
                article_trouve = True
                break

        if not article_trouve:
            raise ValueError("L'article à supprimer n'existe pas dans le panier.")

    def vider_panier(self):
        self.articles = []

    def article_existe(self, nom_article):
        for article in self.articles:
            if article['nom'] == nom_article:
                return True
        return False