import random
import streamlit as st

st.set_page_config(page_title="Daily Quote", page_icon="✦", layout="centered")
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');
html,body,[class*="css"]{font-family:'DM Sans',sans-serif}.stApp{background:radial-gradient(circle at top left,#f0eaff 0%,#faf8ff 42%,#f2f7ff 100%)}
.block-container{max-width:850px;padding-top:3rem;padding-bottom:3rem}.hero{text-align:center;padding:1rem 0 1.8rem}
.hero h1{font-family:'Playfair Display',serif;font-size:2.7rem;color:#29204f;margin-bottom:.4rem}.hero p{color:#706b85;font-size:1.05rem}
.quote-card{background:#fff;border:1px solid #e9e4f7;border-radius:28px;padding:clamp(1.5rem,5vw,3.2rem);box-shadow:0 20px 55px #3d2c6c12;text-align:center}
.quote-mark{font-family:'Playfair Display',serif;font-size:4rem;line-height:.8;color:#9a82e8}.quote-text{font-family:'Playfair Display',serif;font-size:clamp(1.5rem,3vw,2.15rem);line-height:1.45;color:#282044;margin:1.2rem 0}.quote-author{color:#7861c9;font-weight:700;letter-spacing:.03em}
div.stButton>button{border-radius:14px;min-height:3rem;font-weight:700}div.stButton>button[kind="primary"]{background:#6d4ed8;color:white;border:0}div.stButton>button:hover{border-color:#8b72e8;color:#6247c4}
</style>""",unsafe_allow_html=True)
QUOTES=[
("It always seems impossible until it’s done.","Nelson Mandela","Courage"),
("The secret of getting ahead is getting started.","Mark Twain","Motivation"),
("Great things are done by a series of small things brought together.","Vincent van Gogh","Growth"),
("Believe you can and you’re halfway there.","Theodore Roosevelt","Courage"),
("Success is the sum of small efforts, repeated day in and day out.","Robert Collier","Motivation"),
("It does not matter how slowly you go as long as you do not stop.","Confucius","Growth"),
("The future depends on what you do today.","Mahatma Gandhi","Mindfulness"),
("Act as if what you do makes a difference. It does.","William James","Motivation"),
("You are never too old to set another goal or to dream a new dream.","C. S. Lewis","Growth"),
("Do what you can, with what you have, where you are.","Theodore Roosevelt","Courage"),
("Nothing will work unless you do.","Maya Angelou","Motivation"),
("Happiness depends upon ourselves.","Aristotle","Mindfulness"),
("Turn your wounds into wisdom.","Oprah Winfrey","Growth"),
("The only way out is through.","Robert Frost","Courage"),
("Wherever you go, go with all your heart.","Confucius","Mindfulness"),
("You miss 100% of the shots you don’t take.","Wayne Gretzky","Motivation"),
("If you can dream it, you can do it.","Walt Disney","Growth"),
("No act of kindness, no matter how small, is ever wasted.","Aesop","Kindness"),
("Be yourself; everyone else is already taken.","Oscar Wilde","Confidence"),
("Start where you are. Use what you have. Do what you can.","Arthur Ashe","Motivation"),
("Nothing diminishes anxiety faster than action.","Walter Anderson","Courage"),
("The best way to predict the future is to create it.","Peter Drucker","Growth"),
("You have power over your mind—not outside events.","Marcus Aurelius","Mindfulness"),
("A little progress each day adds up to big results.","Unknown","Motivation"),
("Be kind whenever possible. It is always possible.","Dalai Lama","Kindness"),
("Difficulties strengthen the mind, as labor does the body.","Seneca","Courage"),
("The journey of a thousand miles begins with one step.","Lao Tzu","Growth"),
("Nothing can dim the light that shines from within.","Maya Angelou","Confidence"),
("With the new day comes new strength and new thoughts.","Eleanor Roosevelt","Mindfulness"),
("It always seems impossible until it’s done.","Nelson Mandela","Courage")
]
st.markdown('<div class="hero"><h1>✦ A Little Perspective</h1><p>A thoughtful quote for whatever kind of day you’re having.</p></div>',unsafe_allow_html=True)
categories=["All moods"]+sorted({q[2] for q in QUOTES})
category=st.selectbox("Choose a mood",categories)
available=[q for q in QUOTES if category=="All moods" or q[2]==category]
if "quote_current" not in st.session_state: st.session_state.quote_current=random.choice(available)
if st.session_state.get("quote_category")!=category:
    st.session_state.quote_current=random.choice(available); st.session_state.quote_category=category
q=st.session_state.quote_current
st.markdown(f'<div class="quote-card"><div class="quote-mark">“</div><div class="quote-text">{q[0]}</div><div class="quote-author">— {q[1]}</div></div>',unsafe_allow_html=True)
st.write("")
_,center,_=st.columns([1,2,1])
with center:
    if st.button("✦  New Quote",type="primary",use_container_width=True):
        choices=[item for item in available if item!=st.session_state.quote_current]
        st.session_state.quote_current=random.choice(choices or available); st.rerun()
    st.download_button("↓  Save quote as text",data=f'“{q[0]}” — {q[1]}',file_name="quote.txt",mime="text/plain",use_container_width=True)
st.caption(f"{len(available)} quotes in this collection · Mood: {q[2]}")
