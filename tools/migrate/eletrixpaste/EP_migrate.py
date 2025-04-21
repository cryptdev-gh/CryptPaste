# ====================================================================

#        CryptPaste
# The open-source Pastebin alternative
# Under the GPL v3 license

# ====================================================================

#Migrating from EletrixPaste to CryptPaste

'''
DB schema:

            CREATE TABLE IF NOT EXISTS pastes (
                id TEXT PRIMARY KEY,
                text TEXT,
                ip_address TEXT
            )
'''

print("Migrating from EletrixPaste to CryptPaste")
print("Make sure to run this script from the root of CryptPaste")
print("MAKE SURE YOU HAVE RUN THE MAIN FILE BEFORE MIGRATING !!!")
print("Press ENTER to continue")
input()
original = input("Enter your EletrixPaste DB Path: ")
import sys
sys.path.append("././")

import db
import sqlite3
import uuid

conn = sqlite3.connect(original)
c = conn.cursor()

c.execute("SELECT * FROM pastes")
rows = c.fetchall()
temp_session = db.get_session()
for row in rows:
    
    print("Migrating paste with ID:" + row[0])
    x = db.Paste(pid=uuid.uuid4().hex, content=row[1], is_password_protected=0, data=row[2])
    temp_session.add(x)
    temp_session.commit()
    
print("Migrating done.")

c.close()
conn.close()



