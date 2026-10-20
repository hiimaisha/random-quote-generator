import random
import streamlit as st

st.set_page_config(page_title="Quote of the Moment", page_icon="✨", layout="centered")
QUOTES = [
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Great things are done by a series of small things brought together.", "Vincent van Gogh"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Success is the sum of small efforts, repeated day in and day out.", "Robert Collier"),
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
    ("The future depends on what you do today.", "Mahatma Gandhi"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("You are never too old to set another goal or to dream a new dream.", "C. S. Lewis"),
    ("Small steps every day add up to big change.", "Unknown"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("Nothing will work unless you do.", "Maya Angelou"),
]
st.title("✨ Quote of the Moment")
st.caption("A little inspiration, whenever you need it.")
if "quote" not in st.session_state:
    st.session_state.quote = random.choice(QUOTES)

st.write("")
with st.container(border=True):
    st.markdown("### “" + st.session_state.quote[0] + "”")
    st.markdown("**— " + st.session_state.quote[1] + "**")
    st.write("")
    if st.button("✨ New Quote", type="primary", use_container_width=True):
        choices = [q for q in QUOTES if q != st.session_state.quote] or QUOTES
        st.session_state.quote = random.choice(choices)
        st.rerun()
st.caption("Pause. Take a breath. Keep going.")
