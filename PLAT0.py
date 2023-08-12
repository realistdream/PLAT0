import openai
import random
from flask import Flask, render_template, request

# Set up the OpenAI API key
openai.api_key = "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"

# Define the OCEAN personality traits and their associated prompts
personality_traits = {
    "Openness": "Tell me about a new idea that excites you.",
    "Conscientiousness": "What are your long-term goals and how are you working towards them?",
    "Extraversion": "Describe your ideal social situation.",
    "Agreeableness": "What is something kind you have done for someone recently?",
    "Neuroticism": "How do you cope with stress or difficult situations?"
}

# Generate random OCEAN traits for the chatbot
chatbot_traits = {trait: random.randint(1, 7) for trait in personality_traits.keys()}

# Function to generate a response from the GPT-3 chatbot based on the user input
def generate_response(user_input):
    # Generate the response using the GPT-3 API
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )
    
    # Extract the generated response from the API output
    return response.choices[0].text.strip()

# Create the Flask web application
app = Flask(__name__)

# Define the home page route
@app.route('/')
def index():
    return render_template('index2.html')

# Define the chatbot response route
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = generate_response(user_input)
    return {'bot_response': bot_response}

# Run the application
if __name__ == '__main__':
   app.run(host='192.168.1.161', port=5000)
