from pgqueries.pgquery import PostgresQuery
from pg_config import dbsettings

def get_video_list():
    dbconn = PostgresQuery(dbsettings)
    query = '''select id, file_name as name from videoshare.video'''
    res = dbconn.query_return(query)
    for i in res:
        i['name'] = i.get('name')[18:]
    return res

if __name__ == '__main__':
    t1 = get_video_list()

    for i in t1:
        print(i)