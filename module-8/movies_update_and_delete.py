import mysql.connector

def display_records(cursor, label):
    try:
        cursor.execute("SELECT * FROM film")
        records = cursor.fetchall()
        
        print(f"-- {label} --")
        for record in records:
            print(record)
    
    except mysql.connector.Error as e:
        print(f"Error: {e}")

# Connect to the movies database
try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        database="movies",
        user="root",
        password="WinterWinter6969(("
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    cursor = connection.cursor()

    # Display all films
    display_records(cursor, "DISPLAYING FILMS")

    # Insert a new record
    insert_query = """
        INSERT INTO film (film_name, studio_id, genre_id, film_release, film_runtime, film_director)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    insert_values = ("Interstellar", 2, 3, "2014-11-07", 169, "Christopher Nolan")
    cursor.execute(insert_query, insert_values)
    connection.commit()
    print("New record inserted successfully")

    # Display all films after insertion
    display_records(cursor, "DISPLAYING FILMS")

    # Update film genre
    update_query = """
        UPDATE film
        SET genre_id = 1
        WHERE film_name = 'Alien'
    """
    cursor.execute(update_query)
    connection.commit()
    print("Updated genre for 'Alien' to Horror")

    # Display all films after update
    display_records(cursor, "DISPLAYING FILMS")

    # Delete the movie "Gladiator"
    delete_query = "DELETE FROM film WHERE film_name = 'Gladiator'"
    cursor.execute(delete_query)
    connection.commit()
    print("Deleted movie 'Gladiator'")

    # Display all films after deletion
    display_records(cursor, "DISPLAYING FILMS")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
