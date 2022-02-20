#!/usr/bin/env python3
"""
Test psycopg with CockroachDB.
"""


from argparse import ArgumentParser, RawTextHelpFormatter
from distutils.log import debug
from traceback import print_list

import psycopg2
from psycopg2.errors import SerializationFailure

import listings
import users

from flask import Flask, request, jsonify
app = Flask(__name__)

conn = psycopg2.connect("postgresql://studentid:3Rqq_brfto3oV1BfPxpzqQ@free-tier4.aws-us-west-2.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Ddeft-molerat-2424")

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)


@app.route('/', methods=['GET'])
def query_records():
    id = request.args.get('id')
    print(id)
    with conn.cursor() as cur:
        cur.execute("SELECT id, firstname, lastname FROM users WHERE id == ")
        rows = cur.fetchall()
        conn.commit()
        for row in rows:
            print(row)


    listings.create_listing(conn)
    listings.create_listing(conn)
    res = listings.print_listing(conn)
    users.create_user(conn)
    users.print_user(conn)
    listings.delete_listing(conn)
    users.delete_user(conn)
    return tuple(res)


if __name__ == '__main__':
    app.run(debug=True)
# Close communication with the database.
    conn.close()

