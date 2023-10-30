import nltk
nltk.download('punkt')  # Download the Punkt tokenizer data (if you haven't already)

from nltk.tokenize import word_tokenize

# Sample text
text = "NLTK is a leading platform for building Python programs to work with human language data."

# Tokenize the text
tokens = word_tokenize(text)

# Display the tokens
print(tokens)
