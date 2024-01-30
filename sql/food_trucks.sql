CREATE TABLE users (
  id INTEGER NOT NULL UNIQUE,
  first TEXT NOT NULL,
  last TEXT NOT NULL,
  avatar TEXT NOT NULL,
  email TEXT NOT NULL,
  username TEXT NOT NULL
);

CREATE TABLE trucks (
  id INTEGER NOT NULL UNIQUE,
  name TEXT NOT NULL,
  website TEXT NOT NULL,
  category TEXT NOT NULL,
  vegetarian_friendly BOOLEAN NOT NULL,
  owner_id INTEGER NOT NULL REFERENCES users(id)
);

CREATE TABLE reviews (
  id INTEGER NOT NULL UNIQUE,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  reviewer_id INTEGER REFERENCES users("id"),
  rating INTEGER NOT NULL,
  truck_id INTEGER NOT NULL REFERENCES trucks("id")
);

CREATE TABLE menu_items (
    id INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL,
    calories INTEGER NOT NULL
);

CREATE TABLE truck_menu_items (
  truck_id INTEGER NOT NULL REFERENCES trucks("id"),
  menu_item_id INTEGER NOT NULL REFERENCES menu_items("id"),
  price INTEGER NOT NULL
);



INSERT INTO users (id, first, last, avatar, email, username) VALUES
(1, 'Alice', 'Smith', 'avatar1.png', 'alice@example.com', 'alice123'),
(2, 'Bob', 'Jones', 'avatar2.png', 'bob@example.com', 'bobjones'),
(3, 'Charlie', 'Brown', 'avatar3.png', 'charlie@example.com', 'charlieb');

INSERT INTO trucks (id, name, website, category, vegetarian_friendly, owner_id) VALUES
(1, 'Tasty Treats', 'http://tastytreats.com', 'Dessert', TRUE, 1),
(2, 'Healthy Eats', 'http://healthyeats.com', 'Salads', TRUE, 2),
(3, 'Grill Master', 'http://grillmaster.com', 'BBQ', FALSE, 3);

INSERT INTO reviews (id, title, content, reviewer_id, rating, truck_id) VALUES
(1, 'Delicious Desserts', 'Loved the variety of sweets!', 1, 5, 1),
(2, 'Fresh and Tasty', 'Healthy salads, perfect for lunch.', 2, 4, 2),
(3, 'BBQ at its best', 'The best ribs I have ever tasted!', 3, 5, 3);

INSERT INTO menu_items (id, name, calories) VALUES
(1, 'Chocolate Cake', 500),
(2, 'Caesar Salad', 350),
(3, 'BBQ Ribs', 700),
(4, 'Vegan Burger', 450),
(5, 'Ice Cream Sundae', 550);

INSERT INTO truck_menu_items (truck_id, menu_item_id, price) VALUES
(1, 1, 300), -- Chocolate Cake in Tasty Treats
(1, 5, 250), -- Ice Cream Sundae in Tasty Treats
(2, 2, 150), -- Caesar Salad in Healthy Eats
(2, 4, 200), -- Vegan Burger in Healthy Eats
(3, 3, 500); -- BBQ Ribs in Grill Master
