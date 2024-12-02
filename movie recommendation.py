import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie data
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Merge the datasets
movie_data = pd.merge(ratings, movies, on='movieId')

# Create a pivot table
user_movie_matrix = movie_data.pivot_table(index='userId', columns='title', values='rating')

# Fill missing values with 0
user_movie_matrix.fillna(0, inplace=True)

# Calculate cosine similarity
movie_similarity = cosine_similarity(user_movie_matrix.T)
movie_similarity_df = pd.DataFrame(movie_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)


# Function to recommend movies
def recommend_movies(movie_title, num_recommendations=5):
    if movie_title not in movie_similarity_df.columns:
        print(f"Movie '{movie_title}' not found in the dataset.")
        return

    similar_movies = movie_similarity_df[movie_title].sort_values(ascending=False)[1:num_recommendations + 1]
    return similar_movies


# Example usage
movie_title = 'Toy Story (1995)'
recommendations = recommend_movies(movie_title)
print(f"Movies similar to '{movie_title}':\n")
print(recommendations)
