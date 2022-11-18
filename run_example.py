#!/usr/bin/env python

from app import app, create_tables
import sys
sys.path.insert(0, '../..')

create_tables()
app.run(host='localhost', port=5001)
