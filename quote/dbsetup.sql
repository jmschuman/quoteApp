\set user :v1
\set password :v2

DROP DATABASE IF EXISTS quote_db;

/*DROP ROLE IF EXISTS :user; not sure if we want to do this, because it causes an error due to privileges */
CREATE ROLE :user WITH LOGIN PASSWORD :'password';
ALTER ROLE :user CREATEDB;
CREATE DATABASE quote_db;
GRANT ALL PRIVILEGES ON DATABASE quote_db TO :user;
