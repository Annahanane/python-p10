# exo 3.6
# La formule suivante permet de convertir des « miles » en mètres :
#
# miles * 1609.344 = mètres
#
# Bob est en Angleterre.
# On lui dit que la boulangerie la plus proche est à 3 miles.
# Calculez la distance en mètres avec la variable `miles` puis stockez le résultat dans la variable `meters`.
# Affichez un résultat arrondi de la distance en mètres avec la fonction `round()`.
# Convertissez les mètres en kilo mètres puis stockez le résultat dans la variable `km`.
# Affichez un résultat arrondi de la distance en kilo mètre avec la fonction `round()`.

miles = 3

# réponse 3.6
# métres = 4828.032
métres = miles * 1609.344
print(métres)

# arrondi = 4828
arrondi = round(métres)
print(arrondi)

# km = 4.828032
km = métres/1000 
print(km)

# arrondi1 = 5
arrondi1 = round(km)
print(arrondi1)

