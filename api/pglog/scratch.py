from sqlalchemy import create_engine
from sqlalchemy.sql import text



db_url = 'postgresql://postgres:******@*********/postgres'
engine = create_engine(db_url)

with engine.connect() as con:
    statement = text("""select * from test1""")
    rs = con.execute(statement)
    print(rs.rowcount)
        


print("ok")
