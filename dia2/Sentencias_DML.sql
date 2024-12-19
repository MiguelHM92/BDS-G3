-- Active: 1734576852746@@127.0.0.1@3306@datag3
-- SENTENCIAS DML
-- INSERTAR DATOS (INSERT)
INSERT INTO alumno(nro_documento,nombre) VALUES('100','Miguel');
-- INSERT de varios valores
INSERT INTO alumno(nro_documento,nombre,nota)
VALUES
('200','ana',15),
('300','luis',20),
('400','jose',11),
('500','raul',10),
('600','carmen',13),
('700','jorge',16),
('800','daniel',20),
('900','luisa',17),
('1000','pedro',5);

-- ACTUALIZAR DATOS(UPDATE)
UPDATE alumno SET email = 'codigo@gmail.com';
-- Actualizar con WHERE
UPDATE alumno SET email = 'miguel@gmail.com' WHERE id = 1;
-- Actualizar con funciones
UPDATE alumno SET email = CONCAT(nombre,'@gmail.com') WHERE id != 1;
-- ELIMINAR DATOS(DELETE)
DELETE FROM alumno WHERE id = 5;

-- SELECCIONAR (SELECT)
SELECT * FROM alumno;
SELECT nombre,nota FROM alumno;
SELECT nombre,nota FROM alumno WHERE nota > 10;
