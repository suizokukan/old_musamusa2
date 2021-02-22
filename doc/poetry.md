PyPi
====
https://pypi.org/manage/projects/

!!! shebang obligatoire dans main.py

Poetry
======

Poetry: installation
--------------------
    `$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -`

Poetry: version
---------------
    `$ ~/.poetry/bin/poetry --version`
    
Poetry: Initialising a pre-existing project
-------------------------------------------
    `$ ~/.poetry/bin/poetry init` in the project directory
    
Poetry: add an dependency
-------------------------
    either `$ ~/.poetry/bin/poetry add hashlib`
    either in the `tool.poetry.dependencies section` of the `pyproject.toml` file.
    
Poetry: Installing dependencies
-------------------------------
To install the defined dependencies for your project, just run the install command.
    `$ ~/.poetry/bin/poetry install`
    
Poetry: publish
---------------
(1) `$ ~/.poetry/bin/poetry build`
This command will package your library in two different formats: 
sdist which is the source format, and wheel which is a compiled package.

(2) `$ ~/.poetry/bin/poetry publish`
This will package and publish the library to PyPI, 
at the condition that you are a registered user and 
you have configured your credentials properly.

Once this is done, your library will be available to anyone.

Poetry: run the project
-------------------------------
`poetry musamusa/main.py`
