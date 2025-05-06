# Analyse de Données - Automobile Dataset

## Description du Projet
Ce projet consiste en une analyse exploratoire des données (AED) sur le dataset automobile disponible sur [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data). L'objectif est de préparer les données pour une éventuelle modélisation en machine learning.

---

## Étapes Réalisées

### 1. Chargement des Données
- Les données ont été importées depuis l'URL fournie.
- Les données brutes ont été sauvegardées dans un fichier CSV nommé `auto.csv`.

### 2. Préparation des Données
- Ajout des noms de colonnes pour une meilleure lisibilité.
- Remplacement des valeurs manquantes (`?`) par `NaN`.
- Suppression des lignes contenant des valeurs manquantes dans la colonne `price`.
- Sauvegarde du DataFrame nettoyé dans un fichier CSV nommé `automobile.csv`.

### 3. Analyse Exploratoire des Données (AED)
#### a. Compréhension des Données
- Affichage des premières lignes du DataFrame (`head()`).
- Vérification des types de données (`dtypes`) et des informations générales (`info()`).

#### b. Résumé Statistique
- Calcul des statistiques descriptives pour toutes les colonnes (`describe(include='all')`).

#### c. Détection des Valeurs Aberrantes
- Identification des outliers dans les colonnes numériques à l'aide de la méthode IQR.
- Visualisation des outliers avec des boxplots.

#### d. Visualisation des Données
- Utilisation de bibliothèques comme `matplotlib` pour explorer les tendances et relations.

---

## Résultats
- Les données sont prêtes pour une analyse plus approfondie ou une modélisation.
- Les valeurs aberrantes ont été identifiées et visualisées.
- Les données manquantes ont été traitées.

---

## Fichiers Générés
- **auto.csv** : Données brutes téléchargées.
- **automobile.csv** : Données nettoyées et prêtes pour l'analyse.

---

## Technologies Utilisées
- **Python** : Langage principal.
- **Pandas** : Manipulation et nettoyage des données.
- **Matplotlib** : Visualisation des données.

---

## Instructions pour Reproduire
1. Cloner ce dépôt.
2. Installer les dépendances nécessaires :
   ```bash
   pip install pandas matplotlib