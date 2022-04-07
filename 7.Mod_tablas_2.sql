/*  Modificación de tablas 2 | PAIR 1: Alicia y Lara | 07/04 */

USE `leccion-7-sql`;

/* 1 */
-- Zapatillas
/* ALTER TABLE zapatillas AUTO_INCREMENT = 1; DELETE FROM zapatillas; */


INSERT INTO zapatillas (modelo_zapatillas, color_zapatillas, marca, talla_zapatillas)
VALUES ("XQYUN", "negro", "Nike", 42), ("UOPMN", "rosa", "Nike", 39), ("OPNYT", "verde", "Adidas", 35);

SELECT *
FROM zapatillas;

/* 2 */
INSERT INTO empleados (id_empleado, nombre_empleado, tienda_empleado, salario_empleado, fecha_incorporacion_empleado)
VALUES (1, 'Laura', 'Alcobendas', 25987, "2010-09-03"), (2, 'Maria', 'Sevilla', 0, "2021-04-11"), (3, 'Ester', 'Oviedo', 30165, "2000-11-29");

/* UPDATE empleados SET salario_empleado = 30165.98
WHERE id_empleado = 3; */ -- REDONDEA!

SELECT *
FROM empleados; 

/* 3 */
-- Tabla clientes
INSERT INTO clientes (id_cliente, nombre_cliente, numero_telefono, email, direccion, ciudad, provincia, codigo_postal)
VALUES (1, "Monica", 1234567289, "monica@email.com", "Calle Felicidad", "Móstoles", "Madrid", 28176),
(2, "Lorena", 289345678, "lorena@email.com", "Calle Alegria", "Barcelona", "Barcelona", 12346),
(3, "Carmen", 298463759, "carmen@email.com", "Calle del Color", "Vigo", "Pontevedra", 23456);

SELECT *
FROM clientes;

/* 4 */
-- Tabla facturas

INSERT INTO facturas (id_factura, numero_factura, fecha, id_zapatilla, id_empleado, id_cliente, total)
VALUES (1, "123", "2001-12-11", 1, 2, 1, 54.98), (2, "1234", "2005-05-23", 1, 1, 3, 89.91), (3, "12345", '2015-09-18', 2, 3, 3, 76.23); 

SELECT *
FROM facturas;

#SEGUNDA PARTE

-- ZAPATILLAS ROSAS
UPDATE zapatillas SET color_zapatillas = "amarillas"
WHERE id_zapatillas = 2;

SELECT * 
FROM zapatillas;

-- LAURA SE MUDA A A CORUÑA

UPDATE empleados SET tienda_empleado = "A Coruña"
WHERE id_empleado = 1;

SELECT *
FROM empleados;

-- CLIENTES
UPDATE clientes SET num_telefono = 123456728
WHERE id_clientes = 1;

SELECT *
FROM clientes;

-- FACTURAS
UPDATE facturas SET total = 89.91 
WHERE id_factura = 3;

SELECT *
FROM facturas;