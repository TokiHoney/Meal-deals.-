import streamlit as st
import json

BUDGET = 15

# Load food menu data from JSON file
@st.cache_data
def load_menu():
    with open('menu.json', 'r') as f:
        return json.load(f)

menu = load_menu()

st.title("Build Your Favorite Meal!")

if "choices" not in st.session_state:
    st.session_state.choices = {}

total_price = 0

def format_option(item):
    return f"{item['name']} (${item['price']}) [{item['source']}]"

for category in menu.keys():
    st.header(category)

    # Prepare options text with price/source
    options = [format_option(item) for item in menu[category]]

    # Default selection placeholder
    placeholder_text = "Select your " + category.lower()

    # Selection dropdown
    choice = st.selectbox(placeholder_text, options, index=0, key=f"select_{category}")

    # Find the selected item data
    selected_item = menu[category][options.index(choice)]

    # Show image and price next to selection
    cols = st.columns([1, 3])
    with cols[0]:
        st.image(selected_item['img'], width=100)
    with cols[1]:
        st.write(f"**Price:** ${selected_item['price']}")
        st.write(f"**Source:** {selected_item['source']}")

    # Save user's choice
    st.session_state.choices[category] = selected_item

# Calculate total price
total_price = sum(item['price'] for item in st.session_state.choices.values())
st.markdown(f"### Total Price: ${total_price} / ${BUDGET}")

if total_price > BUDGET:
    st.error("Oops! You've exceeded the budget. Please adjust your choices.")

if len(st.session_state.choices) == len(menu):
    st.success("Your meal is complete! Here are your selections:")
    for cat, item in st.session_state.choices.items():
        st.write(f"- **{cat}**: {item['name']} (${item['price']}, {item['source']})")

# Reset button
if st.button("Clear my meal"):
    st.session_state.choices = {}
    st.experimental_rerun()
