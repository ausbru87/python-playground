import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    endpoint = "https://tastedive.com/api/similar"
    params = {
        'type': 'movies',
        'limit': '5',
        'q': movie
    }
    resp = requests_with_caching.get(endpoint, params)
    return resp.json()

def extract_movie_titles(movie_json):
    return [movie['Name'] for movie in movie_json['Similar']['Results']]

def get_related_titles(in_movie_lst):
    final_lst = []
    related_movies = [extract_movie_titles(get_movies_from_tastedive(in_movie)) for in_movie in in_movie_lst]
    for movie_lst in related_movies:
        for movie in movie_lst:
            if movie not in final_lst:
                final_lst.append(movie)
    return final_lst

def get_movie_data(movie):
    endpoint = "http://www.omdbapi.com/"
    params = {
        't': movie,
        'r': 'json'
    }
    resp = requests_with_caching.get(endpoint, params)
    return resp.json()

def get_movie_rating(movie_json):
    for rating_sites in movie_json['Ratings']:
        if rating_sites['Source'] == 'Rotten Tomatoes':
            return int(rating_sites['Value'].rstrip('%'))
    return 0

def get_sorted_recommendations(movie_lst):
    related_titles = get_related_titles(movie_lst)
    sorted_ratings_tup = sorted([(get_movie_rating(get_movie_data(title)), title) for title in related_titles], reverse=True)
    final_sorted_titles = [title for rating, title in sorted_ratings_tup]
    return final_sorted_titles
