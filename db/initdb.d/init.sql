USE hack-u-db;

DROP TABLE IF EXISTS presents;

CREATE TABLE presents
(
  id             INT PRIMARY KEY AUTO_INCREMENT,
  user_id        INT,
  month          INT
);