# Analyse de Données - Automobile Dataset

## Description du Projet
Ce projet consiste en une analyse exploratoire et un nettoyage des données du dataset automobile disponible sur [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data). L'objectif est de préparer les données pour une analyse approfondie ou une modélisation.

---

## Étapes Réalisées

### 1. Chargement des Données
- Les données ont été importées depuis l'URL fournie.
- Les données brutes ont été sauvegardées dans un fichier CSV nommé `usedcars.csv`.

### 2. Préparation des Données
- Ajout des noms de colonnes pour une meilleure lisibilité.
- Remplacement des valeurs manquantes (`?`) par `NaN`.
- Calcul des moyennes pour les colonnes numériques contenant des valeurs manquantes (`normalized-losses`, `bore`, `stroke`, `horsepower`, `peak-rpm`) et remplacement des valeurs manquantes par ces moyennes.
- Remplacement des valeurs manquantes dans la colonne `num-of-doors` par la valeur la plus fréquente.
- Suppression des lignes contenant des valeurs manquantes dans la colonne `price`.
- Conversion des types de données pour les colonnes numériques.

### 3. Transformation des Données
- Conversion des colonnes `city-mpg` et `highway-mpg` en L/100km.
- Normalisation des colonnes `length`, `width`, et `height` en divisant par leurs valeurs maximales.
- Création de catégories pour la colonne `horsepower` en utilisant des intervalles (binned data).

### 4. Création de Variables Dummy
- Création de variables indicatrices (dummy variables) pour les colonnes catégoriques `fuel-type` et `aspiration`.
- Fusion des variables indicatrices avec le DataFrame principal et suppression des colonnes originales.

### 5. Sauvegarde des Données Nettoyées
- Les données nettoyées et transformées ont été sauvegardées dans un fichier CSV nommé `clean_df.csv`.

---

## Résultats
- Les données sont prêtes pour une analyse plus approfondie ou une modélisation.
- Les valeurs manquantes ont été traitées.
- Les colonnes catégoriques ont été converties en variables indicatrices.
- Les données numériques ont été normalisées et transformées pour faciliter l'analyse.

---

## Technologies Utilisées
- **Python** : Langage principal.
- **Pandas** : Manipulation et nettoyage des données.
- **NumPy** : Calculs numériques.
- **Matplotlib** : Visualisation des données.

---