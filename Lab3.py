import psycopg2

class Queries():
	
	def q1(self):
		return """
		CREATE TABLE singha_customers_accounts(
			id SERIAL PRIMARY KEY,
			first_name VARCHAR(20),
			last_name VARCHAR(20),
			bank_account_number VARCHAR(30),
			paypal_email VARCHAR(40),
			venmo_email VARCHAR(40),
			created_at DATE
		);

		CREATE TABLE singha_stocks(
			id SERIAL PRIMARY KEY,
			symbol CHAR(3),
			price REAL,
			last_updated_at DATE
		);

		INSERT INTO singha_customers_accounts 
		(first_name, last_name, bank_account_number, paypal_email, venmo_email, created_at) 
		VALUES
			('anik', 'singha', '0000', 'anik.singha68@myhunter.cuny.edu', 'anik.singha68@myhunter.cuny.edu', '2021-10-05'),
			('Jack', 'Singer', '0001', 'jacksinger@gmail.com', 'jacksinger@gmail.com', '2021-09-04'),
			('Nick', 'Smith', '0002', 'nicksmith@yahoo.com', 'nicksmith@yahoo.com', '2021-04-11'),
			('Tina', 'Smith', '0003', 'tinasmith@gmail.com', 'tinasmith@gmail.com', '2021-06-14'),
			('Jona', 'Davis', '0004', 'jonadavis@outlook.com', 'jonadavis@outlook.com', '2021-01-01'),
			('Joe', 'Jonas', '0005', 'joejonas@yahoo.com', 'joejonas@yahoo.com', '2022-02-03'),
			('Dace', 'Goggins', '0006', 'dacegoggins@yahoo.com', 'dacegoggins@yahoo.com', '2021-07-04'),
			('Alvin', 'Lam', '0007', 'alvinlam@gmail.com', 'alvinlam@gmail.com', '2021-03-03'),
			('Novin', 'Tang', '0008', 'novintang@gmail.com', 'novintang@gmail.com', '2021-07-08'),
			('No', 'Clue', '0009', 'noclue@yahoo.com', 'noclue@yahoo.com', '2021-09-10');

		INSERT INTO singha_stocks 
		(symbol, price, last_updated_at)
		VALUES
			('$#@', 1000, '2021-01-14'),
			('$$#', 1450, '2021-07-03'),
			('@#', 1700, '2022-02-07'),
			('$@$', 950, '2021-09-10'),
			('$$$', 750, '2021-01-01');
	"""

	def q2(self):
		return """
		SELECT first_name, last_name
		FROM singha_customers_accounts
		WHERE created_at::TEXT ~'-[0,1][7-9]|0-';
	"""

	def q3(self):
		return """
		SELECT symbol
		FROM singha_stocks
		WHERE last_updated_at > '2016-01-01' AND last_updated_at < '2026-01-01';
	"""

	def q4(self):
		return """
		SELECT SUM(price) AS "total market price",
		MAX(price) AS "highest priced stock",
		MIN(price) AS "lowest price stock",
		COUNT(last_updated_at)
		From singha_stocks
		WHERE last_updated_at = '2021-09-10';
	"""

	def q5(self):
		return """
		SELECT symbol,
		CASE
			WHEN price >= 3557.0 THEN 'SELL'
			WHEN price < 3557.0 THEN 'BUY'
		END AS "Action"
		FROM singha_stocks;
	"""

	def q6(self):
		return """
		SELECT first_name, 
		last_name,
		CASE
			When paypal_email IS NOT NULL then paypal_email
			WHEN paypal_email IS NULL THEN bank_account_number
			WHEN bank_account_number IS NULL THEN venmo_email
			WHEN venmo_email IS NULL THEN NULL
		END AS "Payment method"
		FROM singha_customers_accounts
		WHERE first_name != 'anik';
	"""
