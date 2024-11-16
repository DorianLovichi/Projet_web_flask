DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstname TEXT,
  lastname TEXT,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);

DROP TABLE IF EXISTS items;

CREATE TABLE items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  item_type TEXT NOT NULL,
  item_name TEXT NOT NULL,
  item_quantity INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id)
);

INSERT INTO items (user_id, item_type, item_name, item_quantity)
VALUES
  (1,'fruit', 'apple', 10),
  (1,'fruit', 'banana', 5),
  (1,'fruit', 'cherry', 3);