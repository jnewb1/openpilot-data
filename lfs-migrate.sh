#!/bin/sh

# Migrate segments to LFS

BASEDIR=$(dirname "$0")

for segment in $BASEDIR/segments/*.bz2; do
  git lfs track $segment
done

git add .
git commit -m "Migrate segments to LFS"
git lfs migrate import --fixup