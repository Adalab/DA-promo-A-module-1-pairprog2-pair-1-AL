USE Northwind;

-- 1. Extraed los pedidos con el máximo "OrderDate" para cada empleado.
-- Nuestro jefe quiere saber la fecha de los pedidos más recientes que ha 
-- gestionado cada empleado. Para eso nos pide que lo hagamos con una query correlacionada.

SELECT order_date, employee_id
FROM orders AS or1
WHERE order_date = (SELECT MAX(order_date)
					FROM orders AS or2
                    WHERE or1.employee_id = or2.employee_id
                    GROUP BY employee_id);

-- 2.Extraed el precio unitario (UnitPrice) de cada producto vendido.
-- Supongamos que ahora nuestro jefe quiere un informe de los productos 
-- más vendidos y su precio unitario. De nuevo lo tendréis que hacer con queries correlacionadas.


/* 3. Ciudades que empiezan con "A" o "B"
Por un extraño motivo, nuestro jefe quiere que le devolvamos una tabla con aquelas compañias 
que están afincadas en ciudades que empiezan por "A" o "B". 
Necesita que le devolvamos la ciudad, el nombre de la compañia y el nombre de contacto.*/

SELECT city, company_name, contact_name
FROM customers
WHERE city LIKE 'A%' OR 'B%';

/* 4. Número de pedidos que han hecho en las ciudades que empiezan con L
En este caso, nuestro objetivo es devolver los mismos campos que 
en la query anterior el número de total de pedidos que han hecho todas las ciudades que empiezan por "L".*/

SELECT city, company_name, contact_name, orders.order_id
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
WHERE city LIKE 'L%';

/*Todos los clientes cuyo "ContactTitle" no incluya "Sales".
Nuestro objetivo es extraer los clientes que no tienen el contacto "Sales" en su "ContactTitle". 
Extraer el nombre de contacto, su posisión (ContactTitle) y el nombre de la compañia.*/

SELECT contact_name, contact_title, company_name
FROM customers
WHERE contact_title NOT LIKE 'S%';

/* 6. Todos los clientes que no tengan una "A" en segunda posición en su nombre.
Devolved unicamente el nombre de contacto.*/

SELECT contact_name
FROM customers
WHERE contact_name NOT LIKE '_a%';
