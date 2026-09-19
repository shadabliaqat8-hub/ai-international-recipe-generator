# 🍳 AI International Recipe Generator

Discover delicious recipes from around the world! Pick a cuisine, enter the ingredients you have, and get an AI-generated recipe inspired by that country's food.

## 🌐 Live Demo

**Try it here:** https://shadab-recipe-ai.streamlit.app

## ✨ Features

- 🌍 Choose from 10 cuisines: Pakistan, Italy, India, China, Japan, Mexico, Turkey, South Korea, Thailand and France
- 🥘 Enter the ingredients you already have at home
- 🍽️ Pick a meal type: Breakfast, Lunch, Dinner, Snack or Dessert
- 📊 Pick a difficulty level: Easy, Medium or Hard
- 👥 Set the number of servings and the ingredient amounts scale to match
- 📝 Get a full recipe with description, ingredients, step-by-step instructions, preparation and cooking time, cooking tips and a short cultural note

## 🤖 How the AI behaves

- Respects the selected country's cuisine and prefers traditional or well-known dishes
- Uses your available ingredients whenever reasonably possible
- Clearly tells you when an important ingredient is missing and suggests substitutions
- Honestly labels a recipe as fusion or modified if it is not traditionally authentic
- Keeps instructions beginner-friendly

## 🛠️ Tech Stack

- Python
- Streamlit (web interface)
- Groq API with the `groq` Python library (AI recipe generation)
- Google Colab (development)
- Streamlit Community Cloud (deployment)

## 🚀 Run It Yourself

1. Clone this repository
2. Install the requirements: `pip install -r requirements.txt`
3. Get a free API key from https://console.groq.com
4. Set your key as an environment variable named `GROQ_API_KEY`
5. Start the app: `streamlit run app.py`

The API key is never stored in the code. When deployed, it is kept in Streamlit Community Cloud secrets.

## 👩‍🍳 Author

Built by Shadab Liaqat as a beginner-friendly AI portfolio project.
