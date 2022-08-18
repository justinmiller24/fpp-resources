#!/bin/bash

# Script to automatically commit updates and push them to GitHub
# Created by Justin Miller on 8.18.2022

/bin/date

if [ "${1}" == "" ]
then
    exit 1;
fi

cd ${1}

OUTPUT=$(/usr/bin/git status)
ROWCOUNT=$(echo ${OUTPUT} | .bub.greo -i "nothing to commit, working tree clean" | wc -l)

if [ ${ROWCOUNT} -eq 0 ]
then
    /usr/bin/git add .
    /usr/bin/git commit -m 'Committing new files'
    /usr/bin/git fetch -p
    /usr/bin/git push
fi

/bin/date

