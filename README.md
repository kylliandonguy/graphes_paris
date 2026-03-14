# 🚌 Planificateur de Trajet - Bus Paris (BUT1)

Ce projet est une application Python développée dans le cadre du module **Graphes** du BUT1. Il permet de calculer et de visualiser l'itinéraire le plus rapide entre deux stations de bus parisiennes.

## 📝 Présentation du projet
L'application utilise la théorie des graphes pour modéliser le réseau de transport :
- **Sommets** : Stations de bus (ex: Bastille, Châtelet, Gare de Lyon).
- **Arêtes** : Liaisons directes entre les stations.
- **Poids** : Temps de parcours en minutes entre deux arrêts.

Le programme s'appuie sur l'**algorithme de Dijkstra** (via NetworkX) pour garantir le chemin le plus court en temps, et non seulement en nombre d'arrêts.

## 🛠️ Installation

### 1. Prérequis
Assurez-vous d'avoir Python installé. Vous pouvez vérifier en tapant `python --version` dans votre terminal.

### 2. Installation des dépendances
Le projet utilise les bibliothèques `networkx` pour les calculs de graphes et `matplotlib` pour l'affichage graphique. Installez-les avec la commande suivante :

`pip install -r requirements.txt`

🚀 Utilisation
Lancez l'application avec la commande :


`python app.py`


📁 Structure des fichiers
app.py : Script principal contenant la logique de calcul et l'affichage.

donnees_bus.py : Base de données du réseau (liaisons, lignes de bus et temps).

requirements.txt : Liste des modules Python nécessaires.


🎓 Notions abordées (BUT1)
Utilisation de la bibliothèque NetworkX.

Manipulation de MultiGraphs (plusieurs lignes sur un même trajet).

Implémentation du plus court chemin (Dijkstra).

Visualisation de données avec Matplotlib.

Projet réalisé pour le module Graphes - IUT

1. **Fichier `requirements.txt`** : Assure-toi qu'il contient bien ces deux lignes :
   ```text
   networkx
   matplotlib
