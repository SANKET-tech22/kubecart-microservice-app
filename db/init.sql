CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price INT
);

INSERT INTO products (name, price) VALUES
('Laptop', 8000),
('Phone', 5000)