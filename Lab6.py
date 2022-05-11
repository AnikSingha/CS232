import psycopg2

class Queries():
	
	def q1(self):
		return """
		CREATE TABLE singha_users(
			id SERIAL PRIMARY KEY,
			username VARCHAR(40),
			password VARCHAR(40),
			email VARCHAR(60)
		);

		CREATE TABLE singha_posts(
			id SERIAL PRIMARY KEY,
			user_id INTEGER REFERENCES singha_users(id),
			content TEXT
		);

		INSERT INTO singha_users
		(username, password, email)
		VALUES
			('aniksingha', 'singhaanik', 'anik.singha68@myhunter.cuny.edu'),
			('Jack', 'Singer', 'jacksinger@gmail.com'),
			('Nick', 'Smith', 'nicksmith@yahoo.com'),
			('Tina', 'Smith', 'tinasmith@gmail.com'),
			('Jona', 'Davis', 'jonadavis@outlook.com'),
			('Joe', 'Jonas', 'joejonas@yahoo.com'),
			('Dace', 'Goggins', 'dacegoggins@yahoo.com'),
			('Alvin', 'Lam', 'alvinlam@gmail.com'),
			('Novin', 'Tang', 'novintang@gmail.com'),
			('No', 'Clue', 'noclue@yahoo.com'),
			('Jake', 'Krants', 'jakekrantz@gmail.com'),
			('Jimmy', 'Donalds', 'jimmydonalds@hotmail.com'),
			('Chris', 'Pine', 'chrispine@gmail.com'),
			('Pratt', 'Stevens', 'prattstevens@yahoo.com'),
			('Steven', 'Universe', 'stevenuniverse@gmail.com'),
			('Chris', 'Evans', 'chrisevans@outlook.com'),
			('Robert', 'Downey', 'robertdowney@gmail.com'),
			('Mark', 'Ruffalo', 'markruffalo@gmail.com'),
			('Tom', 'Holland', 'tomholland@yahoo.com'),
			('Steven', 'Strange', 'stevenstrange@hotmail.com'),
			('Bennedict', 'Cumberbatch', 'bennedictcumberbatch@gmail.com');

		INSERT INTO singha_posts
		(user_id, content)
		VALUES
			(1, 'hello'),
			(2, 'my'),
			(3, 'friend'),
			(4, 'how'),
			(5, 'have'),
			(6, 'you'),
			(7, 'been'),
			(8, 'these'),
			(9, 'past'),
			(10, 'couple'),
			(11, 'years.'),
			(12, 'It has been'),
			(13, 'a long'),
			(14, 'time'),
			(15, 'since we'),
			(16, 'last'),
			(17, 'spoke'),
			(18, 'I hope'),
			(19, 'you have'),
			(20, 'been well');
	"""

	def q2(self):
		return """
		SELECT username, AVG(LENGTH(content))
		FROM singha_users
		INNER JOIN singha_posts
		ON singha_users.id = singha_posts.user_id
		WHERE username != 'aniksingha'
		GROUP BY username;
	"""

	def q3(self):
		return """
		
	"""

	def q4(self):
		return """
		SELECT username, email
		FROM singha_users
		WHERE LENGTH(username) = 10 AND
		STRPOS(username,')
	"""

	def q5(self):
		return """
		
	"""

	def q6(self):
		return """
		
	"""

