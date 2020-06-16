import time
import logging
import traceback
# import psycopg2
from .pgquery import PostgresQuery
from .pg_config import dbsettings


class PostgresHandler(logging.Handler):
    # see TYPE log_level
    _levels = ('debug', 'info', 'warning', 'error', 'critical')

    def __init__(self, db_settings):
        logging.Handler.__init__(self)
        self._db_settings = db_settings

    def emit(self, record):
        level = record.levelname.lower()
        if level not in self._levels:
            level = "debug"

        if record.exc_info:
            traceback_text = logging._defaultFormatter.formatException(record.exc_info)
        else:
            traceback_text = ""
        traceback_text = traceback_text.replace('\'', '\'\'')

        message = record.getMessage()
        message = message.replace('\'', '\'\'')
        logger = record.name
        function = record.funcName
        filename = record.pathname
        line_no = record.lineno
        traceback = traceback_text
        # print(args)
        # print(record.created)
        # insert to database
        dbconn = PostgresQuery(dbsettings)
        #print(query)
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))
        query = f"insert into log_table (created_at, log_level, message, traceback, logger) values ('{tm}', '{level}', '{message}', '{traceback}', '{logger}')"
        #print(query)
        dbconn.run(query)

