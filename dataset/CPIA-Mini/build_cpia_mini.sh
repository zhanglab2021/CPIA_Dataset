#!/bin/bash
# To run this script: (Note to disable the terminal output)
# nohup bash build_cpia_mini.sh > /dev/null 2>&1 &

set -e

# Create intermediate files
zip -F L.zip --out L_Scale.zip
zip -FF L_Scale.zip --out L.zip -fz
zip -F M.zip --out M_Scale.zip
zip -FF M_Scale.zip --out M.zip -fz

# Remove original & intermediate zip files
rm -f L_Scale.zip
rm -f L.z01
rm -f M_Scale.zip
rm -f M.z01
rm -f M.z02

# Unzip composed zip files
unzip L.zip
unzip M.zip
unzip S.zip

# Remove composed zip files
rm -f L.zip
rm -f M.zip
rm -f S.zip

# Create combined CPIA-mini dataset
mkdir All
cp -r L/* All/
cp -r M/* All/
cp -r S/* All/

set +e
