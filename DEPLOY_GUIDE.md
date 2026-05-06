# 🚀 Guide de Déploiement PythonAnywhere - Session Actuelle

## ✅ Prérequis vérifiés
- ✅ Code poussé sur GitHub (branche `production`)
- ✅ Branches Git organisées (develop/production)
- ✅ Fichiers de configuration prêts

## 📋 Étapes de déploiement

### 1. Créer un compte PythonAnywhere
- Allez sur https://www.pythonanywhere.com/
- Créez un compte gratuit
- Notez votre **nom d'utilisateur** (ex: `votrenom`)

### 2. Ouvrir la console Bash
- Dans PythonAnywhere, cliquez sur **"Open Bash console here"**

### 3. Cloner votre projet
```bash
cd ~
git clone -b production https://github.com/djama-vianney10/Notion_clone.git
cd Notion_clone
```

### 4. Créer l'environnement virtuel
```bash
python3.11 -m venv ~/venvs/notion_clone
source ~/venvs/notion_clone/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Créer l'application Web
- Allez dans l'onglet **"Web"**
- Cliquez **"Add a new web app"**
- Choisissez **"Django"**
- Sélectionnez **Python 3.11**
- Entrez le chemin : `/home/votrenom/Notion_clone`

### 6. Configurer le fichier WSGI
Dans l'onglet **"Web"** > **"WSGI configuration file"**, remplacez le contenu par :
```python
import os
import sys

path = '/home/votrenom/Notion_clone'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'notion_clone.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 7. Variables d'environnement
Dans l'onglet **"Web"** > **"Environment variables"**, ajoutez :
```
DJANGO_SECRET_KEY=votre-nouvelle-cle-secrete-production
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=votrenom.pythonanywhere.com
```

**Générez une nouvelle clé secrète :**
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(50))"
```

### 8. Fichiers statiques
Dans l'onglet **"Web"** > **"Static files"**, ajoutez :
- **URL** : `/static/`
- **Directory** : `/home/votrenom/Notion_clone/staticfiles`

Puis dans la console :
```bash
cd ~/Notion_clone
python manage.py collectstatic
```

### 9. Base de données
```bash
cd ~/Notion_clone
python manage.py migrate
python manage.py createsuperuser  # Optionnel
```

### 10. Redémarrer l'application
- Dans l'onglet **"Web"**, cliquez **"Reload votrenom.pythonanywhere.com"**

### 11. Tester
- Visitez `https://votrenom.pythonanywhere.com/`
- Testez l'inscription/connexion
- Vérifiez que les pages fonctionnent

## 🔧 Dépannage

### Erreur 500
- Vérifiez les logs : onglet **"Web"** > **"Error log"**
- Variables d'environnement correctes ?
- Permissions sur les fichiers ?

### Fichiers statiques ne chargent pas
- `collectstatic` exécuté ?
- Configuration static files correcte ?

### Base de données
- Migrations appliquées ?
- SQLite est supporté sur PythonAnywhere

## 📞 Support
Si vous avez des erreurs, copiez-collez les messages d'erreur et je vous aiderai à les résoudre.

## 🎯 URL finale
Votre application sera accessible sur : `https://votrenom.pythonanywhere.com/`