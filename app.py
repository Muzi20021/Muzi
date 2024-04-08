from flask import Flask, jsonify
import csv

app = Flask(__name__)


def read_csv(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


movies_data = read_csv('movies.csv')
links_data = read_csv('links.csv')
ratings_data = read_csv('ratings.csv')
tags_data = read_csv('tags.csv')

class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres

    def serialize(self):
        return {
            'id': self.movieId,
            'title': self.title,
            'genres': self.genres,
        }


@app.route('/')
def hello_world():
    return jsonify({'hello': 'world'})


@app.route('/movies')
def get_movies():
    serialized_movies = [Movie(movie['movieId'], movie['title'], movie['genres']).serialize() for movie in movies_data]
    return jsonify(serialized_movies)


@app.route('/links')
def get_links():
    pass

@app.route('/ratings')
def get_ratings():
    pass

@app.route('/tags')
def get_tags():
    pass

if __name__ == '__main__':
    app.run(debug=True)
