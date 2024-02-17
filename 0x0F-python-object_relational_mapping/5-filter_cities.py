#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def lists_cities():
    """Gives access to db and get the cities from db."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cmdquery = 'SELECT cities.name FROM \
        cities INNER JOIN states ON states.id=cities.state_id \
        WHERE states.name=%s'
    cursor = db.cursor()
    cursor.execute(cmdquery, (state_name,))
    rows = cursor.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    cursor.close()
    db.close()


if __name__ == "__main__":
    lists_cities()
