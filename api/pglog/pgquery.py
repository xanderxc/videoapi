import psycopg2
from psycopg2 import Error


class PostgresQuery:
    def __init__(self, db_settings):
        self._settings = db_settings

    def run(self, query):
        try:
            connection = psycopg2.connect(user=self._settings.user,
                                          password=self._settings.password,
                                          host=self._settings.host,
                                          port=self._settings.port,
                                          database=self._settings.database)

            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while running PostgreSQL query", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.close()
