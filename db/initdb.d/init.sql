USE hack-u-db;

CREATE TABLE user_res
(
  id               INT PRIMARY KEY AUTO_INCREMENT,
  money_min        INT,
  money_max        INT,
  age              INT,
  sex              INT,
  relationship     INT,
  topic1           BOOLEAN,
  topic2           BOOLEAN,
  topic3           BOOLEAN,
  topic4           BOOLEAN,
  topic5           BOOLEAN,
  user_res         TEXT
);