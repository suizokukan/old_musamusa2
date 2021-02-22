how to write MusaMusa code
--------------------------

* all .py files have the same header
* code documentation is written in the pimydoc file
* to avoid debug-like code, print() is forbidden; if you really have to print a
  string without using rich methods, call sys.stdout.write() .
* if you remove/add a third parties dependency please update musamusa.aboutproject::THIRDPARTIES_DEPENDENCIES
* each error has its number (ERRIDXXX where XXX are three digits); see `err_codes.sh` script