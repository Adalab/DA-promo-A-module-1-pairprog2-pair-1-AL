/* Consultas múltiples 4 | PAIR 1: Alicia y Lara | 31/03 */
--

USE Northwind;

/* 1 */

/* Extraed información de los productos "Beverages".
En este caso nuestro jefe nos pode que le devolvamos toda la 
información necesaria para identificar un tipo de producto. En concreto, 
tienen especial interés por los productos con categoría "Beverages". Devuelve 
su el ID del producto, el nombre del producto y su ID de categoría. */

SELECT product_id, product_name, category_id
FROM products
WHERE category_id IN (SELECT category_id
						FROM categories
						WHERE category_name = "Beverages");


/* 2 */
/* Extraed la lista de países donde viven los clientes, pero no hay ningún 
proveedor ubicado en ese país. Suponemos que si se trata de ofrecer un mejor
 tiempo de entrega a los clientes, entonces podría dirigirse a estos países 
 para buscar proveedores adicionales. */

SELECT DISTINCT country
FROM customers
WHERE country NOT IN (SELECT country
						FROM suppliers)
ORDER BY country;
 -- Opcional: podemos ordenarlos alfabéticamente para facilitar su lectura.
 
 /* 3 */
/* Extraer los clientes que compraron mas de 20 articulos "Grandma's Boysenberry Spread"
Extraed una lista de pedidos y sus clientes que pidieron más de 20 artículos del producto
 "Grandma's Boysenberry Spread" (ProductID 6) en un solo pedido. */
 
 SELECT order_id AS lista_pedidos, customer_id AS clientes
 FROM orders
 WHERE order_id IN (SELECT order_id
					FROM order_details
					WHERE product_id IN (SELECT product_id
										 FROM products
										 WHERE product_id = 6)
					AND quantity > 20);
													
 /* 4 */
/* Extraed los 10 productos mas caros
Nos siguen pidiendo más queries correlacionadas. En este caso queremos
 saber cuáles son los 10 productos más caros. */
 
 SELECT product_id AS id, product_name AS nombre_producto, unit_price AS precio
 FROM products
 ORDER BY unit_price DESC
 LIMIT 10;
 -- Is this too simple????
 
 /* 5 */
 /* Extraed cuál es el producto que más ha sido comprado y la cantidad que se compró. */

 SELECT product_id AS id, product_name AS nombre_producto -- cantidad
 FROM products
 WHERE product_id IN (SELECT product_id
						FROM order_details
                        GROUP BY product_id
                       -- HAVING MAX(quantity));
                        
 