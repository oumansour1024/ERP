# 🏫 School Management System (manage_scolaire) - Odoo 20

Ce projet est un module de gestion scolaire personnalisé développé pour **Odoo 20** utilisant **Docker Compose**. Il permet de gérer efficacement les étudiants, les inscriptions et les données académiques.

---

## 🚀 Fonctionnalités Actuelles
* **Gestion des Étudiants :** Enregistrement des informations personnelles (Nom, Date de naissance, Genre, Contact).
* **Numérotation Automatique :** Génération automatique des numéros d'inscription.
* **Sécurité & Accès :** Configuration des règles d'accès (`ir.model.access.csv`) conformes aux exigences d'Odoo 20.

---

## 🛠️ Prérequis
Avant de commencer, assurez-vous d'avoir installé sur votre machine :
* [Docker](https://docker.com)
* [Docker Compose](https://docker.com)

---

## 📦 Structure du Projet
```text
core/
├── docker-compose.yaml      # Configuration des conteneurs Odoo & PostgreSQL
├── .env                     # Variables d'environnement (Mots de passe, Versions)
└── addons/                  # Dossier contenant les modules personnalisés
    └── manage_scolaire/     # Notre module de gestion scolaire
        ├── models/          # Logique métier & Base de données (Python)
        ├── views/           # Interfaces utilisateurs & Menus (XML)
        ├── security/        # Droits d'accès et sécurité (CSV)
        └── __manifest__.py  # Fiche d'identité du module Odoo
```

---

## ⚙️ Installation et Lancement

### 1. Cloner ou configurer l'environnement
Assurez-vous que vos fichiers `docker-compose.yaml` et `.env` sont bien configurés dans le répertoire racine.

### 2. Démarrer les conteneurs Docker
Lancez la commande suivante pour démarrer l'application en arrière-plan :
```bash
docker compose up -d
```

### 3. Vérifier le statut des conteneurs
```bash
docker compose ps
```

---

## 🧩 Activation du Module dans Odoo

Une fois les conteneurs démarrés, suivez ces étapes pour installer le module :

1. Ouvrez votre navigateur et accédez à : `http://localhost:8069`
2. Connectez-vous ou créez une nouvelle base de données.
3. Activez le **Mode Développeur** (*Developer Mode*) :
   * Allez dans **Configuration** (*Settings*).
   * Faites défiler vers le bas et cliquez sur **Activer le mode développeur**.
4. Allez dans le menu **Applications**.
5. Cliquez sur **Mettre à jour la liste des applications** (*Update Apps List*) dans la barre supérieure.
6. Supprimez le filtre `Applications` par défaut dans la barre de recherche.
7. Recherchez `School Management` ou `manage_scolaire`.
8. Cliquez sur **Activer** (*Activate*).

---

## 🔄 Commandes Utiles au Développement

* **Redémarrer uniquement Odoo (après modification du code Python) :**
  ```bash
  docker compose restart odoo
  ```
* **Mettre à jour le module directement depuis le terminal :**
  ```bash
  docker compose exec odoo odoo -u manage_scolaire -d <nom_de_votre_bdd>
  ```
* **Consulter les Logs en temps réel :**
  ```bash
  docker compose logs -f odoo
  ```

---

## 📝 Technologies Utilisées
* **Framework :** Odoo 20.0 (Community Edition)
* **Langages :** Python 3, XML
* **Base de données :** PostgreSQL 16
* **Déploiement :** Docker / Docker Compose
