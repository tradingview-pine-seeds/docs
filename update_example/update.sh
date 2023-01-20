#!/usr/bin/bash

set -e

python3 update_santiment.py

cd ../seed_crypto_santiment
git add .
git commit -m "Update data"
git push
