create table videoshare.video (
    id SERIAL PRIMARY KEY,
    video_name VARCHAR(255) NOT NULL,
    language VARCHAR(100) default 'english' NOT NULL, 
    year INTEGER,
    category VARCHAR(25) default 'cartoon',
    duration INTEGER,
    file_name VARCHAR(255) NOT NULL UNIQUE,
    created_date timestamp default now(),
    created_by VARCHAR(100) default USER,
    updated_date timestamp default now(),
    updated_by VARCHAR(100) default USER
)
