from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to handle cross-origin requests
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Predefined FAQ dictionary
faq_dict = {
    "what is your name": "I am an AI chatbot.",
    "how can I contact support": "You can email support@example.com.",
    "what services do you provide": "We offer AI-powered solutions including chatbots and translation tools.",
}

@app.route("/chat", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("user_input", "").lower()

    # Tokenize and preprocess user input
    tokens = word_tokenize(user_input)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stopwords.words('english')]

    # Check if any FAQ question matches
    for question, answer in faq_dict.items():
        if all(word in question.split() for word in tokens):
            return jsonify({"response": answer})

    # Default response if no match
    return jsonify({"response": "I'm sorry, I don't have an answer for that."})

if __name__ == "__main__":
    # Run the app using Gunicorn for production
    app.run(host='0.0.0.0', port=5000, debug=False)
