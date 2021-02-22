#!/usr/bin/env bash

# ---- minimal/maximal indexes searched in ERRID$integer strings ------------
min_index=1
max_index=10


if [ $# -eq 0 ]
then
    # no argument → error message
    echo 'Error : this script needs an argument : --list or a string like "027" .'
    exit 255
fi

# ---- --help ----------------------------------------------------------------
if [[ $1 = "--help" ]] || [[ $1 = "-h" ]]
then
    echo "err_codes.sh : search ERRID strings"
    echo "argument:"
    echo "  * --list  : show all known err codes."
    echo "  * '001' : search 'ERR001' string."
    exit 255
fi

# ==== REAL WORK =============================================================

if [ $1 = "--list" ]
then
    for (( index=$min_index; index<=$max_index; index++ ))
    do
        str_index="ERRID"`printf "%03g" $index`

        echo "→ "$str_index" :"
        ./codesearch_in_codedirectory.sh "$str_index"
    done
    exit 255
fi

str_index="ERRID"`printf "%03g" $1`

./codesearch_in_codedirectory.sh "$str_index"

exit 0
