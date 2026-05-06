# Notion Clone - Déploiement

Application Django clone de Notion avec authentification sociale (GitHub/Google) et éditeur CKEditor.

## Prérequis

- Python 3.11+
- Git
- Compte PythonAnywhere (gratuit)

## Déploiement sur PythonAnywhere

### 1. Préparation locale

1. Créez un compte sur [PythonAnywhere](https://www.pythonanywhere.com/)
2. Copiez le fichier `.env.example` vers `.env` et remplissez les valeurs :
   ```bash
   cp .env.example .env
   ```
3. Modifiez `.env` avec vos vraies valeurs de production

### 2. Upload du projet

Deux méthodes :

**Méthode A : Git clone**
```bash
cd ~
git clone https://github.com/votre-utilisateur/votre-repo.git
cd votre-repo
```

**Méthode B : Upload manuel**
- Téléchargez votre projet en ZIP
- Uploadez via l'interface Web de PythonAnywhere

### 3. Configuration de l'environnement virtuel

```bash
# Créez le virtualenv
python3.11 -m venv ~/venvs/notion_clone

# Activez-le
source ~/venvs/notion_clone/bin/activate

# Installez les dépendances
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configuration de l'application Web

1. Allez dans l'onglet **Web** de PythonAnywhere
2. Cliquez sur **Add a new web app**
3. Choisissez **Django**
4. Sélectionnez la version Python (3.11)
5. Indiquez le chemin vers votre projet : `/home/votreuser/votre-repo`

### 5. Configuration du fichier WSGI

Le fichier WSGI devrait ressembler à ça :
```python
import os
import sys

path = '/home/votreuser/votre-repo'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'notion_clone.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 6. Variables d'environnement

Dans l'onglet **Web** > **Environment variables**, ajoutez :
- `DJANGO_SECRET_KEY` = votre clé secrète (générez-en une nouvelle)
- `DJANGO_DEBUG` = `False`
- `DJANGO_ALLOWED_HOSTS` = `votreuser.pythonanywhere.com`

### 7. Fichiers statiques

1. Dans `settings.py`, vérifiez que `STATIC_ROOT` est défini :
   ```python
   STATIC_ROOT = BASE_DIR / 'staticfiles'
   ```

2. Dans l'onglet **Web** > **Static files**, ajoutez :
   - URL : `/static/`
   - Directory : `/home/votreuser/votre-repo/staticfiles`

3. Collectez les fichiers statiques :
   ```bash
   python manage.py collectstatic
   ```

### 8. Base de données

```bash
# Appliquez les migrations
python manage.py migrate

# Créez un superuser si nécessaire
python manage.py createsuperuser
```

### 9. Configuration des applications sociales (optionnel)

Si vous utilisez GitHub/Google OAuth :

1. Créez des applications sur GitHub et Google
2. Configurez les URLs de callback :
   - GitHub : `https://votreuser.pythonanywhere.com/accounts/github/login/callback/`
   - Google : `https://votreuser.pythonanywhere.com/accounts/google/login/callback/`
3. Ajoutez les clés dans les variables d'environnement :
   - `GITHUB_CLIENT_ID`
   - `GITHUB_CLIENT_SECRET`
   - `GOOGLE_CLIENT_ID`
   - `GOOGLE_CLIENT_SECRET`

### 10. Déploiement final

1. Cliquez sur **Reload** dans l'onglet Web
2. Visitez `https://votreuser.pythonanywhere.com/`

## Commandes utiles

```bash
# Activer le virtualenv
source ~/venvs/notion_clone/bin/activate

# Migrations
python manage.py makemigrations
python manage.py migrate

# Collecter les fichiers statiques
python manage.py collectstatic

# Créer un superuser
python manage.py createsuperuser

# Tester localement
python manage.py runserver
```

## Dépannage

### Erreur 500
- Vérifiez les logs dans l'onglet **Web** > **Error log**
- Assurez-vous que `DEBUG = False` et `ALLOWED_HOSTS` sont corrects

### Fichiers statiques non chargés
- Vérifiez que `collectstatic` a été exécuté
- Vérifiez la configuration des static files dans l'interface Web

### Base de données
- SQLite fonctionne sur PythonAnywhere
- Pour plus de trafic, migrez vers PostgreSQL

## Migration vers un hébergement payant

Si vous dépassez les limites gratuites :
- Render.com
- Railway.app
- DigitalOcean App Platform
- Heroku

Ces plateformes nécessitent généralement PostgreSQL au lieu de SQLite.

## Support

Pour des questions, consultez :
- [Documentation Django](https://docs.djangoproject.com/)
- [Documentation PythonAnywhere](https://help.pythonanywhere.com/)