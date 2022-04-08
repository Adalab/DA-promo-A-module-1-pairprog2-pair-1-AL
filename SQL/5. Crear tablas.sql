/* CREAR TABLAS | PAIR 1: Alicia y Lara | 05/04 */


/*
Tabla Zapatillas: tiene 4 columnas: id, modelo, color, talla con las siguientes características:
idZapatillas: es una clave primaria de tipo int, autoincremental y no nula.
Modelo: es una cadena de caracteres de longitud máxima de 45 caracteres, no nula.
Talla: es un integer, no nula.
Color: es una cadena de caracteres de longitud máxima de 45 caracteres, no nula. */

CREATE TABLE zapatillas (
id_zapatillas INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
modelo_zapatillas VARCHAR (45) NOT NULL,
talla_zapatillas INT NOT NULL,
color_zapatillas VARCHAR (45) NOT NULL
);

/* Tabla Clientes: tiene 9 columnas idcliente, nombre, numero_telefono, email, direccion, ciudad, provincia, pais, codigo_postal con las siguientes características:
idEmpleado: es una clave primaria de tipo int, autoincremental y no nula.
Nombre: es una cadena de caracteres de longitud máxima de 45 caracteres, no nula.
Numero_telefono: es integer de longitud máxima de 9 caracteres, no nula.
Email: es una cadena de caracteres de longitud máxima de 45 caracteres, no nula.
Direccion: es una cadena de caracteres de longitud máxima de 45 caracteres, no nula.
Ciudad: es una cadena de caracteres de longitud máxima de 45 caracteres, puede ser nula.
Provincia: es una cadena de caracteres de longitud máxima de 45 caracteres, no nula.
Pais: es una cadena de caracteres de longitud máxima de 45 caracteres, no nula.
Codigo_postal: es integer de longitud máxima 5, no nula. */

CREATE TABLE clientes (
id_cliente INT AUTO_INCREMENT NOT NULL PRIMARY KEY, #Cambiamos a cliente para que sea clave única
nombre_cliente VARCHAR (45) NOT NULL,
numero_telefono INT (9) NOT NULL, #Warning al limitar tamaño del INT
email VARCHAR (45) NOT NULL,
direccion VARCHAR (45) NOT NULL,
ciudad VARCHAR (45) NOT NULL,
provincia VARCHAR (45) NOT NULL,
pais VARCHAR (45) NOT NULL,
codigo_postal INT (5) NOT NULL);

/* Tabla Empleados: tiene 5 columnas idEmpleado, nombre, tienda, salario, fecha_incorporacion con las siguientes características:
idEmpleado: es una clave primaria de tipo int, autoincremental y no nula.
Nombre: es una cadena de caracteres de longitud máxima de 45 caracteres, no nula.
Tienda: es una cadena de caracteres de longitud máxima de 45 caracteres, no nula.
salario: es decimal, puede ser nula.
fecha_incorporacion: es una columna de tipo date, no nula. */

CREATE TABLE empleados (
id_empleado INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
nombre_empleado VARCHAR(45) NOT NULL,
tienda_empleado VARCHAR(45) NOT NULL,
salario_empleado FLOAT,
fecha_incorporacion_empleado DATE NOT NULL
); 

/* Tabla Facturas: tiene 5 columnas idFactura, idEmpleado, idCliente, fecha, total con las siguientes características:
idFactura: es una clave primaria de tipo int, autoincremental y no nula.
idEmpleado: es una clave foránea de tipo int, no nula.
idCliente: es una clave foránea de tipo int, no nula.
idZapatilla: es una clave foránea de tipo int, no nula
Fecha: es una columna de tipo date, no nula.
Total: es decimal, no nula. */


CREATE TABLE facturas (
	id_factura INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    numero_factura VARCHAR(45) NOT NULL,
	id_empleado INT NOT NULL REFERENCES empleados,
	id_cliente INT NOT NULL REFERENCES clientes,
	id_zapatilla INT NOT NULL REFERENCES zapatillas,
    fecha DATE NOT NULL,
	total FLOAT NOT NULL);
