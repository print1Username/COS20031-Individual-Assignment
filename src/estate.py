import sqlite3

connection = sqlite3.connect( 'database/estate.db', check_same_thread = False )
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


def create_estate():
	cursor.execute( 'DROP TABLE IF EXISTS Estate_Table' )
	cursor.execute(
		'''
				CREATE TABLE Estate_Table (
				Estate_ID INT NOT NULL PRIMARY KEY,
				Estate_Name VARCHAR(32) NOT NULL,
				Estate_Description VARCHAR(255) NULL,
				Estate_Price INT NOT NULL);
			'''
		)


def database_estate():
	cursor.execute( 'SELECT * FROM Estate_Table' )
	estate = cursor.fetchall()
	return estate


def add_estate(estate_id, estate_name, estate_description, estate_price):
	if estate_id is not None and estate_name is not None and estate_price is not None:
		cursor.execute( f'INSERT INTO Estate_Table VALUES ({estate_id}, "{estate_name}", "{estate_description}", {estate_price});' )
		connection.commit()
		return True
	else:
		return False


def search_estate(estate_id):
	if estate_id is not '':
		cursor.execute( f'SELECT * FROM Estate_Table WHERE Estate_ID = {estate_id}' )
	else:
		cursor.execute( 'SELECT * FROM Estate_Table' )

	estate = cursor.fetchall()
	return estate


if __name__ == '__main__':
	create_estate()
