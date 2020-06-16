import time
import json
from flask import Flask
from flask_cors import CORS

from pgqueries.pgquery import PostgresQuery
from pg_config import dbsettings


def get_video_list():
    dbconn = PostgresQuery(dbsettings)
    query = '''select id, file_name as name from videoshare.video'''
    res = dbconn.query_return(query)
    for i in res:
        i['name'] = i.get('name')[18:]
    return res


app = Flask(__name__)
CORS(app)


@app.route('/list')
def get_movie_list():
    movie_list_str = get_video_list()
    return json.dumps({"movielist":movie_list_str}) 


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


