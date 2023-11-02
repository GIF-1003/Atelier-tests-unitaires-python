# Atelier de tests unitaires python

Ce projet est une référence en python sur l'atelier de tests unitaires en C++.
L'objectif principal de celui-ci est de donner aux étudiants une solution de l'atelier dans un autre language de programmation.
Il peut aussi servir de référence dans le futur pour l'élaboration de tests unitaires en python.
Ce projet est une introduction aux bonnes pratiques des tests unitaires que l'on retrouve dans l'industrie.

## Exercice
Complétez les trois tests unitaires manquants dans la classe test_panier_achat.py.

## Description des classes

### Calculateur
La classe Calculateur fournit des méthodes pour effectuer des opérations mathématiques simples.

- addition(a, b): Cette méthode prend deux nombres en entrée et retourne leur somme.
- soustraction(a, b): Cette méthode prend deux nombres en entrée et retourne leur différence.
- multiplication(a, b): Cette méthode prend deux nombres en entrée et retourne leur produit.
- division(a, b): Cette méthode prend deux nombres en entrée et retourne leur quotient. 
Si la division par zéro est tentée, une exception ValueError est levée avec le message "Division by zero is not allowed."

### Manipulateur de chaines
La classe ManipulateurDeChaines fournit des méthodes pour manipuler les chaînes de caractères.

- compter_caracteres(s): Cette méthode prend une chaîne de caractères en entrée et retourne le nombre de caractères dans la chaîne.
- supprimer_espaces(s): Cette méthode prend une chaîne de caractères en entrée et supprime tous les espaces de la chaîne.
- convertir_en_minuscules(s): Cette méthode prend une chaîne de caractères en entrée et retourne une nouvelle chaîne en minuscules.
- compter_nombre_de_mots(s): Cette méthode prend une chaîne de caractères en entrée et retourne le nombre de mots dans la chaîne.

### Panier d'achat
La classe PanierAchat représente un panier d'achat avec des articles.

- ajouter_article(nom_article, prix): Cette méthode permet d'ajouter un article au panier avec son nom et son prix.
- appliquer_remise(nom_article, pourcentage_remise): Cette méthode applique une réduction en pourcentage sur le prix d'un article spécifié dans le panier.
- req_cout_total(): Cette méthode retourne le coût total de tous les articles dans le panier.
- req_articles(): Cette méthode retourne la liste de tous les articles dans le panier.
- retirer_article(nom_article): Cette méthode permet de supprimer un article spécifique du panier.
- vider_panier(): Cette méthode permet de vider le panier, en supprimant tous les articles.
- article_existe(nom_article): Cette méthode vérifie si un article spécifié existe dans le panier. Elle retourne True si l'article existe et False sinon.
