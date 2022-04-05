/* CTEs 1 | PAIR 1: Alicia y Lara | 04/04 */
USE Northwind;

/* 1 */
/* Extraer en una CTE todos los nombres de las compañias y los id de los clientes.
Para empezar nos han mandado hacer una CTE muy sencilla el id del cliente y el
 nombre de la compañia de la tabla Customers. */
 
WITH cte_id_y_nombre AS (
	SELECT customer_id, company_name
	FROM customers)
SELECT *
FROM cte_id_y_nombre;

/* 2 */
/* 
Selecciona solo los de que vengan de "Germany"
Ampliemos un poco la query anterior. En este caso, queremos un resultado similar al
 anterior, pero solo queremos los que pertezcan a "Germany". */
 
WITH cte_id_y_nombre_alemania AS (
	SELECT customer_id, company_name, country
	FROM customers
    WHERE country = 'Germany')
SELECT customer_id, company_name
FROM cte_id_y_nombre_alemania;


/* 3 */
/* Extraed el id de las facturas y su fecha de cada cliente.
En este caso queremos extraer todas las facturas que se han emitido a un cliente, 
su fecha la compañia a la que pertenece.
📌 NOTA En este caso tendremos columnas con elementos repetidos(CustomerID, y Company Name). */

WITH facturas AS (
	SELECT orders.order_id, orders.order_date, orders.customer_id, customers.company_name
	FROM orders
    INNER JOIN customers
    ON orders.customer_id = customers.customer_id
    GROUP BY orders.order_id, orders.customer_id)
SELECT company_name AS compañia, order_id AS factura, order_date AS fecha
FROM facturas;



/* 4 */
/* Contad el número de facturas por cliente. Mejoremos la query anterior. En este caso
 queremos saber el número de facturas emitidas por cada cliente. */
 
WITH facturas AS (
	SELECT orders.order_id, orders.order_date, orders.customer_id, customers.company_name
	FROM orders
    INNER JOIN customers
    ON orders.customer_id = customers.customer_id
    GROUP BY orders.order_id, orders.customer_id)
SELECT company_name AS compañia, COUNT(DISTINCT order_id) AS cantidad_facturas
FROM facturas
GROUP BY company_name;

 
 /* 5 */
 
 /* Cuál la cantidad media pedida de todos los productos ProductID.
Necesitaréis extraet la suma de las cantidades por cada producto y calcular la media*/

-- WITH media_productos AS (
	WITH total_productos AS (
		SELECT order_details.quantity, products.product_id, products.product_name
		FROM order_details
		INNER JOIN products
		ON order_details.product_id = products.product_id
		GROUP BY order_details.product_id, order_details.quantity)
	SELECT product_name AS producto, SUM(quantity) AS total_pedidos
	FROM media_productos
	GROUP BY product_name)
-- SELECT AVG(total_pedidos) AS media_total_pedidos;
-- FROM media_productos;
