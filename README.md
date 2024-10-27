# Projet Web Flask - M1DWM

Mehdi Ghoulam <med@gelk.fr>

## Structure du projet

- `.venv/` Environnement virtuel Python où sont installées les dépendances
- `flaskr/` Dossier contenant le code source de l'application
- `flaskr/inventory.py` **Blueprints** pour la gestion de l'inventaire

### Glossaire

- `Blueprints` : Les blueprints sont des objets qui enregistrent des vues, des modèles et des templates. Ils sont utilisés pour organiser le code de l'application en modules.

## Installation

### Creation de l'environnement virtuel

```bash
python3 -m venv .venv
```

### Activation de l'environnement virtuel

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux

```bash
source .venv/bin/activate
```

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Lancement de l'application

Vous pouvez lancer l'application en mode développement avec la commande suivante :

```bash
flask --app flaskr run --debug
```

### Initialisation de la base de données

```bash
flask --app flaskr init-db
```

Cette commande va executer le script `schema.sql` pour initialiser la base de données.

### Modification du style avec Tailwind CSS

Pour modifier le style de l'application, vous pouvez exécuter le script `tailwindcss` qui va générer un fichier CSS à partir du fichier `tailwind.config.js`.
Le fichier source est `flaskr/static/css/input.css` et le fichier de sortie est `flaskr/static/css/output.css`.

- Vous pouvez utiliser le drapeau `--watch` pour recompiler automatiquement le fichier CSS à chaque modification.

```bash
./tailwindcss -i flaskr/static/css/input.css -o flaskr/static/css/output.css --watch
```
