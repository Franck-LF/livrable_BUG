# Projet : Résolution d'incident

# Projet de Résolution d’Incidents Techniques – Application de Classification d’Images Satellite

Ce projet consiste à diagnostiquer, corriger et améliorer une application existante de classification d’images satellite, tout en mettant en place des bonnes pratiques de **MLOps**, de **monitoring** et de **qualité logicielle**.

---

# Objectifs

* Identifier et corriger les dysfonctionnements de l’application
* Mettre en place des outils de **monitoring** et de **journalisation**
* Ajouter des **tests unitaires** pour détecter automatiquement les erreurs
* Implémenter une **feedback loop** pour améliorer le modèle dans le temps

---

# Contexte

L’application repose sur :

* Une API web développée avec **Flask**
* Un modèle de classification d’images satellite
* 4 classes possibles à prédire par le modèle :

  * Desert
  * Forest
  * Meadow
  * Mountain

---

# 1. Résolution de l'incident

* Reproduire le Bug
* Comprendre le Bug (message d'erreur)
* Correction du bug

---

# 2. Mise en place de sécurité

* Mise en place d'un système de logging
* Mise en place de tests unitaires
* Automatisation des tests via GitHub Action
* Mise en place d'un système d'alerting
* Mise en place d'un système de Monitoring

---

# 3. Feedback Loop (MLOps)

<img src="https://github.com/Franck-LF/livrable_BUG/blob/main/Image/mlops.jpg" alt="Drawing" style="width: 500px;"/>


## Objectif

Amélioreation continue du modèle d'IA grâce aux feedback.

## Fonctionnement

1. Suite à une prédiction, on récupère le feedback utilisateur dans l'interface WEB
2. Enregistrer le feedback en base de données (Donnée + annotation)
3. Séparation des données (entraînement + test)
3. Réentraînement du modèle avec les données augmentées
4. Enregistrement du modèle 

---

## Pipeline MLOps

```id="ux1g0u"
Données → Prédiction → Feedback utilisateur → Enregistrement en base → Réentraînement
```

---

# Installation du projet

## 1. Cloner le projet

```bash id="1d6q0z"
git clone https://github.com/Franck-LF/livrable_BUG
cd <votre_nom_de_dossier>
```

---

## 2. Installer les dépendances

```bash id="5fdv91"
pip install -r requirements.txt
```

---

## Lancer l’application

```bash id="8e8m6g"
python app.py
```

---

# Technologies utilisées

* Python
* Flask
* Traitement d’image (PIL, Numpy)
* Pytest pour les tests
* Logging
* 

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