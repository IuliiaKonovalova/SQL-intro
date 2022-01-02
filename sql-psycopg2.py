import psycopg2


# connect to chinook db
connection = psycopg2.connect(database="chinook")

# a cursor(set/list) object of the db
cursor = connection.cursor()

cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Fetch the results(multiple)
results = cursor.fetchall()

# fetch sing result
#result = cursor.fetchone()

# close the connections
connection.close()

# print the results

for result in results:
    print(result)

