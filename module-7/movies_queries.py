import mysql.connector

# Database connection parameters
config = {
    'host': '127.0.0.1',
    'database': 'movies',
    'user': 'root',
    'password': r'WinterWinter6969(('
}

try:
    # Establish connection to the database
    connection = mysql.connector.connect(**config)
    
    if connection.is_connected():
        print('Connected to MySQL database')

    # Query 1: Select all fields for the studio table
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    print("Studio Table:")
    for studio in studios:
        print(studio)

    # Query 2: Select all fields for the genre table
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    print("\nGenre Table:")
    for genre in genres:
        print(genre)

    # Query 3: Select movie titles for movies with a run time of less than two hours
    cursor.execute("SELECT title FROM movies WHERE run_time < 120")
    short_movies = cursor.fetchall()
    print("\nMovie Titles with Run Time Less Than Two Hours:")
    for movie in short_movies:
        print(movie[0])

    # Query 4: Get a list of film titles and directors grouped by director
    cursor.execute("SELECT m.title, d.director FROM movies m JOIN director d ON m.director_id = d.id GROUP BY d.director")
    film_directors = cursor.fetchall()
    print("\nFilm Titles and Directors Grouped by Director:")
    for film_director in film_directors:
        print(film_director)

except mysql.connector.Error as e:
    print(f'Error connecting to MySQL database: {e}')

finally:
    # Close the connection when done
    if 'connection' in locals():
        connection.close()
        print('\nMySQL connection closed')

