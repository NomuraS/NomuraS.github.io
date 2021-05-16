#!/bin/sh

find . -name '.DS_Store' -type f -ls -delete
rm -rf build
rm -rf docs
source activate py38
python freeze.py
mv build docs

echo "--------------------- update github----------------------"
today=$(date "+%Y%m%d")
git add .
git commit -m "update_${today}"
# git remote add origin git@github.com:NomuraS/NomuraS.github.io.git
git push -u origin main



# git init
# git add .
# git commit -m "modified for pages"
# git branch -M main
# git remote add origin git@github.com:NomuraS/NomuraS.github.io.git
# git push -u origin main

