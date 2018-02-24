#!/usr/bin/env bash

sqlite3 -header -csv aliexpress_db.sqlite "select * from products;" > products.csv