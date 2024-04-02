CREATE DATABASE TeaJinja_DB;

USE TeaJinja_DB;

create table tea
(
tea_id INT AUTO_INCREMENT PRIMARY KEY,
tea_name VARCHAR(50) NOT NULL,
tea_price DECIMAL(3,2) NOT NULL,
tea_file_name VARCHAR(50) NOT NULL
);


create table orders
(
order_id INT AUTO_INCREMENT PRIMARY KEY,
tea_id INT, FOREIGN KEY (tea_id) REFERENCES tea(tea_id),
quantity INT NOT NULL,
customer_name VARCHAR(50) NOT NULL,
collection_time TIME NOT NULL,
order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO tea (tea_name, tea_price, tea_file_name)
VALUES
('Strawberry', 4.95, 'images/strawberry.webp'),
('Brown Sugar', 4.95, 'images/bsugar.jpg');
-- ('Taro', 4.95, 'images/strawberry.webp'),
-- ('Matcha', 4.95, 'images/strawberry.webp'),
-- ('Rose Milk', 4.95, 'images/strawberry.webp'),
-- ('Mango Boba', 4.95, 'images/strawberry.webp'),
-- ('Classic Milk', 4.95, 'images/strawberry.webp'),
-- ('Honey Dew', 4.95, 'images/strawberry.webp');

SELECT * FROM tea;



SELECT * FROM orders;

-- View to see the order queue! 

CREATE VIEW orders_view AS
SELECT o.order_id, t.tea_name, u.u_name AS user_name, o.collection_time
FROM orders o
JOIN tea t ON o.tea_id = t.tea_id
JOIN USERS u ON o.user_id = u.user_id;

SELECT * FROM orders_view;
