from utils import to_db_str

if __name__ == "__main__":
    from_dir = "/mnt/g/ent/movies"
    exts = [".mp4"]
    sql_list = to_db_str(from_dir, exts)
    for i in sql_list:
        print(i)
