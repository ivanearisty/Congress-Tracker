-- Create the database
CREATE DATABASE congresstrackerdb;

-- Use the database
USE congresstrackerdb;

-- Create the 'users' table
CREATE TABLE users (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    bills JSON
);

-- Create the 'bills' table
CREATE TABLE bills (
    congress INT,
    latestAction TEXT,
    number INT,
    originChamber VARCHAR(50),
    originChamberCode VARCHAR(10),
    title VARCHAR(255),
    type VARCHAR(50),
    updateDate DATE,
    updateDateIncludingText DATETIME,
    url VARCHAR(255)
);
