/* Modificación de tablas | PAIR 1: Alicia y Lara | 06/04 */

USE `leccion-7-sql`;

/* 1 */
-- TABLA ZAPATILLAS

/* Incluir Marca:  es una cadena de caracteres de longitud máxima de 45 caracteres, no nula.
Talla`: es un entero, no nulo. (aunque ya está talla_zapatillas)*/ 

ALTER TABLE zapatillas
ADD COLUMN marca VARCHAR(45) NOT NULL, 
ADD COLUMN talla INT NOT NULL;

/* 2 */
-- TABLA​ EMPLEADOS
-- Cambiar salario_empleado a FLOAT NOT NULL.

ALTER TABLE empleados
MODIFY salario_empleado FLOAT NOT NULL; 

/* 3 */
-- TABLA CLIENTES
/* `Pais`: Eliminar hemos incluido en la tabla pero nuestro negocio solo distribuye a España, 
por lo que es una columna que no hará falta. La eliminaremos. 
​`Codigo Postal`: es un *string*, pero esto no tiene mucho ya que son números de longitud
 fija de 5 caracteres. Por lo tanto, cambiaremos el tipo a entero de longitud 5. */
 -- En la tabla previa ya era INT(5), aunque sí comentamos en clase que fuera string.
 
 ALTER TABLE clientes
 DROP COLUMN pais,
 MODIFY codigo_postal INT (5) NOT NULL;

/* 4 */
-- TABLA FACTURAS
-- Incluir total

ALTER TABLE facturas
ADD COLUMN total FLOAT;


