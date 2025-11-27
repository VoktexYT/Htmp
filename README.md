🐍 HTMP : HTML, CSS et JS avec PythonHTMP est un module Python qui simplifie la création et la gestion de projets web (HTML, CSS et JavaScript) en utilisant une syntaxe Python simple et intuitive.✨ Caractéristiques ClésSyntaxe Simplifiée : Écrivez du code web rapidement avec une syntaxe Python épurée.Structure de Code Claire : Aide à maintenir une bonne structure de projet et à réduire les lignes de code.Gestion des Événements : Intégration facile des événements JS et des pseudo-classes CSS (comme :hover).Raccourcis String : Utilisez des raccourcis pour le formatage HTML de base (gras, lien, etc.).🛠 Installation et ConfigurationInstallation du ModuleLe module HTMP est généralement disponible en téléchargeant les fichiers source.Cliquez sur le bouton "Code" sur la page du projet.Téléchargez et dézippez le module.Placez le dossier du module HTMP dans le répertoire de votre projet.Utilisation BasiquePour commencer à utiliser HTMP dans votre script Python :Pythonimport htmp
# Ou, si vous avez mis les fichiers dans un sous-dossier:
from HTMP import htmp
🚀 Démarrage RapideVoici les étapes de base pour initialiser votre projet et créer vos premiers fichiers.1. Initialiser le ProjetLa classe Web crée la structure de dossiers pour votre projet web.Pythonfrom HTMP import htmp

# Initialisation du projet
project1 = htmp.Web("<chemin_vers_dossier>", "<nom_du_dossier_de_projet>")
# Exemple : project1 = htmp.Web("/home/user/Desktop", "MonPremierWeb")
ParamètreDescription<chemin_vers_dossier>Le chemin où le dossier du projet sera créé.<nom_du_dossier_de_projet>Le nom du répertoire qui contiendra vos fichiers web.2. Créer les FichiersUtilisez la méthode .init() du projet pour créer les fichiers HTML, CSS et JS.Python# Création d'un fichier HTML
page1_html = htmp.Html(project1.init("index.html"))

# Création d'un fichier CSS
style1_css = htmp.Css(project1.init("style.css"))

# Création d'un fichier JS
script1_js = htmp.Js(project1.init("script.js"))
3. Charger le ProjetUne fois tous les fichiers créés et édités, utilisez .load() pour générer le code final dans les fichiers.Python# Listez toutes les variables de pages HTML
all_files = [page1_html.source()]

# Chargez le projet (génère les fichiers)
project1.load(all_files)
Attention : N'oubliez pas d'utiliser .source() à la fin de chaque variable de page HTML.💻 Édition des FichiersÉdition de la Page HTMLAprès avoir créé une instance htmp.Html, vous pouvez éditer son <head> et son <body>.ActionCode PythonDescriptionCharsetpage1_html.Header["charset"]("utf-8")Définit l'encodage de caractères.Titrepage1_html.Header["title"]("Mon Site Web !")Définit le titre de la page.Lien CSSpage1_html.Header["link"]([style1_css])Lie la page CSS (via sa variable).Lien JS (Head)page1_html.Header["script"]([script1_js])Lie le script JS dans le <head>.Lien JS (Body)page1_html.Body["script"]([script1_js])Lie le script JS à la fin du <body>.Titre (h1-h6)page1_html.Body["h"](1, "Mon titre H1")1 est la taille (1 à 6).Paragraphepage1_html.Body["p"]("Ceci est un texte.")Crée un élément <p>.Imagepage1_html.Body["img"]("path/ou/url_image.jpg")Crée un élément <img>.Ajouter ID et ClasseLes arguments id_ et class_ sont des paramètres nommés pour ajouter des attributs.Python# Uniquement un ID
page1_html.Body["p"]('Bonjour', id_='texte-principal')

# Uniquement une Classe
page1_html.Body["p"]('Au revoir', class_='petit-texte')

# ID et Classe
page1_html.Body["p"]('Texte complet', id_='zone-a-style', class_='standard')
Édition de la Page CSSAprès avoir créé une instance htmp.Css, utilisez la méthode Style pour ajouter des règles.Python# Création de la page CSS
style_css = htmp.Css(project1.init("style.css"))

# Règle CSS de base
style_css.Style('selecteur', {
    'propriete_css': 'valeur',
    'color': 'red',
    'font-size': '16px'
})
Ajout d'un Événement (Pseudo-classe)Ajoutez le nom de la pseudo-classe (comme :hover, :focus) comme troisième argument.Pythonstyle_css.Style('selecteur', {
    'color': 'blue',
    'cursor': 'pointer'
}, 'hover')
# Génère : selecteur:hover { color: blue; cursor: pointer; }
Récupérer un SélecteurVous pouvez récupérer l'id ou la class d'un élément HTML créé pour les utiliser directement dans votre CSS.Python# 1. Créez l'élément et stockez sa référence
text_page = page1_html.Body["p"]('Texte stylisé', id_='mon_texte')

