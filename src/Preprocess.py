import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Function to preprocess text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove URLs (assuming URLs are prefixed with "http" or "https")
    text = re.sub(r'http\S+', '', text)

    # Remove special characters, symbols, and punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Join tokens back into a string
    cleaned_text = ' '.join(tokens)

    return cleaned_text

# Read data from a CSV file
def preprocess_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    # Apply preprocessing to the 'text' column
    df['cleaned_text'] = df['text'].apply(preprocess_text)

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(output_csv, index=False)

# Example usage
if __name__ == "__main__":
    input_csv = "input_data.csv"   # Replace with your CSV file
    output_csv = "cleaned_data.csv"   # Replace with your desired output CSV file

    preprocess_csv(input_csv, output_csv)

