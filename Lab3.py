import psycopg2

class Queries():
	
	def q1(self):
		return """
		CREATE TABLE singha_customers_accounts(
			id INTEGER PRIMARY KEY,
			first_name VARCHAR(20),
			last_name VARCHAR(20),
			bank_account_number VARCHAR(30),
			paypal_email VARCHAR(40),
			venmo_email VARCHAR(40),
			created_at DATE
		);

		CREATE TABLE singha_stocks(
			id INTEGER PRIMARY KEY,
			symbol CHAR(3),
			price REAL,
			last_updated_at DATE
		);

		INSERT INTO singha_customers_accounts 
		(id, first_name, last_name, bank_account_number, paypal_email, venmo_email, created_at) 
		VALUES
			(0, 'anik', 'singha', '0000', 'anik.singha68@myhunter.cuny.edu', 'anik.singha68@myhunter.cuny.edu', '2021-10-05'),
			(1, 'Jack', 'Singer', '0001', 'jacksinger@gmail.com', 'jacksinger@gmail.com', '2021-09-04'),
			(2, 'Nick', 'Smith', '0002', 'nicksmith@yahoo.com', 'nicksmith@yahoo.com', '2021-04-11'),
			(3, 'Tina', 'Smith', '0003', 'tinasmith@gmail.com', 'tinasmith@gmail.com', '2021-06-14'),
			(4, 'Jona', 'Davis', '0004', 'jonadavis@outlook.com', 'jonadavis@outlook.com', '2021-01-01'),
			(5, 'Joe', 'Jonas', '0005', 'joejonas@yahoo.com', 'joejonas@yahoo.com', '2022-02-03'),
			(6, 'Dace', 'Goggins', '0006', 'dacegoggins@yahoo.com', 'dacegoggins@yahoo.com', '2021-07-04'),
			(7, 'Alvin', 'Lam', '0007', 'alvinlam@gmail.com', 'alvinlam@gmail.com', '2021-03-03'),
			(8, 'Novin', 'Tang', '0008', 'novintang@gmail.com', 'novintang@gmail.com', '2021-07-08'),
			(9, 'No', 'Clue', '0009', 'noclue@yahoo.com', 'noclue@yahoo.com', '2021-09-10');

		INSERT INTO singha_stocks 
		(id, symbol, price, last_updated_at)
		VALUES
			(0, '$#@', 1000, '2021-01-14'),
			(1, '$$#', 1450, '2021-07-03'),
			(2, '@#', 1700, '2022-02-07'),
			(3, '$@$', 950, '2021-09-10'),
			(4, '$$$', 750, '2021-01-01');
	"""

	def q2(self):
		return """
		INSERT INTO singha_employees 
		(id, first_name, last_name, email, age) 
		VALUES
			(0, 'anik', 'singha', 'anik.singha68@myhunter.cuny.edu', 18),
			(1, 'Jack', 'Singer', 'jacksinger@gmail.com', 27),
			(2, 'Nick', 'Smith', 'nicksmith@yahoo.com', 19),
			(3, 'Tina', 'Smith', 'tinasmith@gmail.com', 24),
			(4, 'Jona', 'Davis', 'jonadavis@outlook.com', 36),
			(5, 'Joe', 'Jonas', 'joejonas@yahoo.com', 29),
			(6, 'Dace', 'Goggins', 'dacegoggins@yahoo.com', 43),
			(7, 'Alvin', 'Lam', 'alvinlam@gmail.com', 24),
			(8, 'Novin', 'Tang', 'novintang@gmail.com', 18),
			(9, 'No', 'Clue', 'noclue@yahoo.com', 44),
			(10, 'Jake', 'Krants', 'jakekrantz@gmail.com', 26),
			(11, 'Jimmy', 'Donalds', 'jimmydonalds@hotmail.com', 22),
			(12, 'Chris', 'Pine', 'chrispine@gmail.com', 51),
			(13, 'Pratt', 'Stevens', 'prattstevens@yahoo.com', 37),
			(14, 'Steven', 'Universe', 'stevenuniverse@gmail.com', 19),
			(15, 'Chris', 'Evans', 'chrisevans@outlook.com', 38),
			(16, 'Robert', 'Downey', 'robertdowney@gmail.com', 53),
			(17, 'Mark', 'Ruffalo', 'markruffalo@gmail.com', 54),
			(18, 'Tom', 'Holland', 'tomholland@yahoo.com', 25),
			(19, 'Steven', 'Strange', 'stevenstrange@hotmail.com', 35),
			(20, 'Bennedict', 'Cumberbatch', 'bennedictcumberbatch@gmail.com', 38);

		INSERT INTO singha_salaries 
		(employee_id, salary) 
		VALUES
			(0, 154500),
			(1, 54000),
			(2, 25000),
			(3, 84500),
			(4, 47000),
			(5, 93200),
			(6, 71300),
			(7, 44000),
			(8, 56000),
			(9, 63500),
			(10, 15500),
			(11, 340000),
			(12, 125000),
			(13, 84000),
			(14, 54500),
			(15, 37000),
			(16, 225000),
			(17, 32000),
			(18, 110000),
			(19, 33000),
			(20, 24000);
	"""

	def q3(self):
		return """
		SELECT DISTINCT employee_id
		FROM singha_salaries;
	"""

	def q4(self):
		return """
		SELECT id
		FROM singha_employees
		WHERE id IS NOT NULL;
	"""

	def q5(self):
		return """
		SELECT salary + 8 
		AS new_salaries 
		FROM singha_salaries;
	"""

	def q6(self):
		return """
		SELECT *
		FROM singha_employees
		WHERE id IS NOT NULL;
		
	"""

	def q7(self):
		return """
		SELECT employee_id
		FROM singha_salaries
		WHERE salary < 16307
		LIMIT 13;
	"""