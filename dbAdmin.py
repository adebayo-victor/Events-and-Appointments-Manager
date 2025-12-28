# seed_all_cs50.py
# Delete and repopulate ALL tables in your DB (CS50-style)
# Requires: pip install cs50

from cs50 import SQL

DB_URL = "sqlite:///clinic.db"  # Change if needed
db = SQL(DB_URL)

print(db.execute("select  * FROM team_members"))