import psycopg2

class Queries():
	
	def q1(self):
		return """
		CREATE TABLE students (
			student_id INTEGER PRIMARY KEY,
			first_name VARCHAR(20),
			last_name VARCHAR(20),
			gpa REAL
		);
	"""

	def q2(self):
		return """
		CREATE TABLE homeworks (
			homework_id INTEGER PRIMARY KEY,
			student_id INTEGER REFERENCES students(student_id),
			grade INTEGER 
		);
	"""

	def q3(self):
		return """
		INSERT INTO students (student_id, first_name, last_name, gpa) VALUES
			(0, 'Anik', 'Singha', 3.7),
			(1, 'Jack', 'Singer', 3.45),
			(2, 'Nick', 'Smith', 3.73),
			(3, 'Tina', 'Smith', 3.8),
			(4, 'Jona', 'Davis', 3.94),
			(5, 'Joe', 'Jonas', 2.4),
			(6, 'Dace', 'Goggins', 3.0),
			(7, 'Alvin', 'Lam', 3.12),
			(8, 'Novin', 'Tang', 3.94),
			(9, 'No', 'Clue', 2.2),
			(10, 'Jake', 'Krants', 3.75),
			(11, 'Jimmy', 'Donalds', 3.4),
			(12, 'Chris', 'Pine', 2.8),
			(13, 'Pratt', 'Stevens', 2.7),
			(14, 'Steven', 'Universe', 1.85),
			(15, 'Chris', 'Evans', 3.75),
			(16, 'Robert', 'Downey', 4.0),
			(17, 'Mark', 'Ruffalo', 3.4),
			(18, 'Tom', 'Holland', 3.84),
			(19, 'Steven', 'Strange', 3.54),
			(20, 'Bennedict', 'Cumberbatch', 3.73);
	"""

	def q4(self):
		return """
		INSERT INTO homeworks (homework_id, student_id, grade) VALUES
			(0, 0, 100),
			(1, 1, 84),
			(2, 2, 94),
			(3, 3, 93),
			(4, 4, 15),
			(5, 5, 21),
			(6, 6, 83),
			(7, 7, 74),
			(8, 8, 68),
			(9, 9, 75),
			(10, 10, 54),
			(11, 11, 43),
			(12, 12, 91),
			(13, 13, 15),
			(14, 14, 88),
			(15, 15, 75),
			(16, 16, 75),
			(17, 17, 85),
			(18, 18, 93),
			(19, 19, 100),
			(20, 20, 100);
	"""

	def q5(self):
		return """
		UPDATE homeworks
		SET grade = 25
		WHERE grade < 25;
	"""

	def q6(self):
		return """
		DELETE FROM homeworks
		WHERE homework_id = 12;
	"""

	def q7(self):
		return """
		DROP TABLE students, homeworks;
	"""
