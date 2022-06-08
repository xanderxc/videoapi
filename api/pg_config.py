class dbsettings:
    user = "postgres" 
    password = "*****"
    host = "******"
    port = 5432
    database = "postgres"
    pg_url = f'postgresql://{user}:{password}@{host}:{port}/{database}'
