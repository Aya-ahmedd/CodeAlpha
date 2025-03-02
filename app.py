from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend access

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLP tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Predefined FAQ dictionary
faq_dict = {
    "what is your name": "I am an AI FAQ chatbot.",
    "how can i contact support": "You can email support@example.com.",
    "what services do you provide": "We offer AI-powered solutions including chatbots and automation.",
    "where are you located": "We are a remote-based company operating worldwide.",
    "how does your pricing work": "Pricing is based on a subscription model. Contact us for details.",
}

def preprocess_text(text):
    """Tokenize, remove stopwords, and lemmatize input text."""
    tokens = word_tokenize(text.lower())  # Convert to lowercase and tokenize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha() and word not in stop_words]
    return tokens

@app.route("/chat", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("user_input", "").lower()
    processed_tokens = preprocess_text(user_input)

    # Match input to FAQ
    for question, answer in faq_dict.items():
        question_tokens = preprocess_text(question)
        if set(processed_tokens).issubset(set(question_tokens)):  # Partial match
            return jsonify({"response": answer})

    return jsonify({"response": "I'm sorry, I don't have an answer for that."})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
