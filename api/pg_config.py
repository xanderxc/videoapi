class dbsettings:
    user = "postgres" 
    password = "linjie1018"
    host = "192.168.1.187"
    port = 5432
    database = "postgres"
    pg_url = f'postgresql://{user}:{password}@{host}:{port}/{database}'
