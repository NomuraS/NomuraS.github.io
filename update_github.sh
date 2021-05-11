#!/bin/sh

find . -name '.DS_Store' -type f -ls -delete
rm -rf build
rm -rf docs
python freeze.py
mv build docs

today=$(date "+%Y%m%d")
echo "update-heroku"
echo "git"
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

