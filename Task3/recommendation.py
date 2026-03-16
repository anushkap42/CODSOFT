# Simple Movie Recommendation System

movies = {
    "Action": ["Mad Max", "John Wick", "Avengers"],
    "Comedy": ["The Mask", "Superbad", "Hangover"],
    "Romance": ["Titanic", "The Notebook", "La La Land"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"],
    "Horror": ["The Conjuring", "It", "A Quiet Place"]
}

print("Movie Recommendation System")
print("Available genres:")

for genre in movies:
    print("-", genre)

user_choice = input("\nEnter your favorite genre: ")

if user_choice in movies:
    print("\nRecommended movies for you:")
    for movie in movies[user_choice]:
        print("-", movie)
else:
    print("\nSorry, genre not found.")
