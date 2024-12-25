-- Active: 1734576852746@@127.0.0.1@3306@datag3
CREATE TABLE empresa(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nro_ruc VARCHAR(11) NOT NULL,
    razon_social VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);

INSERT INTO empresa(nro_ruc,razon_social,email)
VALUES
('1010','Chespirito SRL','chespi@gmail.com'),
('1020','Barberia Figaro SAC','barfig@gmail.com'),
('1030','Delicia Restaurante SA','delres@gmail.com')

CREATE TABLE ciudad(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
);

INSERT INTO ciudad(nombre) VALUES ('Lima'),('Huaraz'),('Arequipa')

CREATE TABLE direccion(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    empresa_id int NOT NULL,
    ciudad_id int NOT NULL,
    direccion VARCHAR(80),
    FOREIGN KEY (empresa_id) REFERENCES empresa(id),
    FOREIGN KEY (ciudad_id) REFERENCES ciudad(id)
);

INSERT INTO direccion(empresa_id,ciudad_id,direccion)
VALUES
(1,1,'Av. Los Robles 123'),
(2,2,'Jr. Carlos V 1025'),
(3,2,'Av. Ramon Castilla 123')

