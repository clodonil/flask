#!/bin/bash


rm -rf db_repository
rm -rf db/banco_de_dados.db


./db_create.py
./db_migrate.py

./populando.py
