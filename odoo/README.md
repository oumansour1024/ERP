# 🚀 Déploiement d'Odoo ERP avec Docker

Ce projet permet de déployer rapidement une instance d'**Odoo ERP** (version 18.0) adossée à une base de données **PostgreSQL** en utilisant Docker Compose.

---

## 📋 Architecture & Grille de Configuration

| Composant | Image Docker | Nom du Conteneur | Port Externe | Volume Persistant |
| :--- | :--- | :--- | :--- | :--- |
| **Base de données** | `postgres:15` | `odoo-db` | _Interne au réseau_ | `odoo-db-data:/var/lib/postgresql/data` |
| **Application ERP** | `odoo:18.0` | `odoo` | **8069** | `odoo-web-data:/var/lib/odoo` |

---

## 🛠️ Variables d'Environnement

Le tableau suivant liste les variables configurées pour l'interconnexion des conteneurs :

| Conteneur | Variable | Description | Valeur par défaut |
| :--- | :--- | :--- | :--- |
| **odoo-db** | `POSTGRES_DB` | Base de données par défaut | `postgres` |
| | `POSTGRES_USER` | Utilisateur PostgreSQL | `odoo` |
| | `POSTGRES_PASSWORD` | Mot de passe de la base | `mon_mot_de_passe_db` |
| **odoo** | `HOST` | Liaison vers le conteneur DB | `odoo-db` |
| | `USER` | Identifiant de connexion DB | `odoo` |
| | `PASSWORD` | Mot de passe de connexion DB | `mon_mot_de_passe_db` |

---

## 🚀 Procédure de Lancement

Suivez ces étapes simples pour démarrer votre environnement :

### 1. Démarrer les conteneurs
Exécutez cette commande dans votre terminal à l'emplacement du fichier `docker-compose.yml` :
```bash
docker compose up -d
```

### 2. Arrêter l'environnement
Pour stopper temporairement les services sans supprimer vos données :
```bash
docker compose stop
```

### 3. Réinitialiser l'environnement
Pour arrêter et supprimer les conteneurs (vos données restent protégées dans les volumes) :
```bash
docker compose down
```

## Module `school_management`

Le module personnalisé se trouve dans `addons/school_management` et est monté
automatiquement dans le conteneur Odoo sous `/mnt/extra-addons`. Il fournit la
gestion des étudiants et des filières avec des vues liste, formulaire, kanban
et recherche compatibles avec Odoo 18.

Après le premier démarrage, créez une base depuis l'interface Odoo, puis
installez le module directement depuis le conteneur :

```bash
docker compose exec odoo odoo -d <nom_de_la_base> -i school_management --stop-after-init
docker compose restart odoo
```

Pour appliquer des modifications ultérieures au module :

```bash
docker compose exec odoo odoo -d <nom_de_la_base> -u school_management --stop-after-init
docker compose restart odoo
```

Vous pouvez aussi activer le mode développeur dans Odoo, ouvrir
**Applications**, actualiser la liste des applications et installer
**School Management**.

---

## 🔗 Premier Accès & Configuration

Une fois l'initialisation terminée, ouvrez votre navigateur web :

* **URL :** `http://localhost:8069`
* **Étape initiale :** Odoo affichera un écran de configuration pour créer votre première base de données.
* **Important :** Notez précieusement le **Master Password** généré automatiquement par Odoo, il vous sera demandé pour toute gestion future de vos bases de données.
