#!/bin/bash
echo nombre del commit:
read name
git add .
git commit -m "$name"
git push -u origin master
