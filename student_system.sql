CREATE DATABASE student_system;
USE student_system;

CREATE TABLE register(
    id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(50),
    lname VARCHAR(50),
    contact VARCHAR(20),
    email VARCHAR(100),
    question VARCHAR(100),
    answer VARCHAR(100),
    password VARCHAR(50)
);
