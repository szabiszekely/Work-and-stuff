-- 1 a,b
SELECT ship_state_province FROM orders
UNION -- All
SELECT state_province FROM customers;

-- 2
SELECT COUNT(category), product_name
FROM products
GROUP BY product_name;

-- 3
SELECT COUNT(id), ship_city
FROM orders
GROUP BY ship_city;

-- 4
SELECT COUNT(id), city
FROM customers
GROUP BY city
HAVING COUNT(id) < 3;