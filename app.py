import os
import string
from collections import Counter

def get_most_common_words(file_path, top_n=5):
    """
    Reads a text file and returns the top N most common words.

    Args:
        file_path (str): Path to the text file.
        top_n (int): Number of top common words to return.

    Returns:
        list: A list of tuples containing words and their counts.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()

    # Count word frequencies
    word_counts = Counter(words)

    # Return the top N most common words
    return word_counts.most_common(top_n)

def main():
    print("Welcome to the Word Frequency Analyzer!")
    file_path = input("Enter the path to your text file: ").strip()

    try:
        top_words = get_most_common_words(file_path)
        print("\nTop 5 Most Common Words:")
        for word, count in top_words:
            print(f"{word}: {count} occurrences")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
