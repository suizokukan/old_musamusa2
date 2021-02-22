ROADMAP
=======

[DONE] v. 0.0.1 : Basic structure: poetry/logging/config file/command line args
[TODO] v. 0.0.2 : level0 (=most basic features of the musamusa text format)
[TODO] v. ?.?.?
  * level1 (=glossary lines)
  * essayer l'installation via pip

PROJECT' VERSIONS
=================

[STILL IN DEVELOPMENT] v. 0.0.2
-------------------------------

[TODO] task-10
    Documentation about the future versions
    
[DONE] v. 0.0.1
---------------

```
[DONE] v. 0.0.1
    Basic structure: poetry/logging/config file/command line args

    task-0, task-1, task-2, task-3, task-4, task-5, task-6, task-7,
    task-8, task-9

    
[DONE] task-0
  - basic file hierarchy
  - documentation

[DONE] task-1
  - doc/musamusatextformatfile.md must be an easy to read .md file.

[DONE] task-2
  - poetry stuff
  - project version: 0.0.1

[DONE] task-3
    - musamusa/aboutproject.py::__version__
    - automatically update pyproject.toml via propagate_versionnumber.py

[DONE] task-4
    - header for .py files
    - improved documentation (README.md, in various .py files)
    - code pylinted

[DONE] task-5
    - musamusa/aboutprojects.py:
    __author__, __projectname__,  __version__, __email__,  __license__,
    __location__
    - doc/code.md : how to write code
    - musamusa/cmdlineargs.py
      command line arguments : --help / -h / --about / --version
    - pimydoc file

[DONE] task-6
    - --checkenv command line option
      musamusa/cmdline_checkenv.py
      musamusa.aboutproject::THIRDPARTIES_DEPENDENCIES
    - improved doc
    - code has been pylinted

[DONE] task-7
    - --logcfgfile argument
    - pimydoc:exit codes are now:
         1 : (success) print version and exit
         2 : (success) print about informations and exit
         3 : (success) print checkenv informations and exit
        -1 : (error) missing main configuration file    
        -2 : (error) missing logging configuration file
    - logging facilities
      logging.ini
      musamusa/global_logger.py
    - --maincfgfile option
    - new files:
      logging.ini
      mainconfig.ini    
      musamusa/global_logger.py
      musamusa/global_maincfgini.py
      musamusa/maincfgfile.py
      musamusa/logging_facilities.py

[DONE] task-8
    - fix the headers of all .py files (i.e. licence and shebang)
    - each error has its number (ERRIDXXX)
    - new files:
      err_codes.sh
      codesearch_in_codedirectory.sh
    - the doc has been improved

[DONE] task-9
    - improved doc in mainconfig.ini
    - no more TODOs
    
```