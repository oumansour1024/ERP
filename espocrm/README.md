# 🚀 Déploiement d'EspoCRM avec Docker

Ce projet permet de déployer rapidement une instance d'**EspoCRM** adossée à une base de données **MariaDB** en utilisant Docker.

---

## 📋 Architecture & Grille de Configuration

| Composant | Image Docker | Nom du Conteneur | Port Externe | Volume Persistant |
| :--- | :--- | :--- | :--- | :--- |
| **Base de données** | `mariadb:latest` | `espocrm-db` | _Interne au réseau_ | `espocrm-db:/var/lib/mysql` |
| **Application CRM** | `espocrm/espocrm:latest` | `espocrm` | **8080** | `espocrm-data`, `espocrm-custom` |

---

## 🛠️ Variables d'Environnement

Le tableau suivant liste les variables à configurer lors du lancement des conteneurs :

| Conteneur | Variable | Description | Valeur par défaut |
| :--- | :--- | :--- | :--- |
| **espocrm-db** | `MARIADB_DATABASE` | Nom de la base de données | `espocrm` |
| | `MARIADB_USER` | Utilisateur de la base | `espocrm` |
| | `MARIADB_PASSWORD` | Mot de passe de l'utilisateur | `mon_mot_de_passe` |
| | `MARIADB_ROOT_PASSWORD` | Mot de passe Root de MariaDB | `mon_root_password` |
| **espocrm** | `ESPOCRM_DATABASE_HOST` | Hôte de la base de données | `espocrm-db` |
| | `ESPOCRM_SITE_URL` | URL d'accès à l'application | `http://localhost:8080` |

---

## 🚀 Procédure d'Installation (Ligne de commande)

Exécutez les commandes suivantes dans votre terminal pour initialiser l'environnement :

### 1. Création du réseau et des volumes
```bash
docker network create espocrm-network
docker volume create espocrm-db
docker volume create espocrm-data
docker volume create espocrm-custom
docker volume create espocrm-custom-client
```

### 2. Lancement de la Base de Données (MariaDB)
```bash
docker run --name espocrm-db \
  --network espocrm-network \
  --restart unless-stopped \
  -e MARIADB_DATABASE=espocrm \
  -e MARIADB_USER=espocrm \
  -e MARIADB_PASSWORD=mon_mot_de_passe \
  -e MARIADB_ROOT_PASSWORD=mon_root_password \
  -v espocrm-db:/var/lib/mysql \
  -d mariadb
```
*(Note : Si le conteneur existe déjà, utilisez `docker rm espocrm-db` avant de relancer).*

### 3. Lancement d'EspoCRM
```bash
docker run --name espocrm \
  --network espocrm-network \
  -p 8080:80 \
  --restart unless-stopped \
  -e ESPOCRM_DATABASE_HOST=espocrm-db \
  -e ESPOCRM_DATABASE_USER=espocrm \
  -e ESPOCRM_DATABASE_PASSWORD=mon_mot_de_passe \
  -e ESPOCRM_SITE_URL=http://localhost:8080 \
  -v espocrm-data:/var/www/html/data \
  -v espocrm-custom:/var/www/html/custom \
  -v espocrm-custom-client:/var/www/html/client/custom \
  -d espocrm/espocrm
```

---

## 🔗 Accès à l'application

Une fois les conteneurs démarrés, ouvrez votre navigateur et accédez à l'interface :

* **URL :** `http://localhost:8080`
* **Identifiant par défaut :** `admin`
* **Mot de passe par défaut :** `password` *(À modifier obligatoirement dès la première connexion)*
