import psycopg2

class Queries():
	
	def q1(self):
		return """
		CREATE TABLE singha_employees(
			id INTEGER PRIMARY KEY,
			first_name VARCHAR(20),
			last_name VARCHAR(20),
			email VARCHAR(40),
			age INTEGER
		);

		CREATE TABLE singha_salaries(
			employee_id INTEGER REFERENCES singha_employees(id),
			salary REAL
		);
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
			(2, 67500),
			(3, 84500),
			(4, 47000),
			(5, 93200),
			(6, 71300),
			(7, 44000),
			(8, 56000),
			(9, 63500),
			(10, 46800),
			(11, 340000),
			(12, 125000),
			(13, 84000),
			(14, 54500),
			(15, 37000),
			(16, 225000),
			(17, 78000),
			(18, 110000),
			(19, 93500),
			(20, 48000);
	"""

	def q3(self):
		return """
		SELECT DISTINCT employee_id
		FROM singha_salaries;
	"""

	def q4(self):
		return """
		SELECT DISTINCT employee_id
		FROM singha_salaries;
	"""

	def q5(self):
		return """
		SELECT employee_id
		FROM singha_salaries;
		
	"""

	def q6(self):
		return """
		SELECT DISTINCT employee_id
		FROM singha_employees;
		
	"""

	def q7(self):
		return """
		SELECT * FROM singha_employees;
		
	"""

