#!/usr/bin/python

import os
import shutil
import bcrypt
import gdbm
ficheiro = "passwords.dbm"
db=gdbm.open(ficheiro, "c", 0o600)
# contas XXXX- com a mesma password
password = "YYYY"
# e.g. range(36,40)=36,37,38,39
for i in range(1,10):
    username = "XXXX-" + str(i)
    print(username+"\n") 
    db[username] = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
#
db.close()
