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