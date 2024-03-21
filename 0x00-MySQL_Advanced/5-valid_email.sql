-- triger to update the valid email attribute field
DROP TRIGGER IF EXISTS validate_email;
DELIMITER $$

CREATE TRIGGER validate_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;