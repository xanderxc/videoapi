DROP TABLE IF EXISTS log_table;
CREATE TABLE IF NOT EXISTS log_table(
    id bigserial PRIMARY KEY,
    logger text,
    created_at timestamp,
    log_level text,
    message varchar(20480),
    traceback varchar(255000)
);
