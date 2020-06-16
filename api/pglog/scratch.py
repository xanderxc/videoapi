from sqlalchemy import create_engine
from sqlalchemy.sql import text



db_url = 'postgresql://postgres:linjie1018@192.168.1.187:5432/postgres'
engine = create_engine(db_url)

with engine.connect() as con:
    statement = text("""select * from test1""")
    rs = con.execute(statement)
    print(rs.rowcount)
        


print("ok")