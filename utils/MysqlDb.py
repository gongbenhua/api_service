# Database driver class
import pymysql
from setting import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB


class MysqlDb():

    def __init__(self, host, port, user, passwd, db):
        """ Establish database connection"""
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            autocommit=True
        )
        # Create a cursor object through cursor () and output the query results in dictionary format
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        """ Triggered when the object resource is released, the last operation when the object is about to be deleted """

        # Close Cursor
        self.cur.close()
        # Close database connection
        self.conn.close()

    def select_one(self, sql):
        """No value query, return a result"""

        # Check whether the connection is disconnected, and reconnect if it is disconnected
        self.conn.ping(reconnect=True)
        # Execute sql using execute()
        self.cur.execute(sql)
        # Use fetchone() to get query results
        data = self.cur.fetchone()

        return data

    def select_one_value(self, sql, value: tuple):
        """Query by passing a value and return a result"""

        self.conn.ping(reconnect=True)
        self.cur.execute(sql, value)
        data = self.cur.fetchone()
        return data

    def select_all(self, sql):
        """Return a dictionary without value query"""

        self.conn.ping(reconnect=True)
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def select_all_value(self, sql, value: tuple):
        """Query by passing a value and return a dictionary"""

        self.conn.ping(reconnect=True)
        self.cur.execute(sql, value)
        data = self.cur.fetchall()
        return data

    def execute(self, sql):
        """Update/add/delete without passing a value, and return the number of affected lines"""
        self.conn.ping(reconnect=True)
        rowcount = self.cur.execute(sql)
        # Commit transaction
        self.conn.commit()

        return rowcount

    def execute_value(self, sql, property: tuple):
        """Update/add/delete with passing a value, and return the number of affected lines"""
        self.conn.ping(reconnect=True)
        rowcount = self.cur.execute(sql, property)
        self.conn.commit()
        return rowcount





db = MysqlDb(MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB)
