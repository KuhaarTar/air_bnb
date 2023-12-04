USE air_bnb;

# <--TRIGGERS-->

CREATE TRIGGER IF NOT EXISTS before_insert_rules
    BEFORE INSERT
    ON apartment_rules
    FOR EACH ROW
BEGIN
    IF new.apartment_id NOT IN (SELECT id FROM apartment)
    THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Such apartment does not exist';
    END IF;
END;

CREATE TRIGGER IF NOT EXISTS determine_update_transaction
    BEFORE UPDATE
    ON transaction
    FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Not allowed to update transaction';
END;

CREATE TRIGGER IF NOT EXISTS lessor_validate
    BEFORE INSERT
    ON lessor
    FOR EACH ROW
BEGIN
    IF LENGTH(new.email) <= 10
    THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Not valid lessor email';
    END IF;
END;

CREATE TRIGGER IF NOT EXISTS renter_name_validate
    BEFORE INSERT
    ON renter
    FOR EACH ROW
BEGIN
    IF new.first_name NOT IN ('Alice', 'Bob', 'Oliver', 'Emily', 'Daniel',
                              'Sophia', 'Ava', 'Ethan', 'Mia', 'Liam')
    THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Not valid first_name';
    END IF;
END;


# <--PROCEDURES-->

DELIMITER //
CREATE PROCEDURE IF NOT EXISTS insert_into_lessor(
    IN email_ VARCHAR(255),
    IN phone_ VARCHAR(100),
    IN first_name_ VARCHAR(50),
    IN last_name_ VARCHAR(50)
)
BEGIN
    INSERT INTO lessor(email, phone, first_name, last_name)
    VALUES (email_, phone_, first_name_, last_name_);
    SELECT * FROM lessor ORDER BY id DESC LIMIT 1;
END //
DELIMITER //


DELIMITER //
CREATE PROCEDURE IF NOT EXISTS insert_values_lessor_noname()
BEGIN
    DECLARE i INTEGER;
    SET i = 0;

    WHILE i <= 10
        DO
            INSERT INTO lessor(email, phone, first_name, last_name)
            VALUES (CONCAT('NonameGmail', i), CONCAT('Noname', i),
                    CONCAT('Noname', i), CONCAT('Noname', i));
            SET i = i + 1;
        END WHILE;

    SELECT * FROM lessor ORDER BY id DESC LIMIT 10;
END;
DELIMITER //

DELIMITER //
CREATE FUNCTION IF NOT EXISTS find_aggregate(type_of_search VARCHAR(10))
    RETURNS INTEGER
    READS SQL DATA
BEGIN
    IF type_of_search = 'AVG' THEN
        RETURN (SELECT AVG(count_of_reviews) FROM apartment_rating);
    END IF;
    IF type_of_search = 'MAX' THEN
        RETURN (SELECT MAX(count_of_reviews) FROM apartment_rating);
    END IF;
    IF type_of_search = 'MIN' THEN
        RETURN (SELECT MIN(count_of_reviews) FROM apartment_rating);
    END IF;
    IF type_of_search = 'SUM' THEN
        RETURN (SELECT SUM(count_of_reviews) FROM apartment_rating);
    END IF;
    RETURN NULL;
END;

CREATE PROCEDURE IF NOT EXISTS select_aggregate_from_rating
    (IN type_of_search VARCHAR(50))
BEGIN
    SELECT (find_aggregate(type_of_search));
END;

CREATE PROCEDURE IF NOT EXISTS add_apartment_amenity(
  apartment_id_ BIGINT,
  amenity_id_ BIGINT
)
BEGIN
  IF NOT EXISTS (SELECT * FROM apartment WHERE id = apartment_id_)
  THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Apartment with ID = @apartment_id does not exist';
  END IF;

  IF NOT EXISTS (SELECT * FROM amenities WHERE amenities_id = amenity_id_)
  THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Amenity with ID = @amenity_id does not exist';
  END IF;

  INSERT INTO apartment_has_amenities (apartment_id, amenities_id)
  VALUES (apartment_id_, amenity_id_);
  SELECT * FROM apartment_has_amenities LIMIT 1;
END;
DELIMITER //


DELIMITER //
CREATE PROCEDURE IF NOT EXISTS create_table_with_variable_name(
    IN tableName VARCHAR(150)
)
BEGIN
    DECLARE numColumns INT;
    DECLARE @i INT;
    SET @numColumns = FLOOR(RAND() * 10) + 1;
    SET @sql = CONCAT('CREATE TABLE ', tableName, ' (');
    SET @i = 1;
    WHILE @i <= @numColumns DO

        SET @sql = CONCAT(@sql, 'column_', CAST(@i AS CHAR ), ' INT,');
        SET @i = @i + 1;
    END WHILE;

    SET @sql = CONCAT(@sql, ')');

    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END;
DELIMITER //

CALL create_table_with_variable_name('GACHI');

DROP PROCEDURE create_table_with_variable_name;
DROP PROCEDURE add_apartment_amenity;

CALL add_apartment_amenity(1,1)
