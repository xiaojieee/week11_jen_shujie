CREATE DATABASE TeaJinja_DB;

USE TeaJinja_DB;

create table tea
(
tea_id INT AUTO_INCREMENT PRIMARY KEY,
tea_name VARCHAR(50) NOT NULL,
tea_price FLOAT(3,2) NOT NULL,
tea_file_name VARCHAR(50) NOT NULL
);


create table collection
(
collection_id INT AUTO_INCREMENT PRIMARY KEY,
collection_number INT NOT NULL,
collection_time TIME NOT NULL
);


create table orders
(
order_id INT AUTO_INCREMENT PRIMARY KEY,
tea_id INT, FOREIGN KEY (tea_id) REFERENCES tea(tea_id),
quantity INT NOT NULL,
customer_name VARCHAR(50) NOT NULL,
order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
collection_id INT, FOREIGN KEY (collection_id) REFERENCES collection(collection_id)
);


INSERT INTO tea (tea_name, tea_price, tea_file_name)
VALUES
('Strawberry', 4.95, 'images/strawberry.webp'),
('Brown Sugar', 4.95, 'images/bsugar.jpg'),
('Taro', 5.00, 'images/taro1.jpg'),
('Matcha', 5.95, 'images/matcha1.jpg'),
('Rose Milk', 4.95, 'images/rose.webp'),
('Mango Boba', 5.95, 'images/mango.jpg'),
('Classic Milk', 3.95, 'images/milk.jpg'),
('Honey Dew', 5.95, 'images/honeydew.jpg');


SELECT * FROM tea;

SELECT * FROM collection;

SELECT * FROM orders;


-- View to see who ordered what and collection time and collection number
CREATE VIEW OrderQueue AS
SELECT o.customer_name, t.tea_name, o.quantity, c.collection_number, c.collection_time
FROM orders o
JOIN tea t ON o.tea_id = t.tea_id
JOIN collection c ON o.collection_id = c.collection_id;

SELECT * FROM OrderQueue;
