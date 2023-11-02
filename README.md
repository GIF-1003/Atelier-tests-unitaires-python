# Solution de l'atelier de tests unitaires en python

Voici la solution de l'atelier de tests unitaires en python en anglais.

## Description des classes

### Calculator
La classe Calculator fournit des méthodes pour effectuer des opérations mathématiques simples.

- add(a, b): Cette méthode prend deux nombres en entrée et retourne leur somme.
- subtract(a, b): Cette méthode prend deux nombres en entrée et retourne leur différence.
- multiply(a, b): Cette méthode prend deux nombres en entrée et retourne leur produit.
- divide(a, b): Cette méthode prend deux nombres en entrée et retourne leur quotient. 
Si la division par zéro est tentée, une exception ValueError est levée avec le message "Division by zero is not allowed."

### StringManipulator
La classe StringManipulator fournit des méthodes pour manipuler les chaînes de caractères.

- count_characters(s): Cette méthode prend une chaîne de caractères en entrée et retourne le nombre de caractères dans la chaîne.
- remove_spaces(s): Cette méthode prend une chaîne de caractères en entrée et supprime tous les espaces de la chaîne.
- convert_to_lowercase(s): Cette méthode prend une chaîne de caractères en entrée et retourne une nouvelle chaîne en minuscules.
- count_number_of_words(s): Cette méthode prend une chaîne de caractères en entrée et retourne le nombre de mots dans la chaîne.

### ShoppingCart
La classe ShoppingCart représente un panier d'achat avec des articles.

- add_item(item_name, price): Cette méthode permet d'ajouter un article au panier avec son nom et son prix.
- apply_discount(item_name, discount_percentage): Cette méthode applique une réduction en pourcentage sur le prix d'un article spécifié dans le panier.
- get_total_cost(): Cette méthode retourne le coût total de tous les articles dans le panier.
- get_items(): Cette méthode retourne la liste de tous les articles dans le panier.
- remove_item(item_name): Cette méthode permet de supprimer un article spécifique du panier.
- clear_cart(): Cette méthode permet de vider le panier, en supprimant tous les articles.
- item_exists(item_name): Cette méthode vérifie si un article spécifié existe dans le panier. Elle retourne True si l'article existe et False sinon.
