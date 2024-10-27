
DROP TABLE IF EXISTS items;

CREATE TABLE items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  item_name TEXT NOT NULL,
  item_quantity INTEGER NOT NULL
);

INSERT INTO items (item_name, item_quantity)
VALUES
  ('apple', 10),
  ('banana', 5),
  ('cherry', 3),
  ('date', 7),
  ('elderberry', 2),
  ('fig', 1),
  ('grape', 9),
  ('honeydew', 4),
  ('kiwi', 6),
  ('lemon', 8);