-- DO NOT USE 

CREATE DATABASE Tea_DB;

USE Tea_DB;


CREATE TABLE tea_orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name_n VARCHAR(50) NOT NULL,
    tea_type VARCHAR(50) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM tea_orders

-- create table USERS
-- (
-- user_id INT AUTO_INCREMENT PRIMARY KEY,
-- u_name VARCHAR(50) NOT NULL,
-- email VARCHAR(50) NOT NULL,
-- mobile INT NOT NULL
-- );


-- INSERT INTO users (u_name, email, mobile)
-- VALUES
-- ('Lisa', 'lisa@simpson.com', 12345678);

-- SELECT * FROM users;

-- INSERT INTO orders (tea_id, user_id, collection_time)
-- VALUES
-- (1, 1, '15:00:00');


-- View to see the order queue! 

CREATE VIEW orders_view AS
SELECT o.order_id, t.tea_name, u.u_name AS user_name, o.collection_time
FROM orders o
JOIN tea t ON o.tea_id = t.tea_id
JOIN USERS u ON o.user_id = u.user_id;

SELECT * FROM orders_view;
