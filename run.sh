#!/usr/bin/env bash


echo "Initializing database ..."
rm master.db
echo "Creating database schema ..."
python3 schema.py
echo "Seeding msft database table ..."
python3 seed.py
echo "Done! Database table seeded with 8,133 rows."
