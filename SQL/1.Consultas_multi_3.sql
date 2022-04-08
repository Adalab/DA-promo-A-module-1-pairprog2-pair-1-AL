/* Consultas múltiples 3 | PAIR 1: Alicia y Lara | 30/03 */

USE Northwind;
/* 1 */
/* Extraer toda la información sobre las compañias que tengamos en la BBDD.
Nuestros jefes nos han pedido que creemos una query uqe nos devuelva todos
los clientes y proveedores que tenemos en la BBDD. Mostrad la ciudad a la que 
pertenecen, el nombre de la empresa y el nombre del contacto, además de la relación
(Proveedpr o Cliente). Pero importante! No debe haber duplicados en nuestra respuesta */

SELECT customer_id AS ID, city AS ciudad, company_name AS empresa, contact_name AS contacto
FROM customers
UNION
SELECT supplier_id, city, company_name, contact_name
FROM suppliers;
-- Para marcar cuál es cliente y cual proveedor, nos fijamos en el id (letras / números).

/* 2 */
/*Extraer todos los pedidos gestionados por "Nancy Davolio"
En este caso, nuestro jefe quiere saber cuantos pedidos ha
 gestionado "Nancy Davolio", una de nuestras empleadas. Nos pide 
 todos los detalles tramitados por ella. */
 
 SELECT *
 FROM orders
 WHERE employee_id IN (SELECT employee_id 
						FROM employees
						WHERE first_name = "Nancy" AND last_name = "Davolio");

/* 3 */ 
/*Extraed todas las empresas que no han comprado en el año 1997*/
-- Year

SELECT customer_id AS id_cliente, company_name AS empresa
FROM customers
WHERE customer_id  IN (SELECT customer_id
						FROM orders	
                        WHERE YEAR(order_date) != "1997");


/* 4 */
/*Extraed toda la información de los pedidos donde tengamos "Konbu" */
 
 SELECT *
 FROM orders
 WHERE order_id IN (SELECT order_details.order_id
						FROM order_details
						INNER JOIN products
						ON order_details.product_id = products.product_id
                        WHERE products.product_name = "Konbu");

 