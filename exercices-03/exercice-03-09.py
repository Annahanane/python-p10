# exo 3.9
# Charly fait ses courses.
# Il compare le prix de deux marques différentes de chocolat.
# La marque Alpha propose une tablette à 2,00 euros (pour 120 g).
# La marque Beta propose une tablette à 1,70 euros (pour 100 g).
# Charly a l'intuition que la marque Alpha est plus avantageuse.
# A-t-il raison ?
# Calculez d'abord le poid au kilo (convertir les grammes en kilo donc) et stockez les résultats dans les variables `weight_alpha` et `weight_beta`.
# Puis calculez le prix au kilo avec les variables `price_alpha` et `weight_alpha`, et `price_beta` et `weight_beta` respectivement puis stockez les résultat dans les variables `price_per_kilo_alpha` et `price_per_kilo_beta`.
# Utilisez un opérateur de comparaison (qui doit donc renvoyer une valeur booléenne) pour vérifier si Charly a raison.
# Affichez le résultat booléen.

price_alpha = 2.00
price_beta = 1.70

# réponse 3.9
g_alpha = 120
g_beta = 100

# le poid au kilo
weight_alpha = g_alpha/1000
print(weight_alpha)
weight_beta = g_beta/1000
print(weight_beta) 

# le prix au kilo
price_per_kilo_alpha = price_alpha / weight_alpha
print(price_per_kilo_alpha)
price_per_kilo_beta = price_beta / weight_beta
print(price_per_kilo_beta)

if price_alpha < 17 and price_beta <= 17 :
    print(True)

else  :
    print(False)   



