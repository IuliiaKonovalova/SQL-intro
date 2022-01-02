import psycopg2

# connect to chinook db
connection = psycopg2.connect(database="chinook")

# a cursor(set/list) object of the db
cursor = connection.cursor()

# Fetch the results(multiple)
results = cursor.fetchall()
