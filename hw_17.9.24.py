"""
-- a:

CREATE TABLE "category" (
	"category_id"	INTEGER,
	"name"	TEXT NOT NULL,
	PRIMARY KEY("category_id" AUTOINCREMENT)
);

CREATE TABLE "nutritions" (
	"nutrition_id"	INTEGER,
	"product_id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"calories"	INTEGER,
	"fats"	TEXT,
	"sugar"	TEXT,
	PRIMARY KEY("nutrition_id" AUTOINCREMENT),
	FOREIGN KEY("product_id") REFERENCES "products"("product_id")
);

CREATE TABLE "orders" (
	"order_id"	INTEGER,
	"date_time"	TEXT NOT NULL,
	"address"	TEXT NOT NULL,
	"customer_name"	TEXT NOT NULL,
	"customer_ph"	REAL,
	"total_price"	REAL NOT NULL,
	PRIMARY KEY("order_id" AUTOINCREMENT)
);

CREATE TABLE "orders_products" (
	"order_id"	INT,
	"product_id"	INT,
	"amount"	INT NOT NULL,
	PRIMARY KEY("order_id","product_id"),
	FOREIGN KEY("order_id") REFERENCES "orders"("id_order"),
	FOREIGN KEY("product_id") REFERENCES "products"("product_id")
);

CREATE TABLE "products" (
	"product_id"	INTEGER,
	"name"	TEXT,
	"price"	REAL,
	"category_id"	INTEGER,
	PRIMARY KEY("product_id" AUTOINCREMENT),
	FOREIGN KEY("category_id") REFERENCES ""
);

-- b:

-- 1.
-- טבלת המוצרים וטבלת הקטגוריוט
-- הקשר הוא: יחיד לרבים
-- הסבר: כל מוצר שייך לקטגוריה אחת בלבד, אך קטגוריה אחת יכולה לכלול מספר מוצרים
-- יחיד: כל מוצר  "פרודוקט" שייך לקטגוריה אחת
-- מפתח זר "אי די_קטיגורי" בטבלת מוצרים מפנה ל-"אי די_קטיגורי" בטבלת קטגוריות
-- רבים: קטגוריה אחת  יכולה לכלול מספר מוצרים

-- 2.
-- טבלת מוצרים וטבלת ערכים תזונתיים
-- הקשר הוא: יחיד לרבים
-- הסבר: כל מוצר יכול להיות לו ערכים תזונתיים שונים, אך כל ערך תזונתי שייך למוצר אחד בלבד.
-- יחיד: כל ערך תזונתי  שייך למוצר אחד
-- מפתח זר "אי די_פרודקט" בטבלת ערכים תזונתיים מפנה ל-"אי די_פרודקט"  בטבלת מוצרים
-- רבים: מוצר אחד יכול לכלול מספר ערכים תזונתיים

-- 3.
-- קשר: יחיד לרבים
-- הסבר: כל הזמנה יכולה לכלול מספר מוצרים, אך כל רשומת מוצר בהזמנה שייכת להזמנה אחת בלבד
-- יחיד: כל רשומת מוצר בהזמנה שייכת להזמנה אחת
-- מפתח זר "אי די_אורדר" בטבלת מוצרים בהזמנות מפנה ל-"אי די_אורדר" בטבלת הזמנות
-- רבים: הזמנה אחת יכולה לכלול מספר מוצרים

-- 4.
-- טבלת מוצרים וטבלת מוצרים בהזמנות
-- קשר: יחיד לרבים
-- הסבר: כל מוצר יכול להיות חלק ממספר הזמנות, אך כל רשומת מוצר בהזמנה שייכת למוצר אחד בלבד
-- יחיד: כל רשומת מוצר בהזמנה שייכת למוצר אחד
-- מפתח זר "אי די_פרודקט" בטבלת מוצרים בהזמנות מפנה ל-"אי די_פרודקט" בטבלת מוצרים
-- רבים: מוצר אחד יכול להיות חלק ממספר הזמנות

-- 5.
-- טבלת הזמנות וטבלת מוצרים בהזמנות
-- קשר: רבים לרבים
-- הסבר: הזמנה אחת יכולה לכלול מספר מוצרים, ומוצר אחד יכול להיכלל בכמה הזמנות
-- הקשר בין טבלת הזמנות למוצרים בהזמנות הוא קשר רבים לרבים
-- המפתח הראשי המורכב בטבלת מוצרים בהזמנות "אי די_אורדר, אי די_פרודקט" מייצג את הקשר הזה

-- c.

INSERT INTO category (name) VALUES
('Beverages'),
('Snacks'),
('Dairy'),
('Fruits'),
('Vegetables');

INSERT INTO products (name, price, category_id) VALUES
('Orange Juice', 5.99, 1),
('Chocolate Bar', 2.50, 2),
('Milk', 3.20, 3),
('Apple', 1.50, 4),
('Carrot', 0.99, 5),
('Coca Cola', 1.50, 1),    -- Beverages
('Pepsi', 1.40, 1),        -- Beverages
('Water Bottle', 0.99, 1), -- Beverages
('Orange Soda', 1.70, 1),  -- Beverages
('Iced Tea', 2.00, 1),     -- Beverages
('Potato Chips', 1.80, 2),   -- Snacks
('Pretzels', 2.20, 2),       -- Snacks
('Popcorn', 1.99, 2),        -- Snacks
('Granola Bar', 1.50, 2),    -- Snacks
('Cookies', 3.00, 2),        -- Snacks
('Cheese', 4.50, 3),      -- Dairy
('Yogurt', 1.25, 3),      -- Dairy
('Butter', 3.75, 3),      -- Dairy
('Cream Cheese', 2.50, 3),-- Dairy
('Ice Cream', 5.00, 3),   -- Dairy
('Banana', 1.20, 4),      -- Fruits
('Grapes', 2.99, 4),      -- Fruits
('Mango', 1.75, 4),       -- Fruits
('Pineapple', 3.00, 4),   -- Fruits
('Strawberries', 2.80, 4);-- Fruits


INSERT INTO nutritions (product_id, name, calories, fats, sugar) VALUES
(1, 'Orange Juice', 120, 0.2, 20),
(2, 'Chocolate Bar', 220, 12, 18),
(3, 'Milk', 150, 8, 12),
(4, 'Apple', 95, 0.3, 19),
(5, 'Carrot', 41, 0.1, 5),
(6, 'Coca Cola', 140, 0, 39),      -- Coca Cola
(7, 'Pepsi', 150, 0, 41),          -- Pepsi
(8, 'Water Bottle', 0, 0, 0),      -- Water Bottle
(9, 'Orange Soda', 160, 0, 44),    -- Orange Soda
(10, 'Iced Tea', 90, 0, 23),       -- Iced Tea
(11, 'Potato Chips', 160, 10, 1),  -- Potato Chips
(12, 'Pretzels', 110, 1, 1),       -- Pretzels
(13, 'Popcorn', 120, 5, 0),        -- Popcorn
(14, 'Granola Bar', 150, 6, 7),    -- Granola Bar
(15, 'Cookies', 250, 12, 18),      -- Cookies
(16, 'Cheese', 113, 9, 1),         -- Cheese
(17, 'Yogurt', 80, 1.5, 11),       -- Yogurt
(18, 'Butter', 100, 11, 0),        -- Butter
(19, 'Cream Cheese', 99, 10, 1),   -- Cream Cheese
(20, 'Ice Cream', 270, 14, 28),    -- Ice Cream
(21, 'Banana', 105, 0.3, 14),      -- Banana
(22, 'Grapes', 62, 0.3, 15),       -- Grapes
(23, 'Mango', 99, 0.6, 23),        -- Mango
(24, 'Pineapple', 50, 0.1, 10),    -- Pineapple
(25, 'Strawberries', 53, 0.5, 8);  -- Strawberries

INSERT INTO orders (date_time, address, customer_name, customer_ph, total_price) VALUES
('2024-09-17 10:30', '123 Main St', 'John Doe', '555-1234', 25.67),
('2024-09-17 11:45', '456 Oak St', 'Jane Smith', '555-5678', 15.30),
('2024-09-17 12:15', '789 Pine St', 'Emily Davis', '555-8765', 9.99),
('2024-09-17 13:00', '321 Elm St', 'Michael Johnson', '555-4321', 20.10),
('2024-09-17 13:30', '654 Maple St', 'Sarah Wilson', '555-6789', 30.55);

INSERT INTO orders_products (order_id, product_id, amount) VALUES
(1, 1, 2),
(1, 2, 1),
(2, 3, 1),
(3, 4, 3),
(4, 5, 5),
(5, 1, 1),
(5, 3, 2),
(5, 4, 2),
(1, 6, 3),     -- Coca Cola
(1, 11, 1),    -- Potato Chips
(2, 7, 2),     -- Pepsi
(2, 12, 2),    -- Pretzels
(3, 8, 1),     -- Water Bottle
(3, 13, 2),    -- Popcorn
(4, 9, 1),     -- Orange Soda
(4, 14, 2),    -- Granola Bar
(5, 10, 1),    -- Iced Tea
(5, 15, 1),    -- Cookies
(1, 16, 1),    -- Cheese
(2, 17, 3),    -- Yogurt
(3, 18, 2),    -- Butter
(4, 19, 1),    -- Cream Cheese
(5, 20, 1),    -- Ice Cream
(1, 21, 4),    -- Banana
(2, 22, 2),    -- Grapes
(3, 23, 3),    -- Mango
(4, 24, 1),    -- Pineapple
(5, 25, 2)    -- Strawberries


-- d.i:

SELECT
    p.name AS product_name,
    p.price AS product_price,
    n.name AS nutrition_name,
    n.calories AS calories,
    n.fats AS fats,
    n.sugar AS sugar,
    c.name AS category_name
FROM
    products p
JOIN
    nutritions n ON p.product_id = n.product_id
JOIN
    category c ON p.category_id = c.category_id
ORDER BY
    p.name;


-- d.ii:

   SELECT
    o.order_id,
    o.date_time,
    o.address,
    o.customer_name,
    o.customer_ph,
    o.total_price,
    p.product_id,
    p.name AS product_name,
    p.price AS product_price,
    op.amount AS quantity
FROM
    orders o
JOIN
    orders_products op ON o.order_id = op.order_id
JOIN
    products p ON op.product_id = p.product_id
ORDER BY
    o.order_id,
    p.name;


-- d.iii:

INSERT INTO orders_products (order_id, product_id, amount) VALUES (2, 5, 1)

-- הקוד לא עובד, אין לי מושג למה ואיך לתקן. נסיתי הרבה ונעזרתי בצאט גבט ולא הסתדר לי... אשמח אם תסביר לי איך פוטרים שאלה כזאת


-- d.iv:

UPDATE orders o
SET total_price = (				-- מגדיר מהו השדה שאנחנו רוצים לעדכן. במקרה זה, אנחנו מעדכנים את השדה  "טוטל_פרייס" של כל הזמנה.
    SELECT SUM(op.amount * p.price)	-- השאילתא הפנימית  מחושבת כאן. היא מחשבת את הסכום הכולל של כל המוצרים בהזמנה על ידי חיבור כמות המוצרים  שהוזמנו במחיר של כל מוצר
    FROM orders_products op
    JOIN products p ON op.product_id = p.product_id
    WHERE op.order_id = o.order_id
)
WHERE o.order_id IN (SELECT DISTINCT order_id FROM orders_products);    -- וודאת שהעדכון מתבצע רק עבור הזמנות שיש להן מוצרים



-- d.v:     מהי ההזמנה הכי יקרה? הכי זולה? ממוצע?

SELECT * FROM orders ORDER BY total_price DESC LIMIT 1;

SELECT * FROM orders ORDER BY total_price ASC LIMIT 1;

SELECT AVG(total_price) AS average_price FROM orders;


-- d.vi:     מי הלקוח שהזמין הכי הרבה פעמים?

SELECT customer_name, COUNT(order_id) AS order_count
FROM orders
GROUP BY customer_name
ORDER BY order_count DESC
LIMIT 1;


-- d.vii:  איזה מוצר נמכר הכי הרבה? הכי פחות? ממוצע?

SELECT product_id, SUM(amount) AS total_sold
FROM orders_products
GROUP BY product_id
ORDER BY total_sold DESC
LIMIT 1;

SELECT product_id, SUM(amount) AS total_sold
FROM orders_products
GROUP BY product_id
ORDER BY total_sold ASC
LIMIT 1;

SELECT AVG(total_sold) AS average_sold
FROM (
    SELECT SUM(amount) AS total_sold
    FROM orders_products
    GROUP BY product_id
);


-- d.viii:   איזה קטגוריה של מוצרים נמכרים הכי הרבה? הכי פחות?

SELECT p.category_id, SUM(op.amount) AS total_sold
FROM orders_products op
JOIN products p ON op.product_id = p.product_id
GROUP BY p.category_id
ORDER BY total_sold DESC
LIMIT 1;


SELECT p.category_id, SUM(op.amount) AS total_sold
FROM orders_products op
JOIN products p ON op.product_id = p.product_id
GROUP BY p.category_id
ORDER BY total_sold ASC
LIMIT 1;


-- d. ix:  בונוס: איזה מוצר מופיע בהכי הרבה הזמנות שונות?

SELECT product_id, COUNT(DISTINCT order_id) AS order_count
FROM orders_products
GROUP BY product_id
ORDER BY order_count DESC
LIMIT 1;

"""