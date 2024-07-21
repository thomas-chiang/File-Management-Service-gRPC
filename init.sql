CREATE TABLE files (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(255) NOT NULL
);
