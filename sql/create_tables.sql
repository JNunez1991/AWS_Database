USE INE;

-- Creo la tabla de descripcion IPC
CREATE TABLE t_desc_ipc (
    Division TINYINT PRIMARY KEY,
    Descripcion VARCHAR(255) NOT NULL
);


-- Creo la tabla donde se almaceran los datos de IPC
-- DECIMAL(18,4) = 18 digitos en total (ultimos 4 son decimales)
CREATE TABLE t_ipc (
	Periodo VARCHAR(15), 
	Division TINYINT,
	Ponderacion DECIMAL(18,4) NOT NULL, 
	Indice DECIMAL(18,4) NOT NULL, 
	Var_mensual DECIMAL(18,4) NOT NULL,
    Var_ac_anual DECIMAL(18,4) NOT NULL, 
    Var_doce_meses DECIMAL(18,4) NOT NULL, 
    Incidencia DECIMAL(18,4) NOT NULL,
    PRIMARY KEY (Periodo, Division)
);

-- Creo la tabla de descripcion IMS
CREATE TABLE t_desc_ims (
    Sector CHAR(1) PRIMARY KEY,
    Descripcion VARCHAR(255) NOT NULL
);

-- Creo la tabla donde se almaceran los datos de IMS
CREATE TABLE t_ims (
	Periodo VARCHAR(15), 
	Sector CHAR(1),
	Indice DECIMAL(18,4) NOT NULL, 
	Mes DECIMAL(18,4) NOT NULL, 
	AcumuladoAnual DECIMAL(18,4) NOT NULL,
    UltimosDoceMeses DECIMAL(18,4) NOT NULL, 
    Incidencias DECIMAL(18,4) NOT NULL, 
    PRIMARY KEY (Periodo, Sector)
);


-- Creo la tabla de descripcion ICCV
CREATE TABLE t_desc_iccv (
    Rubro TINYINT PRIMARY KEY,
    Descripcion VARCHAR(255) NOT NULL
);

-- Creo la tabla donde se almacenaran los datos de IMS
CREATE TABLE t_iccv (
	Periodo VARCHAR(15), 
	Rubro TINYINT,
	Indice DECIMAL(18,4) NOT NULL, 
	VariacionMensual DECIMAL(18,4) NOT NULL, 
    Incidencias DECIMAL(18,4) NOT NULL, 
    PRIMARY KEY (Periodo, Rubro)
);

-- Muestra las tablas creadas
SHOW TABLES;

-- Elimina una tabla
DROP TABLES t_ipc;
DROP TABLES t_ims;
DROP TABLES t_iccv;

-- Elimina todos los registros de una tabla
TRUNCATE TABLE t_ipc;
TRUNCATE TABLE t_ims;
TRUNCATE TABLE t_iccv;
