#!/usr/bin/env bash

if [[ $# -ne 1 ]]; then
    echo "コンテスト名を指定してください"
    exit 1
fi

mkdir $1

cp python_macros.txt $1/A.py
cp python_macros.txt $1/B.py
cp python_macros.txt $1/C.py
cp python_macros.txt $1/D.py
cp python_macros.txt $1/E.py
cp python_macros.txt $1/F.py

exit 0
