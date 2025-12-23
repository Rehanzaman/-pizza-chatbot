import streamlit as st

st.set_page_config(page_title="Pizza Chatbot", page_icon="🍕")

st.title("🍕 Pizza Ordering Chatbot")

menu = {
    "Margherita": 800,
    "Pepperoni": 1000,
    "BBQ Chicken": 1200,
    "Veggie": 900
}

# Session state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.order = {}

# Step 0 – Show menu
if st.session_state.step == 0:
    st.write("👋 Welcome! Ye hamara menu hai:")

    for pizza, price in menu.items():
        st.write(f"• **{pizza}** – Rs {price}")

    pizza = st.selectbox("🍕 Pizza choose karein:", list(menu.keys()))
    qty = st.number_input("🔢 Quantity:", min_value=1, step=1)

    if st.button("Next"):
        st.session_state.order["pizza"] = pizza
        st.session_state.order["qty"] = qty
        st.session_state.step = 1

# Step 1 – Confirm order
elif st.session_state.step == 1:
    pizza = st.session_state.order["pizza"]
    qty = st.session_state.order["qty"]
    total = menu[pizza] * qty

    st.write("✅ Aapka order:")
    st.write(f"Pizza: **{pizza}**")
    st.write(f"Quantity: **{qty}**")
    st.write(f"Total Bill: **Rs {total}**")

    if st.button("Confirm Order"):
        st.session_state.step = 2

# Step 2 – Order status
elif st.session_state.step == 2:
    st.success("🍕 Order Confirmed!")
    st.write("⏳ Status: Pizza ban raha hai...")

    if st.button("Check Status"):
        st.info("🚚 Pizza on the way!")

    if st.button("New Order"):
        st.session_state.step = 0
        st.session_state.order = {}
