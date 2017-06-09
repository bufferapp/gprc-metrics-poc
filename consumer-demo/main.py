#!/usr/bin/env python

import os
import json
import logging
import psycopg2
from cerone import process_stream
from google.protobuf import json_format
import collector_pb2

def connect():
    return psycopg2.connect(
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        port=os.environ['DB_PORT'],
        host=os.environ['DB_HOST']
    )

def insert_visit(conn, visit):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO event_data_visits(id,uri,ip)
             VALUES(%s,%s,%s)"""
    cur = conn.cursor()
    cur.execute(sql, (
        visit.id,
        visit.uri,
        visit.ip
    ))
    conn.commit()
    cur.close()


def process_metric_event(data, partition_key=None, sequence_number=None):
    """Write the data to a file."""
    logging.info('Recieved message, partition_key=' + partition_key)

    try:
        conn = connect()

        if partition_key == 'Visit':
            m = collector_pb2.Visit()
            m.ParseFromString(data)
            insert_visit(conn, m)

        logging.info(json_format.MessageToJson(m))
    except Exception as e:
        logging.exception("Failed to decode pb")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    logging.basicConfig(filename='consumer.log',level=logging.DEBUG)
    logging.info('Starting consumer...')
    process_stream(process_metric_event)
