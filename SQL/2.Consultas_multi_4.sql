/* Consultas múltiples 4 | PAIR 1: Alicia y Lara | 31/03 */

USE Northwind;

/* 1 */

/* Extraed información de los productos "Beverages".
ID del producto, el nombre del producto y su ID de categoría. */

SELECT product_id, product_name, category_id
FROM products
WHERE category_id IN (SELECT category_id
						FROM categories
						WHERE category_name = "Beverages");


/* 2 */
/* Extraed la lista de países donde viven los clientes, pero no hay ningún 
proveedor ubicado en ese país. */

SELECT DISTINCT country
FROM customers
WHERE country NOT IN (SELECT country
						FROM suppliers)
ORDER BY country;
 -- Opcional: podemos ordenarlos alfabéticamente para facilitar su lectura.
 
/* 3 */
/* Extraer los clientes que compraron mas de 20 articulos "Grandma's Boysenberry Spread"
en un solo pedido. */
 
 SELECT order_id AS lista_pedidos, customer_id AS id_cliente
 FROM orders
 WHERE order_id IN (SELECT order_id
					FROM order_details
					WHERE product_id IN (SELECT product_id
										 FROM products
										 WHERE product_id = 6)
					AND quantity > 20);
													
/* 4 */
/* Extraed los 10 productos mas caros */ 
 
SELECT product_id AS id_producto, product_name AS producto, unit_price AS precio
FROM products
WHERE unit_price > ANY (SELECT unit_price 
						FROM products)
ORDER BY unit_price DESC
LIMIT 10;
 
/* 5 BONUS */
/* Extraed cuál es el producto que más ha sido comprado y la cantidad que se compró. */

/* SELECT product_id AS id, product_name AS nombre_producto -- cantidad
 FROM products
 WHERE product_id IN (SELECT product_id
						FROM order_details
                        GROUP BY product_id);
                       -- HAVING MAX(quantity)); */
                        
 