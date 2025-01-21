import requests
import json

class Movie:
    def __init__(self, title, year, genre, director):
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director

    def __str__(self):
        return f"Title: {self.title}, Year: {self.year}, Genre: {self.genre}, Director: {self.director}"

def fetch_movies(url):
    """Fetch the movies.json data from the given URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Parse JSON response
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def create_movie_list(data):
    """Create a list of Movie objects from the JSON data."""
    movie_list = []
    for item in data:
        # Create Movie objects from JSON fields
        movie = Movie(
            title=item.get("title"),
            year=item.get("year"),
            genre=item.get("genre"),
            director=item.get("director")
        )
        movie_list.append(movie)
    return movie_list

# Main Code
if __name__ == "__main__":
    # URL to fetch the movies.json file
    url = "https://example.com/movies.json"  # Replace with the actual URL

    # Fetch data
    movies_data = fetch_movies(url)

    if movies_data:
        # Create a list of Movie objects
        movie_list = create_movie_list(movies_data)

        # Print each Movie object
        for movie in movie_list:
            print(movie)
