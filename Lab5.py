
import psycopg2

class Queries():
	
	def q1(self):
		return """
		CREATE TABLE singha_accounts(
			id SERIAL PRIMARY KEY, 
			first_name VARCHAR(40), 
			last_name VARCHAR(40), 
			email VARCHAR(40)
		);

		CREATE TABLE singha_credit_cards(
			id SERIAL PRIMARY KEY, 
			account_id INTEGER REFERENCES singha_accounts(id), 
			card_limit REAL
		);

		CREATE TABLE singha_credit_card_transactions(
			id INTEGER, 
			card_id INTEGER REFERENCES singha_credit_cards(id), 
			amount REAL
		);

		INSERT INTO singha_accounts
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

		INSERT INTO singha_credit_cards
		(account_id, card_limit)
		VALUES
			(1,5000),
			(2,5000),
			(3,5000),
			(4,5000),
			(5,5000),
			(6,5000),
			(7,5000),
			(8,5000),
			(9,5000),
			(1,5000);
		
		INSERT INTO singha_credit_card_transactions
		(id, card_id, amount)
		VALUES
			(1,1,500),
			(2,2,400),
			(3,3,660),
			(4,4,200),
			(5,5,800),
			(6,6,700),
			(7,7,400),
			(8,8,300),
			(9,9,100),
			(3,3,600),
			(2,2,800),
			(1,1,200),
			(6,6,700),
			(4,4,900),
			(3,3,400),
			(6,6,600),
			(7,7,800),
			(8,8,200),
			(2,2,500),
			(9,9,600),
			(10,10,800);
	"""

	def q2(self):
		return """
		SELECT singha_accounts.last_name, singha_accounts.email
		FROM singha_accounts
		INNER JOIN singha_credit_cards
		ON singha_accounts.id = singha_credit_cards.account_id
		WHERE last_name != 'singha';
	"""

	def q3(self):
		return """
		SELECT card_id, COUNT(card_id)
		FROM singha_credit_card_transactions
		GROUP BY card_id;
	"""

	def q4(self):
		return """
		SELECT email, card_id, card_limit, amount
		FROM singha_accounts
		INNER JOIN singha_credit_cards
		ON singha_accounts.id = singha_credit_cards.account_id 
		INNER JOIN singha_credit_card_transactions
		ON singha_credit_cards.id = singha_credit_card_transactions.card_id
		WHERE last_name != 'singha';
	"""

	def q5(self):
		return """
		SELECT first_name, last_name, email
		FROM singha_accounts
		INNER JOIN singha_credit_cards
		ON singha_accounts.id = singha_credit_cards.account_id 
		WHERE singha_credit_cards.id NOT IN (
			SELECT card_id
			FROM singha_credit_card_transactions
		);
	"""