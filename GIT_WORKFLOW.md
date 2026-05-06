# Workflow Git - Développement et Production

## Branches

- `master` : Branche principale (synchronisée avec GitHub)
- `develop` : Développement actif (nouvelles fonctionnalités, corrections)
- `production` : Code prêt pour le déploiement

## Workflow typique

### Développement d'une nouvelle fonctionnalité

```bash
# Travailler sur develop
git checkout develop
git pull origin develop  # Si vous travaillez en équipe

# Créer une branche feature (optionnel)
git checkout -b feature/nouvelle-fonctionnalite

# Commiter vos changements
git add .
git commit -m "Add: nouvelle fonctionnalité"

# Merger vers develop
git checkout develop
git merge feature/nouvelle-fonctionnalite

# Pousser vers GitHub
git push origin develop
```

### Déploiement en production

```bash
# Quand le code est prêt pour production
git checkout production
git merge develop

# Tester et ajuster les settings pour production
# Modifier .env si nécessaire pour production

# Commiter les changements de production
git add .
git commit -m "Deploy: version X.X.X"

# Pousser vers GitHub
git push origin production
```

### Synchronisation avec master

```bash
# Pousser les changements importants vers master
git checkout master
git merge develop
git push origin master
```

## Variables d'environnement par branche

### develop (.env)
```env
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

### production (.env.production)
```env
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=votreuser.pythonanywhere.com
DJANGO_SECRET_KEY=votre-cle-production
```

## Commandes utiles

```bash
# Voir les branches
git branch -a

# Voir l'état
git status

# Voir l'historique
git log --oneline --graph --all

# Comparer les branches
git diff develop production

# Annuler un commit (si nécessaire)
git reset --soft HEAD~1
```

## Bonnes pratiques

1. **Ne jamais commiter** :
   - Clés API secrètes
   - Mots de passe
   - Fichiers locaux (.env avec vraies valeurs)

2. **Toujours tester** avant de merger vers production

3. **Utiliser des messages de commit clairs** :
   - `Add: nouvelle fonctionnalité`
   - `Fix: correction bug login`
   - `Refactor: optimisation code`

4. **Faire des commits atomiques** : un commit = une fonctionnalité/logique

## Déploiement automatique (optionnel)

Vous pouvez configurer PythonAnywhere pour qu'il se mette à jour automatiquement depuis la branche `production`.