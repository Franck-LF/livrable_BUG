# Projet : Résolution d'incident

# 🛠️ Projet de Résolution d’Incidents Techniques – Application de Classification d’Images Satellite

Ce projet consiste à diagnostiquer, corriger et améliorer une application existante de classification d’images satellite, tout en mettant en place des bonnes pratiques de **MLOps**, de **monitoring** et de **qualité logicielle**.

---

# 🎯 Objectifs

* 🔍 Identifier et corriger les dysfonctionnements de l’application
* ✅ Garantir un fonctionnement stable et opérationnel
* 📊 Mettre en place des outils de **monitoring** et de **journalisation**
* 🧪 Ajouter des **tests unitaires** pour détecter automatiquement les erreurs
* 🔁 Implémenter une **feedback loop** pour améliorer le modèle dans le temps

---

# 🧠 Contexte

L’application repose sur :

* Une API web développée avec **Flask**
* Un modèle de classification d’images satellite
* 4 classes :

  * 🌵 Desert
  * 🌲 Forest
  * 🌿 Meadow
  * ⛰️ Mountain

---

# 🚨 1. Résolution des incidents

## 🔎 Diagnostic

Analyse des problèmes existants :

* Erreurs d’exécution
* Problèmes de chargement du modèle
* Mauvaise gestion des entrées utilisateur
* Bugs liés au traitement des images

---

## 🛠️ Corrections apportées

* Correction des erreurs de code
* Amélioration de la gestion des exceptions
* Validation des entrées utilisateur
* Stabilisation du pipeline de prédiction

---

## 📄 Documentation des incidents

Chaque incident est documenté avec :

* Description du problème
* Cause racine
* Solution appliquée
* Impact

---

# 📊 2. Monitoring & Journalisation

## 📈 Monitoring

Mise en place d’indicateurs pour surveiller :

* Temps de réponse de l’API
* Taux d’erreur
* Volume de requêtes

---

## 📝 Logging

Ajout d’un système de logs pour :

* Suivre les requêtes utilisateurs
* Identifier les erreurs
* Tracer les prédictions du modèle

Exemples :

* Logs d’erreurs
* Logs d’inférence
* Logs système

---

# 🧪 3. Tests unitaires

## 🎯 Objectif

Automatiser la détection des anomalies.

## 🔧 Implémentation

* Tests des endpoints Flask
* Tests du pipeline de prédiction
* Tests de validation des entrées

## ✅ Bénéfices

* Réduction des régressions
* Détection rapide des bugs
* Amélioration de la fiabilité

---

# 🔁 4. Feedback Loop (MLOps)

## 🎯 Objectif

Améliorer continuellement le modèle grâce aux données réelles.

## 🔄 Fonctionnement

1. Collecte des prédictions
2. Identification des erreurs ou cas limites
3. Ajout de nouvelles données annotées
4. Réentraînement du modèle
5. Redéploiement

---

## 📦 Pipeline MLOps

```id="ux1g0u"
Données → Modèle → Prédictions → Feedback → Réentraînement → Déploiement
```

---

# 🌐 5. Application Flask

## Fonctionnalités

* Upload d’images satellite
* Prédiction de la classe
* Affichage du résultat

---

# 🏗️ Architecture

```id="64v67z"
Utilisateur → Flask API → Modèle ML → Prédiction → Logs & Monitoring
```

---

# 🛠️ Installation

## 1. Cloner le projet

```bash id="1d6q0z"
git clone <repo_url>
cd <repo_name>
```

---

## 2. Installer les dépendances

```bash id="5fdv91"
pip install -r requirements.txt
```

---

## ▶️ Lancer l’application

```bash id="8e8m6g"
python app.py
```

---

# 📦 Technologies utilisées

* Python
* Flask
* Bibliothèques de traitement d’image (PIL, OpenCV…)
* Framework de tests (pytest ou unittest)
* Logging (logging module)

---

# 🚀 Améliorations possibles

* Intégration avec un outil de monitoring (Prometheus, Grafana)
* Déploiement avec Docker
* CI/CD pour automatiser les tests et le déploiement
* Détection de drift du modèle

---

# 📌 Résultats

* Application stabilisée
* Meilleure observabilité
* Détection proactive des incidents
* Amélioration continue du modèle

---

# 👨‍💻 Auteur

Projet réalisé dans le cadre d’un travail sur la fiabilité des systèmes ML et les bonnes pratiques MLOps.

---



# Consignes du formateur :

Vous disposez d’une application Flask de classification d’images satellite (4 classes : desert, forest, meadow, mountain).

Un problème s'est glissé dans le code, à vous de le débusquer, trouvez l’anomalie, expliquez clairement la cause, proposez et appliquez un correctif minimal.

Documentez bien la résolution et expliquez ce qui n'allait pas, proposez des tests automatisés lors du déploiement CI/CD (comme on a vu avec github actions) pour que le problème détecté, et d'autres éventuels, ne mettent pas à mal l'application flask

Mettez en place une politique de journalisation et un alerting, quelques ressources :

- https://medium.com/@briankworld/logging-in-flask-introduction-and-practical-example-d2eeac0078b0
- https://last9.io/blog/flask-logging/
- https://betterstack.com/community/guides/logging/how-to-start-logging-with-flask/
- https://flask-fr.readthedocs.io/logging/
- https://flask.palletsprojects.com/en/stable/logging/


Proposez la possibilité de monitorer l'application grâce à flask_monitoring-dashboard :
- https://flask-monitoringdashboard.readthedocs.io/en/latest/


Mettez en place une feedback loop : récupérez le feedback de l'utilisateur (sur la page de résultat des boutons sont inactifs, l'utilisateur peut alors classifier lui-même l'image soumise) et réflechissez à comment l'intégrer à l'application. Schématisez via un diagramme fléché, proposez une modélisation d'une base de données recueillant les feedbacks, dans notre cas de figure, il faut récupérer trois éléments : l'image soumise, la prédiction faite par le modèle et le feedback de l'utilisateur (la classe choisie par l'utilisateur).

Expliquez comment un réentraînement peut être mis en place pour améliorer le modèle, justifiez en fournissant des sources.

Critères de réussite (checklist) :

- [ ] Le bug est identifié, expliqué et corrigé.
- [ ] Les tests attrapent l’ancien bug et passent en vert après correctif.
- [ ] La feedback loop enregistre correctement image + prédiction + label utilisateur.
- [ ] La CI GitHub Actions s’exécute à chaque PR et empêche l’intégration si un test échoue.