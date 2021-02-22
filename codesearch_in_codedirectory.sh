#!/usr/bin/env bash

if [ $# -eq 0 ]
then
    # no argument → error message
    echo 'Error : this script needs an argument like "my string" .'
    exit 255
fi

# ---- --help ----------------------------------------------------------------
if [[ $1 = "--help" ]] || [[ $1 = "-h" ]]
then
    echo "code_search_in_codedirectory.sh : search a string only in the code directory ."
    echo "one argument required : the string to be searched."
    exit 255
fi

# ==== REAL WORK =============================================================

find musamusa/ -name "*.py" -exec grep -rHn --color "$1" {} \;

exit 0
