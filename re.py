import random

# Sample data for books and movies
books_data = {
    'Fantasy': ['Harry Potter and the Sorcerer\'s Stone', 'The Hobbit', 'A Game of Thrones', 'Percy Jackson and the Lightning Thief'],
    'Mystery': ['The Da Vinci Code', 'Gone Girl', 'The Girl with the Dragon Tattoo', 'Sherlock Holmes'],
    'Romance': ['Pride and Prejudice', 'The Notebook', 'Me Before You', 'Twilight']
}

movies_data = {
    'Action': ['Inception', 'The Dark Knight', 'Gladiator', 'Mad Max: Fury Road'],
    'Comedy': ['Superbad', 'The Hangover', 'Anchorman', 'Dumb and Dumber'],
    'Drama': ['The Shawshank Redemption', 'Forrest Gump', 'The Godfather', 'Schindler\'s List']
}

def recommend_book(genre):
    if genre in books_data:
        return random.choice(books_data[genre])
    else:
        return "Sorry, we don't have recommendations for that genre."

def recommend_movie(genre):
    if genre in movies_data:
        return random.choice(movies_data[genre])
    else:
        return "Sorry, we don't have recommendations for that genre."

def main():
    print("Welcome to Recommendation System!")
    print("Please choose your preferred genre for books and movies from the following options:")
    print("Books genres:", list(books_data.keys()))
    print("Movies genres:", list(movies_data.keys()))
    
    user_book_genre = input("Enter your preferred book genre: ").capitalize()
    user_movie_genre = input("Enter your preferred movie genre: ").capitalize()
    
    recommended_book = recommend_book(user_book_genre)
    recommended_movie = recommend_movie(user_movie_genre)
    
    print(f"We recommend you read: {recommended_book}")
    print(f"We recommend you watch: {recommended_movie}")

if __name__ == "__main__":
    main()
