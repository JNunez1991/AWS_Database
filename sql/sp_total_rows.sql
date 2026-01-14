USE INE;

-- Elimino la StoredProcedure en caso que ya exista
DROP PROCEDURE IF EXISTS sp_total_rows;

-- Creo la nueva StoredProcedure
CREATE PROCEDURE sp_total_rows (
    IN p_table_name VARCHAR(64),
    OUT p_total_rows BIGINT
)
BEGIN
    -- 1. Preparo sentencia concatenando el nombre de la tabla
    SET @sql_stmt = CONCAT('SELECT COUNT(*) INTO @row_count FROM ', p_table_name);

    -- 2. Ejecuto sentencia dinámica
    PREPARE stmt FROM @sql_stmt;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    -- 3. Asigno resultado de la variable al parámetro de salida
    SET p_total_rows = @row_count;
END;

-- Chequeo que haya quedado correctamente creada
SHOW CREATE PROCEDURE sp_total_rows;
