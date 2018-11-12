import sqlite3
from sqlite3 import Error
import os
import sys
import json


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


def select_all_owners(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM db_app_owner")
    lsts = cur.fetchall()
    lsts = list(lsts)
    labels = ['pk', 'name', 'cell', 'email', 'id_one', 'id_two', 'unit_id']
    dd = []
    i = 0
    for lst in lsts:
        d = dict(zip(labels, lst))
        dd.append(d)
        i += 1
    return json.dumps(dd)


def list_owners(database):
    conn = create_connection(database)
    with conn:
        lmin = select_all_owners(conn)
    return lmin


def select_owner_by_id(db, id):
    conn = create_connection(db)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM db_app_owner WHERE unit_id=%s" %id)
        o = cur.fetchall()
    return json.dumps(o[0])


def main():
    # BDIR = settings.BASE_DIR
    # database = os.path.join(BDIR, 'db.sqlite3')
    database = r"C:\Users\Vusi.Sibande\code\desktop\mica\backend\mica_data\db.sqlite3"
    command = sys.stdin.readline()
    command = command.split('\n')[0]
    if command == 'get_all_owners':
        lmin = list_owners(database)
        sys.stdout.write(lmin + "\n")
    if ":" in command:
        print('we here')
        command, id = command.split(":")
        print(id)
        if command == 'get_owner_by_id':
            id_owner = select_owner_by_id(database, id)
            # print(id_owner)
            sys.stdout.write(id_owner + "\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()

