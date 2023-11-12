-- Prepares the server for the project
-- create database if not exists

DROP DATABASE IF EXISTS msimu_dev_db;
CREATE DATABASE IF NOT EXISTS msimu_dev_db;

-- create new user for the project
CREATE USER IF NOT EXISTS 'msimu_dev'@'localhost' IDENTIFIED BY 'msimu_dev_pwd';
GRANT ALL PRIVILEGES ON msimu_dev_db.* TO 'msimu_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'msimu_dev'@'localhost';

USE msimu_dev_db;

-- create tables

CREATE TABLE locations (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(128) NOT NULL UNIQUE,
    latitude VARCHAR(128) NOT NULL,
    longitude VARCHAR(128) NOT NULL,
    created_at DATETIME,
    updated_at DATETIME
);

CREATE TABLE users (
    id VARCHAR(60) PRIMARY KEY,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    username VARCHAR(128) NOT NULL,
    email VARCHAR(128),
    password VARCHAR(128) NOT NULL,
    phonenumber VARCHAR(128) NOT NULL,
    location_id VARCHAR(60),
    image VARCHAR(128) NOT NULL,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (location_id) REFERENCES locations(id)
);

CREATE TABLE posts (
    id VARCHAR(60) PRIMARY KEY,
    user_id VARCHAR(60) NOT NULL,
    post_text TEXT NOT NULL,
    comment_image VARCHAR(128),
    likes INT NOT NULL DEFAULT 0,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE comments (
    id VARCHAR(60) PRIMARY KEY,
    user_id VARCHAR(60) NOT NULL,
    post_id VARCHAR(60) NOT NULL,
    comment_text TEXT NOT NULL,
    comment_image VARCHAR(128),
    likes INT NOT NULL DEFAULT 0,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (post_id) REFERENCES posts(id)
);

CREATE TABLE services (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(128) NOT NULL UNIQUE,
    description TEXT NOT NULL,
    created_at DATETIME,
    updated_at DATETIME
);

CREATE TABLE location_services (
    id VARCHAR(60) PRIMARY KEY,
    service_id VARCHAR(60) NOT NULL,
    location_id VARCHAR(60) NOT NULL,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (service_id) REFERENCES services(id),
    FOREIGN KEY (location_id) REFERENCES locations(id)
);

CREATE TABLE predictions (
    id VARCHAR(60) PRIMARY KEY,
    location_id VARCHAR(60) NOT NULL,
    value FLOAT,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (location_id) REFERENCES locations(id)
);

CREATE TABLE weather_data (
    id VARCHAR(60) PRIMARY KEY,
    location_id VARCHAR(60) NOT NULL,
    rainfall FLOAT,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (location_id) REFERENCES locations(id)
);


-- insert data
INSERT INTO locations (id, name, latitude, longitude, created_at, updated_at)
VALUES 
('8dc6a7b0-eb49-4a38-8a0d-d81b5c2e7437', 'New York', '40.7128', '-74.0060', '2023-11-12 09:00:00', '2023-11-12 09:00:00'),
('8917492f-0103-42c3-9d64-1694a99bfb39', 'London', '51.5074', '-0.1278', '2023-11-11 15:30:00', '2023-11-11 15:30:00'),
('24db1ef5-2a5c-4c22-b45d-b051786da64e', 'Tokyo', '35.6895', '139.6917', '2023-11-10 12:45:00', '2023-11-10 12:45:00'),
('2d1ccdb0-fcdb-4d03-a3cc-048a48ff115d', 'Paris', '48.8566', '2.3522', '2023-11-09 08:20:00', '2023-11-09 08:20:00'),
('b87a8d17-0b1b-4b65-a114-5c930b7ff39a', 'Sydney', '-33.8688', '151.2093', '2023-11-08 11:10:00', '2023-11-08 11:10:00');

INSERT INTO users (id, first_name, last_name, username, email, password, phonenumber, location_id, image, created_at, updated_at)
VALUES 
('74b078d4-66cc-463e-bdbb-01c005a4e1bc', 'John', 'Doe', 'john_doe', 'john@example.com', 'password123', '+1234567890', '8dc6a7b0-eb49-4a38-8a0d-d81b5c2e7437', 'user_img.jpg', '2023-11-12 10:00:00', '2023-11-12 10:00:00'),
('9463b28a-0de9-453e-b65a-264e7a58f11e', 'Jane', 'Smith', 'jane_smith', 'jane@example.com', 'secretword', '+1987654321', '8917492f-0103-42c3-9d64-1694a99bfb39', 'user2_img.jpg', '2023-11-11 16:30:00', '2023-11-11 16:30:00'),
('9f3b9a56-15b6-498d-ba7b-d5d8e4c20cc7', 'Emma', 'Johnson', 'emma_j', 'emma@example.com', 'mypass321', '+1555666777', '24db1ef5-2a5c-4c22-b45d-b051786da64e', 'user3_img.jpg', '2023-11-10 13:45:00', '2023-11-10 13:45:00'),
('7e81a754-64a3-4a4a-93ff-28c0b2691925', 'Michael', 'Williams', 'mike_w', 'michael@example.com', 'hellothere', '+1444333222', '2d1ccdb0-fcdb-4d03-a3cc-048a48ff115d', 'user4_img.jpg', '2023-11-09 09:20:00', '2023-11-09 09:20:00'),
('5fe3c402-9b4f-42a3-9811-0c3b0b44a0db', 'Olivia', 'Brown', 'olivia_b', 'olivia@example.com', 'test1234', '+1666777888', 'b87a8d17-0b1b-4b65-a114-5c930b7ff39a', 'user5_img.jpg', '2023-11-08 12:10:00', '2023-11-08 12:10:00');

INSERT INTO posts (id, user_id, post_text, comment_image, likes, created_at, updated_at)
VALUES 
('6495b25e-5b29-4b5b-8f88-cc11b3007c54', '74b078d4-66cc-463e-bdbb-01c005a4e1bc', 'Hello world!', 'post_image.jpg', 10, '2023-11-12 10:15:00', '2023-11-12 10:15:00'),
('b4b2c1d8-11b8-4b8e-b920-08c7294b55d1', '9463b28a-0de9-453e-b65a-264e7a58f11e', 'Testing a post', NULL, 5, '2023-11-11 17:00:00', '2023-11-11 17:00:00'),
('1f29ed4f-dca0-4ae4-a167-bf4f0b1a12ae', '9f3b9a56-15b6-498d-ba7b-d5d8e4c20cc7', 'My first post', 'post2_image.jpg', 15, '2023-11-10 14:20:00', '2023-11-10 14:20:00'),
('f7ef89b2-6cc3-4b2d-a612-c1e76aa74a6d', '7e81a754-64a3-4a4a-93ff-28c0b2691925', 'Post example', NULL, 8, '2023-11-09 10:45:00', '2023-11-09 10:45:00');

INSERT INTO comments (id, user_id, post_id, comment_text, comment_image, likes, created_at, updated_at)
VALUES 
('8e6997a3-0571-4d1a-8b56-96a5b9b5d8a6', '74b078d4-66cc-463e-bdbb-01c005a4e1bc', '6495b25e-5b29-4b5b-8f88-cc11b3007c54', 'Great post!', 'comment_img.jpg', 5, '2023-11-12 10:30:00', '2023-11-12 10:30:00'),
('36c2d8fe-2ad7-42eb-b5e2-8e81ad06a16f', '9463b28a-0de9-453e-b65a-264e7a58f11e', 'b4b2c1d8-11b8-4b8e-b920-08c7294b55d1', 'Nice one!', NULL, 3, '2023-11-11 17:15:00', '2023-11-11 17:15:00'),
('ff12e87c-f3e9-4c27-8483-3985e015dd8b', '9f3b9a56-15b6-498d-ba7b-d5d8e4c20cc7', '1f29ed4f-dca0-4ae4-a167-bf4f0b1a12ae', 'Keep it up!', 'comment2_img.jpg', 8, '2023-11-10 14:30:00', '2023-11-10 14:30:00'),
('a6a3e92f-df01-44a3-b91a-0985e9cb6e5b', '7e81a754-64a3-4a4a-93ff-28c0b2691925', 'f7ef89b2-6cc3-4b2d-a612-c1e76aa74a6d', 'Interesting post!', NULL, 6, '2023-11-09 11:00:00', '2023-11-09 11:00:00');

INSERT INTO services (id, name, description, created_at, updated_at)
VALUES 
('7b9c6f1e-9d1b-4e7b-8b89-991a8c0d9974', 'Delivery', 'Fast delivery services', '2023-11-12 11:00:00', '2023-11-12 11:00:00'),
('b54c6761-6f59-4b46-9f8e-f7f9cf8abf4d', 'Cleaning', 'Professional cleaning solutions', '2023-11-11 18:00:00', '2023-11-11 18:00:00'),
('fd9e75b4-c6a1-42e2-baf2-3678f12ab574', 'Consultation', 'Expert consultation services', '2023-11-10 15:00:00', '2023-11-10 15:00:00'),
('0e4f4eb8-0c85-4370-a6d3-1648833a432d', 'Repair', 'Repair and maintenance services', '2023-11-09 12:00:00', '2023-11-09 12:00:00'),
('fc1a8981-8bb1-4917-84e1-2cf97b4df5d6', 'Design', 'Creative design solutions', '2023-11-08 13:00:00', '2023-11-08 13:00:00');

INSERT INTO location_services (id, service_id, location_id, created_at, updated_at)
VALUES 
('f0c14ec9-f80c-4e61-bc19-5a32cfb2e75b', '7b9c6f1e-9d1b-4e7b-8b89-991a8c0d9974', '8dc6a7b0-eb49-4a38-8a0d-d81b5c2e7437', '2023-11-12 11:30:00', '2023-11-12 11:30:00'),
('cde9c0a3-791e-4a01-9d3d-9a51e2e89994', 'b54c6761-6f59-4b46-9f8e-f7f9cf8abf4d', '8917492f-0103-42c3-9d64-1694a99bfb39', '2023-11-11 18:30:00', '2023-11-11 18:30:00'),
('d264da2b-6ab4-4c98-83a2-3b87e40ab784', 'fd9e75b4-c6a1-42e2-baf2-3678f12ab574', '24db1ef5-2a5c-4c22-b45d-b051786da64e', '2023-11-10 15:30:00', '2023-11-10 15:30:00'),
('63c70cf6-5948-4c21-92a7-58b9a55e5a5c', '0e4f4eb8-0c85-4370-a6d3-1648833a432d', '2d1ccdb0-fcdb-4d03-a3cc-048a48ff115d', '2023-11-09 12:30:00', '2023-11-09 12:30:00'),
('1a3d75db-1200-4984-944d-4308b89c7125', 'fc1a8981-8bb1-4917-84e1-2cf97b4df5d6', 'b87a8d17-0b1b-4b65-a114-5c930b7ff39a', '2023-11-08 13:30:00', '2023-11-08 13:30:00');

INSERT INTO predictions (id, location_id, value, created_at, updated_at)
VALUES 
('72cdd7b5-d761-49e5-b13a-69e2d6e1b3db', '8dc6a7b0-eb49-4a38-8a0d-d81b5c2e7437', 0.75, '2023-11-12 12:00:00', '2023-11-12 12:00:00'),
('8e68f20b-1a94-49c8-a7a5-4ec7d04576a3', '8917492f-0103-42c3-9d64-1694a99bfb39', 0.5, '2023-11-11 19:00:00', '2023-11-11 19:00:00'),
('7a0b71d0-1aa2-481b-9f7b-9076fb7ae14e', '24db1ef5-2a5c-4c22-b45d-b051786da64e', 0.9, '2023-11-10 16:00:00', '2023-11-10 16:00:00'),
('abd11b68-9ec4-4b60-8727-499d72e0016d', '2d1ccdb0-fcdb-4d03-a3cc-048a48ff115d', 0.6, '2023-11-09 13:00:00', '2023-11-09 13:00:00'),
('1bca9a5b-c4a7-4d90-b694-28a5c78a6097', 'b87a8d17-0b1b-4b65-a114-5c930b7ff39a', 0.8, '2023-11-08 14:00:00', '2023-11-08 14:00:00');

INSERT INTO weather_data (id, location_id, rainfall, created_at, updated_at)
VALUES 
('f45a1472-6130-4d98-8f85-1e84e493a5e6', '8dc6a7b0-eb49-4a38-8a0d-d81b5c2e7437', 0.2, '2023-11-12 12:30:00', '2023-11-12 12:30:00'),
('bd7aaab2-9f10-4f5a-85cc-2a03968d6b0d', '8917492f-0103-42c3-9d64-1694a99bfb39', 0.1, '2023-11-11 19:30:00', '2023-11-11 19:30:00'),
('c74b3e1b-7b43-4e45-8719-7d97156b9e3e', '24db1ef5-2a5c-4c22-b45d-b051786da64e', 0.5, '2023-11-10 16:30:00', '2023-11-10 16:30:00'),
('87e134b0-63a2-470f-9ac5-8a4189ad25d8', '2d1ccdb0-fcdb-4d03-a3cc-048a48ff115d', 0.3, '2023-11-09 13:30:00', '2023-11-09 13:30:00'),
('25b3846b-fa3d-4825-a97c-f44af04c4bbd', 'b87a8d17-0b1b-4b65-a114-5c930b7ff39a', 0.4, '2023-11-08 14:30:00', '2023-11-08 14:30:00');
