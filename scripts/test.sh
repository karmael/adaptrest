#!/usr/bin/env bash

if [[ $PWD =~ "scripts" ]]; then
    cd ..
fi

MODULE="${1:-api}"
[[ "$MODULE" != "api" ]] && MODULE="api.tests.${MODULE}"
python manage.py test $MODULE --keepdb
