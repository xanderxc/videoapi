import time
import json
from flask import Flask
from flask_cors import CORS

from pgqueries.pgquery import PostgresQuery
from pg_config import dbsettings


def get_video_list():
    dbconn = PostgresQuery(dbsettings)
    query = '''select id, file_name as name from videoshare.video''' # where file_name like \'%Part 12%\''''
    res = dbconn.query_return(query)
    for i in res:
        i['name'] = i.get('name')[18:][:-4]
    return res


app = Flask(__name__)
CORS(app)


@app.route('/list')
def get_movie_list():
    movie_list_str = get_video_list()
    return json.dumps({"movielist":movie_list_str})


@app.route('/test-list')
def get_test_movie_list():
    movie_list_str =[{"id": 646, "name": "cartoon/A.Cat.In.Paris.2010"}, {"id": "12399", "name":"cartoon/short/Masters_of_Russian_Animation_1"},{"id": "12345", "name":"cartoon/Pixar.Short.La.Luna.2011"}, {"id": "12346", "name": "cartoon/Pixar.Short.Partly.Cloudy.2009"}, {"id": "1", "name":"cartoon/Pixar.Short.Piper"}]
    return json.dumps({"movielist":movie_list_str})


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


