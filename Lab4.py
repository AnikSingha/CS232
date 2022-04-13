import psycopg2

class Queries():
	
	def q1(self):
		return """
		CREATE TABLE singha_customers(
			id SERIAL PRIMARY KEY,
			first_name VARCHAR(20),
			last_name VARCHAR(20),
			email VARCHAR(40)
		);

		CREATE TABLE singha_items(
			id SERIAL PRIMARY KEY,
			name VARCHAR(20),
			price REAL
		);

		CREATE TABLE singha_orders(
			customer_id INTEGER REFERENCES singha_customers(id),
			item_id INTEGER REFERENCES singha_items(id),
			purchase_date DATE
		);

		INSERT INTO singha_customers 
		(first_name, last_name, email) 
		VALUES
			('anik', 'singha', 'anik.singha68@myhunter.cuny.edu'),
			('Jack', 'Singer','jacksinger@gmail.com'),
			('Nick', 'Smith', 'nicksmith@yahoo.com'),
			('Tina', 'Smith', 'tinasmith@gmail.com'),
			('Jona', 'Davis', 'jonadavis@outlook.com'),
			('Joe', 'Jonas', 'joejonas@yahoo.com'),
			('Dace', 'Goggins', 'dacegoggins@yahoo.com'),
			('Alvin', 'Lam', 'alvinlam@gmail.com'),
			('Novin', 'Tang', 'novintang@gmail.com'),
			('No', 'Clue', 'noclue@yahoo.com');

		INSERT INTO singha_items
		(name, price)
		VALUES
			('Bag', 15),
			('TV', 750),
			('Laptop', 1400),
			('Phone', 1200),
			('Mouse', 55),
			('Calculator', 70),
			('Headphones', 200),
			('Ear buds', 150),
			('Xbox', 299),
			('PS5', 499);

		INSERT INTO singha_orders
		(customer_id, item_id, purchase_date)
		VALUES	
			(1, 1, '2021-01-14'),
			(2, 2, '2021-07-03'),
			(3, 3, '2022-02-07'),
			(4, 4, '2021-09-10'),
			(5, 5, '2021-01-01'),
			(6, 6, '2019-04-16'),
			(7, 7, '2021-07-14'),
			(8, 8, '2021-09-01'),
			(9, 9, '2021-10-13'),
			(10, 10, '2021-05-17'),
			(1, 1, '2021-08-09'),
			(2, 2, '2021-02-12'),
			(3, 3, '2021-05-18'),
			(4, 4, '2021-11-16'),
			(5, 5, '2021-12-02'),
			(6, 6, '2021-04-09'),
			(7, 7, '2021-08-14'),
			(8, 8, '2021-03-19'),
			(9, 9, '2021-06-24'),
			(10, 10, '2021-07-26');
	"""

	def q2(self):
		return """
		SELECT singha_items.name
		FROM singha_items, singha_orders
		WHERE singha_items.id = singha_orders.item_id AND singha_orders.purchase_date = (
			SELECT MIN(purchase_date)
			FROM singha_orders
		);
	"""

	def q3(self):
		return """
		SELECT item_id, COUNT(item_id)
		FROM singha_orders
		WHERE item_id <= 6
		GROUP BY item_id;
	"""

	def q4(self):
		return """
		SELECT singha_items.name
		FROM singha_orders, singha_items
		GROUP BY singha_items.name
		HAVING COUNT(singha_orders.item_id) < 67;
	"""

	def q5(self):
		return """
		SELECT email
		FROM singha_customers, singha_orders
		WHERE singha_orders.customer_id = (
			SELECT COUNT(customer_id)
			FROM singha_orders
			GROUP BY customer_id
			LIMIT 1
		)
		GROUP by email;

	"""

	def q6(self):
		return """
		SELECT * FROM singha_items;
	"""
