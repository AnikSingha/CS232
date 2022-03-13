import psycopg2

class Queries():
	
	def q1(self):
		return """
		CREATE TABLE singha_employees(
			id SERIAL PRIMARY KEY,
			first_name VARCHAR(20),
			last_name VARCHAR(20),
			email VARCHAR(40),
			age INTEGER
		);
		CREATE TABLE singha_salaries(
			employee_id SERIAL REFERENCES singha_employees(id),
			salary REAL
		);
	"""

	def q2(self):
		return """
		INSERT INTO singha_employees 
		(first_name, last_name, email, age) 
		VALUES
			('anik', 'singha', 'anik.singha68@myhunter.cuny.edu', 18),
			('Jack', 'Singer', 'jacksinger@gmail.com', 27),
			('Nick', 'Smith', 'nicksmith@yahoo.com', 19),
			('Tina', 'Smith', 'tinasmith@gmail.com', 24),
			('Jona', 'Davis', 'jonadavis@outlook.com', 36),
			('Joe', 'Jonas', 'joejonas@yahoo.com', 29),
			('Dace', 'Goggins', 'dacegoggins@yahoo.com', 43),
			('Alvin', 'Lam', 'alvinlam@gmail.com', 24),
			('Novin', 'Tang', 'novintang@gmail.com', 18),
			('No', 'Clue', 'noclue@yahoo.com', 44),
			('Jake', 'Krants', 'jakekrantz@gmail.com', 26),
			('Jimmy', 'Donalds', 'jimmydonalds@hotmail.com', 22),
			('Chris', 'Pine', 'chrispine@gmail.com', 51),
			('Pratt', 'Stevens', 'prattstevens@yahoo.com', 37),
			('Steven', 'Universe', 'stevenuniverse@gmail.com', 19),
			('Chris', 'Evans', 'chrisevans@outlook.com', 38),
			('Robert', 'Downey', 'robertdowney@gmail.com', 53),
			('Mark', 'Ruffalo', 'markruffalo@gmail.com', 54),
			('Tom', 'Holland', 'tomholland@yahoo.com', 25),
			('Steven', 'Strange', 'stevenstrange@hotmail.com', 35),
			('Bennedict', 'Cumberbatch', 'bennedictcumberbatch@gmail.com', 38);


		INSERT INTO singha_salaries 
		(salary) 
		VALUES
			(154500),
			(54000),
			(67500),
			(84500),
			(47000),
			(93200),
			(71300),
			(44000),
			(56000),
			(63500),
			(46800),
			(340000),
			(125000),
			(84000),
			(54500),
			(37000),
			(225000),
			(78000),
			(110000),
			(93500),
			(48000);
	"""

	def q3(self):
		return """
		SELECT DISTINCT employee_id
		FROM singha_salaries;
	"""

	def q4(self):
		return """
		SELECT first_name, last_name
		FROM singha_employees
		WHERE age = 18;
	"""

	def q5(self):
		return """
		SELECT salary + 8 AS new_salaries 
		FROM singha_salaries
	"""

	def q6(self):
		return """
		SELECT id FROM singha_employees
		WHERE (first_name IS NULL 
		AND email = 'anik.singha68@myhunter.cuny.edu') OR
		(last_name IS NULL
		AND email = 'anik.singha68@myhunter.cuny.edu');
	"""

	def q7(self):
		return """
		SELECT employee_id
		FROM singha_salaries
		WHERE salary < 37807
		LIMIT 13;
	"""