USE hack-u-db;

CREATE TABLE user_res
(
  id               INT PRIMARY KEY AUTO_INCREMENT,
  min_money        INT,
  max_money        INT,
  age              INT,
  sex              INT,
  relationship     INT,
  fashion          BOOLEAN,
  daily            BOOLEAN,
  food             BOOLEAN,
  sports           BOOLEAN,
  entertainment    BOOLEAN,
);