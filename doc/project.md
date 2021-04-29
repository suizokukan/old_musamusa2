=============
= le projet =
=============
I] journal de bord
II] les étapes

-------------------------------------------------------------------------------    

I] journal de bord
------------------

2021.02.21
    Je reprends le projet à 0.
    Le but premier est d'avoir une version en ligne capable de convertir un .mus
    en console et en un fichier .html . Le reste est secondaire.
    Dans un premier temps, sortir un version 0.0.1 basée sur du solide : poetry, rich,
    logging.ini correct, documentation du .mus parfaite
    
2021.04.29
    Les progrès sont encourageants: les modules musamusa_fal, musamusa_errors, 
    musamusa_romanumbers, musamusa_etr, musamusa_textref sont fonctionnels.
    Le module musamusa_mustext existe mais n'est pas fonctionnel.
    Pour la suite: 
    (a) musamusa_textref est à terminer pour être pleinement fonctionnel
    (b) le module musamusa_etr doit être mis aux normes musamusa_errors
    (c) le fichier pylintrc commun aux modules musamusa_* doit être
        celui de musamusa_textref qui est intéressant.
        
    Dès que ceci sera fait je pourrai passer au module musamusa_mustext.

II] les étapes
--------------
[stade 0] reprendre la base de code existante en la nettoyant:
  - s'appuyer sur nikw pour le contrôle du logging
  - rich obligatoire
  - définition stricte du format .mus
    comment se fait-il par exemple que les infos contenues dans "(pimydoc)markers in a mustextfile"
    ne soient pas présentes dans la doc décrivant ce format ?
    un fichier à part pour décrire ce(s) format(s) !
  - python3.8 > python3.9 partout
  - poetry
  - [[musamusa;format=default;format version=2]]
  - --checkenv > cmd__checkenv()
    éviter la multiplication des .sh
  - nom des levels : de 0 à F (un seul caractère)
  - utiliser string: str à fond (=moins de doc, erreurs plus facilement détectables)

      
- supprimer ce fichier, remettre à 0 zéro l'historique du projet, dépôt public




*******************************************************************************
# Qu'est-ce qui est commun aux projets musamusa*:

    * pyproject.toml identique
    * gestion des erreurs basée sur musamusa_errors; syntaxe particulière
    * improved_str()

# TODO pour tous les projets musamusa*:

    * README.md: "what's the problem solved by this module ?"
    * # [1] à la place de ## [1]
    * CLI/GPLv3/Python ... avec un lien vers LICENSE
    * vérifier les liens de tous les fichiers README.md
    * 22C5 : donner un exemple, vérifier que c'est le bon car. utilisé dans pimydoc

## TODO/musamusa:

```
[DONE] v. 0.0.1 : Basic structure: poetry/logging/config file/command line args
[TODO] v. 0.0.2 : level0 (=most basic features of the musamusa text format)
[TODO] v. ?.?.?
  * level1 (=glossary lines)
  * essayer l'installation via pip
```

## TODO/musamusa_textref

Il faut définir ref1 <= ref2 <= ref3
