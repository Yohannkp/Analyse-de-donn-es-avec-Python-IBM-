
# Résumé du Projet : Analyse et Modélisation des Prix des Ordinateurs Portables

## Introduction
Ce projet vise à analyser un ensemble de données sur les ordinateurs portables et à construire des modèles de régression pour prédire leurs prix. Les étapes suivantes ont été réalisées pour atteindre cet objectif.

---

## Étapes du Projet

### 1. Chargement des Données
- Les données ont été téléchargées depuis une URL et sauvegardées dans un fichier CSV local.
- Les colonnes inutiles `Unnamed: 0` et `Unnamed: 0.1` ont été supprimées.

### 2. Préparation des Données
- Les données ont été divisées en deux ensembles :
    - `x_data` : Contient les attributs explicatifs.
    - `y_data` : Contient la variable cible, `Price`.
- Les données ont été divisées en ensembles d'entraînement et de test :
    - 10% des données pour le test.
    - 90% des données pour l'entraînement.

### 3. Régression Linéaire Simple
- Un modèle de régression linéaire a été construit en utilisant l'attribut `CPU_frequency`.
- Les scores R² ont été calculés pour les ensembles d'entraînement et de test.

### 4. Validation Croisée
- Une validation croisée à 4 plis a été effectuée pour évaluer la performance du modèle.
- La moyenne et l'écart-type des scores R² ont été calculés.

### 5. Régression Polynomiale
- Les données ont été transformées en utilisant des caractéristiques polynomiales de degré 1 à 5.
- Les scores R² ont été calculés pour chaque degré afin d'identifier le point de surapprentissage.

### 6. Régression Ridge
- Une régression Ridge a été réalisée en utilisant plusieurs caractéristiques (`CPU_frequency`, `RAM_GB`, `Storage_GB_SSD`, etc.) avec des caractéristiques polynomiales de degré 2.
- Les valeurs de l'hyperparamètre `alpha` ont été explorées dans l'intervalle [0.001, 1] avec un pas de 0.001.
- Les scores R² pour les ensembles d'entraînement et de test ont été tracés en fonction de `alpha`.

### 7. Recherche par Grille (Grid Search)
- Une recherche par grille a été effectuée pour identifier la meilleure valeur de `alpha` parmi `{0.0001, 0.001, 0.01, 0.1, 1, 10}`.
- La meilleure valeur de `alpha` a été utilisée pour évaluer le modèle sur l'ensemble de test.

---

## Résultats Clés
- **Validation Croisée** : La moyenne des scores R² est de `Rcross.mean()` avec un écart-type de `Rcross.std()`.
- **Régression Polynomiale** : Le score R² diminue après un certain degré, indiquant un surapprentissage.
- **Régression Ridge** : La meilleure valeur de `alpha` trouvée est `0.1`, avec un score R² de `BestRR.score()` sur l'ensemble de test.

---

## Visualisations
- **R² vs Degré de Polynomiale** : Une courbe a été tracée pour observer le surapprentissage.
- **R² vs Alpha (Ridge)** : Une courbe a été tracée pour comparer les performances sur les ensembles d'entraînement et de test.

---

## Conclusion
Ce projet a permis de construire et d'évaluer plusieurs modèles de régression pour prédire les prix des ordinateurs portables. La régression Ridge avec une recherche par grille a donné les meilleurs résultats, en équilibrant la complexité du modèle et la performance.
