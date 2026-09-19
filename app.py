import os
import streamlit as st
from groq import Groq

# Basic page settings (browser tab title and icon)
st.set_page_config(page_title="AI International Recipe Generator", page_icon="🍳")

# The Groq model that writes the recipes
MODEL_NAME = "openai/gpt-oss-120b"

# Country/Cuisine menu
CUISINES = {
    "🇵🇰 Pakistan": ["Biryani", "Karahi", "Nihari"],
    "🇮🇹 Italy": ["Pasta", "Pizza", "Risotto"],
    "🇮🇳 India": ["Butter Chicken", "Masala Dosa", "Chana Masala"],
    "🇨🇳 China": ["Fried Rice", "Chow Mein", "Dumplings"],
    "🇯🇵 Japan": ["Sushi", "Ramen", "Teriyaki"],
    "🇲🇽 Mexico": ["Tacos", "Enchiladas", "Quesadillas"],
    "🇹🇷 Turkey": ["Kebab", "Pide", "Menemen"],
    "🇰🇷 South Korea": ["Kimchi Fried Rice", "Bibimbap", "Tteokbokki"],
    "🇹🇭 Thailand": ["Pad Thai", "Green Curry", "Tom Yum"],
    "🇫🇷 France": ["Ratatouille", "Crepes", "Quiche"],
    "🇪🇸 Spain": ["Paella", "Tortilla Espanola", "Gazpacho"],
}

# Fixed rules that the AI must always follow
SYSTEM_MESSAGE = """You are a friendly and knowledgeable international cooking assistant.
Follow these rules:
1. Respect the selected country's cuisine.
2. Prefer traditional or commonly known dishes from that cuisine.
3. Use the user's available ingredients whenever reasonably possible.
4. Clearly mention if an important ingredient is missing.
5. Suggest reasonable substitutions for unavailable ingredients.
6. Do not call a recipe traditionally authentic if it is a fusion or modified version. Say so honestly.
7. Keep instructions beginner-friendly and easy to follow.
8. Scale all ingredient amounts for the requested number of servings.
Always reply in simple English only."""


def generate_recipe(client, country, ingredients, meal_type, difficulty, servings):
    """Send the user's choices to Groq and return the recipe text."""
    # "🇮🇹 Italy" -> "Italy" (remove the flag)
    country_name = country.split(" ", 1)[1]

    # Famous dishes of the selected country, used as inspiration
    famous_dishes = ", ".join(CUISINES[country])

    user_message = f"""Create a recipe with these preferences:
- Cuisine: {country_name}
- Popular dishes from this cuisine (for inspiration): {famous_dishes}
- Available ingredients: {ingredients}
- Meal type: {meal_type}
- Difficulty: {difficulty}
- Servings: {servings}

Format the answer in Markdown using exactly these sections:
## 🌍 Cuisine
## 🍽️ Recipe Name
## 📝 Description
## 🥘 Ingredients
## ⚠️ Missing Ingredients and Substitutions
## 👩‍🍳 Instructions (numbered steps)
## ⏱️ Preparation Time
## 🔥 Cooking Time
## 📊 Difficulty
## 👥 Servings
## 💡 Cooking Tips
## 🌎 Cultural Note"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
        max_completion_tokens=3000,
    )
    return response.choices[0].message.content


# ---------- User interface ----------
st.title("🍳 AI International Recipe Generator")
st.write("Discover delicious recipes from around the world!")

country = st.selectbox("🌍 Choose Country/Cuisine", list(CUISINES.keys()))

ingredients = st.text_area(
    "🥘 Enter Your Ingredients",
    placeholder="Example: chicken, tomato, onion, garlic, cheese",
)

meal_type = st.selectbox(
    "🍽️ Meal Type", ["Breakfast", "Lunch", "Dinner", "Snack", "Dessert"], index=2
)

difficulty = st.selectbox("📊 Difficulty", ["Easy", "Medium", "Hard"])

servings = st.number_input("👥 Servings", min_value=1, max_value=12, value=2, step=1)

# Read the API key from the environment (it is never written in this file)
def get_api_key():
    """Read the key from Streamlit Cloud secrets, or from the environment (Colab)."""
    try:
        return st.secrets["GROQ_API_KEY"]
    except Exception:
        return os.environ.get("GROQ_API_KEY")


api_key = get_api_key()

if st.button("Generate Recipe 🍳"):
    if not api_key:
        st.error("GROQ_API_KEY was not found. Please run the key setup cell in Colab first.")
    elif not ingredients.strip():
        st.warning("Please enter at least one ingredient.")
    else:
        try:
            client = Groq(api_key=api_key)
            with st.spinner("Cooking up your recipe... 👩‍🍳"):
                recipe = generate_recipe(
                    client, country, ingredients, meal_type, difficulty, servings
                )
            st.markdown(recipe)
        except Exception as error:
            st.error(f"Something went wrong: {error}")
