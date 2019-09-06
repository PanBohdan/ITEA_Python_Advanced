import mysql.connector


class ConnectionHandler:
    def __init__(self, **cfg):
        self._config = cfg

    def __enter__(self):
        self.cnx = mysql.connector.connect(**self._config)
        return self.cnx

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.cnx.rollback()
        else:
            self.cnx.commit()
        self.cnx.close()


class CursorHandler:
    def __init__(self, our_connection):
        self.our_connection = our_connection

    def __enter__(self):
        self.our_cursor = self.our_connection.cursor(buffered=True)
        return self.our_cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.our_cursor.close()
