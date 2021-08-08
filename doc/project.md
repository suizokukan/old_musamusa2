=============
= le projet =
=============
I] journal de bord
II] les étapes
III] les modules

-------------------------------------------------------------------------------

I] journal de bord
------------------
2021.08.09
-atext semble prêt, j'attaque maintenant la suite de MusTextFile.

à faire:
    (1) noter dans code conventions: * all classes have an improved_str() method using rich attributes
    (1') vérifier dans tous les modules utilisant pimydoc que le caractère spécial (0x...) est bien
         celui annoncé.
    (2) vérifier dans tous les README.md que tous les liens fonctionnent; ceci n'est pas vrai pour au moins
        un module.
    (3) Iaswn : Que faire pour les \\\\\ qui apparaissent ?
    (4) Iaswn : README.md
    (5) AnnotatedText(README.md) : pas de mention de JSON
    (6) rich obligatoire pour les modules musamusa-* (donc pas pour Iaswn); modifier en conséquence
        les .improved_str() et les example.py

2021.08.08
J'ai bien améliorer Iaswn et les modules qui en dépendent en utilisent la dernière version. Objectif: bug (1) et (2) avant de poursuivre MusText (qui sera renommé MusTextFile).

à faire:
    (1) bug dans _atext; si on ajoute les chaînes Beo.1.a, Beo.1.b, Beo.2.a et Beo.2.b avec TextRefDefaultClass,
       l'ordre ne sera pas le bon. Si on utilise la classe TextRefOEVerses, l'ordre est bon.
    (2) Si l'on ajoute Beo.2.c à un AnnotedText utilisant TextRefOEVerses le message d'erreur obtenu
       est peu clair parce qu'il faudrait un processus de validation acceptant dans les regex a-z et 
       interdisant ensuite autre chose que a-b.
    (3) noter dans code conventions: * all classes have an improved_str() method using rich attributes
    (3') vérifier dans tous les modules utilisant pimydoc que le caractère spécial (0x...) est bien
         celui annoncé.
    (4) vérifier dans tous les README.md que tous les liens fonctionnent; ceci n'est pas vrai pour au moins
        un module.
    (5) Iaswn : Que faire pour les \\\\\ qui apparaissent ?
    (6) Iaswn : README.md
    (7) AnnotatedText(README.md) : pas de mention de JSON
    (8) rich obligatoire pour les modules musamusa-* (donc pas pour Iaswn); modifier en conséquence
        les .improved_str() et les example.py

2021.08.02
Je viens de réussir pour la première fois à import/exporter un objet AnnotatedText en utilisant la
library Iaswn. Ca marche !

à faire:
    (1) bug dans _atext; si on ajoute les chaînes Beo.1.a, Beo.1.b, Beo.2.a et Beo.2.b avec TextRefDefaultClass,
       l'ordre ne sera pas le bon. Si on utilise la classe TextRefOEVerses, l'ordre est bon.
    (2) Si l'on ajoute Beo.2.c à un AnnotedText utilisant TextRefOEVerses le message d'erreur obtenu
       est peu clair parce qu'il faudrait un processus de validation acceptant dans les regex a-z et 
       interdisant ensuite autre chose que a-b.
    (3) noter dans code conventions: * all classes have an improved_str() method using rich attributes
    (3') vérifier dans tous les modules utilisant pimydoc que le caractère spécial (0x...) est bien
         celui annoncé.
    (4) vérifier dans tous les README.md que tous les liens fonctionnent; ceci n'est pas vrai pour au moins
        un module.
    (5) Iaswn : optimiser .l si la liste est vide.
    (6) Iaswn : ce serait bien de pouvoir encoder n'import quel objet, pas seulement un class object.
    (7) Iaswn : Que faire pour les \\\\\ qui apparaissent ?
    (8) Iaswn : crypter + zipper.
    (9) AnnotatedText(README.md) : pas de mention de JSON

2021.05.02
à faire:
    (1) bug dans _atext; si on ajoute les chaînes Beo.1.a, Beo.1.b, Beo.2.a et Beo.2.b avec TextRefDefaultClass,
       l'ordre ne sera pas le bon. Si on utilise la classe TextRefOEVerses, l'ordre est bon.
    (2) Si l'on ajoute Beo.2.c à un AnnotedText utilisant TextRefOEVerses le message d'erreur obtenu
       est peu clair parce qu'il faudrait un processus de validation acceptant dans les regex a-z et 
       interdisant ensuite autre chose que a-b.
    (3) noter dans code conventions: * all classes have an improved_str() method using rich attributes
    (3') vérifier dans tous les modules utilisant pimydoc que le caractère spécial (0x...) est bien
         celui annoncé.
    (4) vérifier dans tous les README.md que tous les liens fonctionnent; ceci n'est pas vrai pour au moins
        un module.
    (5) préciser dans le TODO de musamusa_atext qu'un objet AnnotatedText doit être json'able (?)

2021.05.01
    Les 6 premiers modules sont prêts; je vais pouvoir passer au module musamusa_mustext.
    (a) noter dans code conventions: * all classes have an improved_str() method using rich attributes
    (b) vérifier dans tous les modules utilisant pimydoc que le caractère spécial (0x...) est bien
        celui annoncé.
    (c) préciser dans le TODO de musamusa_atext qu'un objet AnnotatedText doit être json'able (?)

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
  - --checkenv > cmd__checkenv()
    éviter la multiplication des .sh
  - nom des levels : de 0 à F (un seul caractère)
  - utiliser string: str à fond (=moins de doc, erreurs plus facilement détectables)

      
- supprimer ce fichier, remettre à 0 zéro l'historique du projet, dépôt public


III] les modules

   module name          | version | tests     | code quality | description
   ----------------------------------------------------------------------------------------------------------------
-¹ musamusa_fal         | 0.1.6   |   1 /   1 | 10/10        | FileAndLine storage
-¹ musamusa_errors      | 0.9.5   |   5 /   5 | 10/10        | MusaMusaErrors-like objects
-  musamusa_romannumbers| 0.1.3   |   6 /   6 | 10/10        | 156 <-> CLVI
-¹ musamusa_textref     | 0.2.2   |  37 /  37 | 10/10        | "Beowulf.3a" ⊂ "Beowulf.3"
-  musamusa_etr         | 0.1.2   |  29 /  29 | 10/10        | Easy-To-Read text format file
-¹ musamusa_atext       | 0.1.5   |  70 /  70 | 10/10        | ("DRN.II.1", "{Ab}mari magno{/Ab}") -> AnnotatedText
+  musamusa_mustext     |         |           |              | ": DRN.II.1 {Ab}mari magno{/Ab}" <-> MusText
   =================================================================================================================
   7 modules prévus                 148 / 148 
   
- : if no logging, + if logging
¹ : jsonable through Iaswn library

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