# 2. Utilisez la valeur de l'ID pour le sélecteur
style_css.Style(text_page['id'], {
    'background-color': 'yellow'
})

# Alternative : utiliser la string directement
style_css.Style('#mon_texte', {
    'background-color': 'yellow'
})
Édition du Fichier JavaScript (JS)Après avoir créé une instance htmp.Js, utilisez la méthode Event pour définir des fonctions.Python# Création de la page JS
script_js = htmp.Js(project1.init("script.js"))

# Définition d'un événement
script_js.Event(
    'nom_de_l_evenement', # Ex: 'click', 'mouseover'
    'selecteur_cible',     # Ex: '#mon_bouton' ou '.ma_classe'
    [
        'code JS normal 1',
        'code JS normal 2'
    ]
)
Code Réflectif (Toggle)Le code réflectif est exécuté la seconde fois que l'événement est déclenché, permettant un comportement de toggle.Pythonscript_js.Event(
    'click',
    '#mon_element',
    # Code normal (exécuté 1ère, 3ème, 5ème fois...)
    ['alert("Code Normal");'],
    # Code réflectif (exécuté 2ème, 4ème, 6ème fois...)
    ['alert("Code Réflectif");']
)
🔗 Raccourcis de Formatage String (HTML)HTMP propose des raccourcis simples pour formater le texte lors de la création d'éléments HTML.HTMLRaccourciExempleRésultat (HTML)<sup>^^^^texte^^<sup>texte<sub>^^texte^<sub>texte<strong>****texte**texte<em>\\texte\texte<mark>##texte#<mark>texte<u>____texte__<u>texte<strike>----texte--<strike>texte<a> (Lien)::texte:<a>texteRaccourcis pour les LiensPour créer des liens entre les pages HTML générées, utilisez le paramètre url_a= en même temps que le raccourci : dans la chaîne.Python# Lien vers la page2_html
page1_html.Body["p"](":Cliquez ici pour page 2:", url_a=[page2_html])

# Liens multiples (dans l'ordre défini)
page1_html.Body["p"](":one: :two: :three:", url_a=[one_file, tow_file, three_file])
Important : L'ordre des variables dans la liste url_a doit correspondre à l'ordre des raccourcis : dans la chaîne de caractères.🧩 Exemple de Code CompletVoici un exemple d'application du module HTMP.Python# 1. Importation
from HTMP import htmp

# 2. Création du projet
wiki_project = htmp.Web('/home/user/Desktop', 'Wiki_Code')

# 3. Création des fichiers
index_html = htmp.Html(wiki_project.init('index.html'))
style_css = htmp.Css(wiki_project.init('style.css'))
script_js = htmp.Js(wiki_project.init('script.js'))

# 4. Édition HTML
btn = index_html.Body['h'](1, 'click me', id_='btn')
txt = index_html.Body['p']('ceci est un texte')

# 5. Édition CSS de base (Sélecteur ID)
style_css.Style(btn['id'], {
    'color': 'grey',
    'background-color': 'black',
    'transition': '0.3s'
})

# 6. Ajout de pseudo-classe CSS (:hover)
style_css.Style(btn['id'], {
    'color': 'red'
}, 'hover')

# 7. Édition JS (Événement click avec toggle)
script_js.Event(
    'click',
    btn['id'],
    # Code normal (1ère fois)
    [
        script_js.changeHtml(txt['id'], 'ceci est un très bon texte'),
        script_js.changeCss(txt['id'], 'color', 'green')
    ],
    # Code réflectif (2ème fois)
    [
        script_js.changeHtml(txt['id'], 'ceci est un très mauvais texte'),
        script_js.changeCss(txt['id'], 'color', 'red')
    ]
)

# 8. Chargement du projet (génération des fichiers)
wiki_project.load([index_html.source()])
# À Propos
Auteur : VoktexYT
Version Actuelle : 9
Pourquoi utiliser HTMP ?
- Vitesse d'Écriture : Pour coder plus rapidement vos maquettes et projets web.
- Simplicité de Syntaxe : Une API Python simple pour générer du code web complexe.
- Réduction des Erreurs : Pour structurer correctement votre code et éviter les bugs manuels.
- Structure du Code : Aide à maintenir une bonne organisation de votre projet.
- Compacité : Réduit le nombre de lignes de code nécessaires.
