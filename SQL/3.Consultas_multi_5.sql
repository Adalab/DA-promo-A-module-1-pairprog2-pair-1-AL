/*  Múltiples tablas 5 | PAIR 1: Alicia y Lara | __/04 */

USE Northwind;

-- 1. Extraed los pedidos con el máximo "OrderDate" para cada empleado.

SELECT employee_id, order_date
FROM orders AS or1
WHERE order_date = (SELECT MAX(order_date)
					FROM orders AS or2
                    WHERE or1.employee_id = or2.employee_id
                    GROUP BY employee_id)
ORDER BY employee_id;


-- 2.Extraed el precio unitario (UnitPrice) de cada producto vendido.

SELECT product_id, unit_price
FROM order_details
WHERE product_id IN (SELECT product_id
					FROM order_details
                    GROUP BY product_id)
ORDER BY quantity DESC;


/* 3. Ciudades que empiezan con "A" o "B"
Ciudad, el nombre de la compañia y el nombre de contacto.*/

SELECT city AS ciudad, company_name AS compania, contact_name AS contacto
FROM customers
WHERE city LIKE 'A%' 
OR city LIKE 'B%';

/* 4. Número de pedidos que han hecho en las ciudades que empiezan con L */

SELECT city AS ciudad, company_name AS empresa, contact_name AS persona_contacto, COUNT(orders.order_id) AS numero_pedidos
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY city, company_name, contact_name
HAVING city LIKE 'L%';


/* 5 - Todos los clientes cuyo "ContactTitle" no incluya "Sales".
Extraer el nombre de contacto, su posisión (ContactTitle) y el nombre de la compañia.*/
SELECT contact_name, contact_title, company_name
FROM customers
WHERE contact_title NOT LIKE 'Sales%';


/* 6. Todos los clientes que no tengan una "A" en segunda posición en su nombre.
Devolved unicamente el nombre de contacto.*/
SELECT contact_name
FROM customers
WHERE contact_name NOT LIKE '_a%';