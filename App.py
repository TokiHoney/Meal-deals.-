import streamlit as st

# Example menu data -- expand as desired!
menu = {
    "Appetizer": [
        {"name": "Mozzarella Sticks", "price": 3, "source": "Fast Food", "img": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Mozzarella_sticks.jpg"},
        {"name": "Chips & Salsa", "price": 2, "source": "Homemade", "img": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Chips_and_Salsa_%287063175661%29.jpg"}
    ],
    "Entree": [
        {"name": "Big Mac", "price": 5, "source": "Fast Food", "img": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Big_Mac_hamburger.jpg"},
        {"name": "Grilled Cheese", "price": 2, "source": "Homemade", "img": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Grilled_Cheese_Sandwich.jpg"}
    ],
    "Dessert": [
        {"name": "McFlurry", "price": 3, "source": "Fast Food", "img": "https://upload.wikimedia.org/wikipedia/commons/1/19/McFlurry.jpg"},
        {"name": "Brownies", "price": 2, "source": "Homemade", "img": "https://upload.wikimedia.org/wikipedia/commons/6/60/Chocolatebrownie.JPG"}
    ],
    "Drink": [
        {"name": "Coke", "price": 1, "source": "Fast Food", "img": "https://upload.wikimedia.org/wikipedia/commons/0/09/Coca-Cola_glass_bottle.jpg"},
        {"name": "Lemonade", "price": 2, "source": "Homemade", "img": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Classic_lemonade.jpg"}
    ]
}

st.title("Build Your Favorite Meal!")
BUDGET = 15

if "choices" not in st.session_state:
    st.session_state.choices = {}

total = 0
for category, options in menu.items():
    st.header(category)
    cols = st.columns(len(options))
    for idx, (col, item) in enumerate(zip(cols, options)):
        with col:
            st.image(item["img"], width=120)
            if st.button(f'{item["name"]} (${item["price"]})\n[{item["source"]}]', key=f"{category}_{idx}"):
                st.session_state.choices[category] = item

# Calculate total
total = sum(v["price"] for v in st.session_state.choices.values())
st.write(f"### Total: ${total} / ${BUDGET}")

# Show choices
if len(st.session_state.choices) == len(menu):
    st.success("Meal Complete! Here are your picks:")
    for cat, item in st.session_state.choices.items():
        st.write(f'- **{cat}**: {item["name"]} (${item["price"]}, {item["source"]})')
    if total > BUDGET:
        st.error("Oops! Over budget. Remove an item to continue.")

# Optionally, add a button to clear choices
if st.button("Clear my meal"):
    st.session_state.choices = {}
