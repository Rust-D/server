USE hack-u-db;

CREATE TABLE user_res
(
  id               INT PRIMARY KEY AUTO_INCREMENT,
  money_min        INT,
  money_max        INT,
  age              INT,
  sex              INT,
  season           INT,
  topic1           INT,
  topic2           INT,
  topic3           INT,
  topic4           INT,
  topic5           INT,
  user_res         TEXT
);