# Analyse des Données - Laptop Pricing Dataset

## Description du Projet
Ce projet consiste en une analyse exploratoire et un nettoyage des données d'un dataset contenant des informations sur les prix des ordinateurs portables. L'objectif est de préparer les données pour une analyse approfondie ou une modélisation.

---

## Étapes Réalisées

### 1. Téléchargement des Données
- Les données ont été récupérées depuis une URL et sauvegardées localement dans un fichier CSV nommé `laptop_pricing_dataset.csv`.

### 2. Chargement des Données
- Les données ont été chargées dans un DataFrame Pandas pour analyse.

### 3. Préparation des Données
- **Arrondi** : Les valeurs de la colonne `Screen_Size_cm` ont été arrondies à 2 décimales.
- **Valeurs Manquantes** :
  - Les colonnes `Weight_kg` et `Screen_Size_cm` contenaient des valeurs manquantes.
  - Ces valeurs ont été remplacées par la moyenne de chaque colonne.
- **Conversion des Types** : Les colonnes numériques ont été converties en type `float`.

### 4. Transformation des Données
- **Standardisation** : Les colonnes numériques `Screen_Size_cm` et `Weight_kg` ont été standardisées à l'aide de `StandardScaler`.
- **Normalisation** : Les mêmes colonnes ont ensuite été normalisées à l'aide de `MinMaxScaler`.

### 5. Catégorisation des Prix
- La colonne `Price` a été divisée en trois catégories (`Low`, `Medium`, `High`) à l'aide de la méthode `pd.cut`.
- Une visualisation sous forme d'histogramme a été créée pour afficher la répartition des catégories.

### 6. Création de Variables Indicatrices
- La colonne catégorique `Screen` a été transformée en variables indicatrices (`Screen-IPS_panel`, `Screen-Full_HD`).
- La colonne originale `Screen` a été supprimée après la transformation.

---

## Résultats
- Les données sont nettoyées, standardisées et prêtes pour une analyse ou une modélisation.
- Les valeurs manquantes ont été traitées.
- Les colonnes catégoriques ont été transformées en variables indicatrices.
- Une catégorisation des prix a été réalisée pour simplifier l'analyse.

---

## Technologies Utilisées
- **Python** : Langage principal.
- **Pandas** : Manipulation et nettoyage des données.
- **NumPy** : Calculs numériques.
- **Matplotlib** : Visualisation des données.
- **Scikit-learn** : Standardisation et normalisation des données.

---