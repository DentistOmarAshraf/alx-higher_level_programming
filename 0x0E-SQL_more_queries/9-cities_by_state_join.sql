-- Inner Join
SELECT c.id, c.name, s.name FROM states s INNER JOIN cities c ON c.state_id = s.id;
