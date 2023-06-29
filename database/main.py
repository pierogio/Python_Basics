import mysql.connector

def connection_database(host, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(3307)
    )
    return connection

def get_users(query, connection):
    return execute_query(query, connection)

def execute_query(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

if __name__ == '__main__':
    conn = connection_database("localhost", "root", "root", "gri")
    query = "SELECT * FROM users"
    results = get_users(query, conn)
    print(results)