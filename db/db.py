import psycopg2

class PostgresSQLConnection:
    def __init__(self, db_params):
        # refactor to load from .env file
        self.db_params = {
        'dbname': 'animals',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
        'port': '5432'
    }
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.db_params)
        except (Exception, psycopg2.Error) as error:
            print("Failed to connect to the database:", error)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, data=None):
        try:
            cursor = self.connection.cursor()
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            return cursor
        except (Exception, psycopg2.Error) as error:
            print("Error when running a query:", error)
            return None

    def add_animal(self, data):
        query = "INSERT INTO animals VALUES (...)"
        cursor = self.execute_query(insert_query, data)
        self.connection.commit()
        cursor.close()

    def get_all_animals(self):
        query = "SELECT * FROM animals"
        cursor = self.execute_query(query)
        results = cursor.fetchall()
        cursor.close()
        return results