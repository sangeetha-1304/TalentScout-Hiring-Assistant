import streamlit as st
from chatbot import ask_tech_questions
from utils import should_exit

st.title("🤖 TalentScout Hiring Assistant")
st.write("Welcome! Please answer the following questions for initial screening.")

questions = [
    "What is your full name?",
    "What is your email address?",
    "What is your phone number?",
    "How many years of experience do you have?",
    "What position are you applying for?",
    "What is your current location?",
    "Please list your tech stack (languages, frameworks, tools)"
]

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

# -------- FINAL RESULT --------
if st.session_state.step == len(questions):
    st.subheader("🔍 Technical Interview Questions")
    tech_stack = st.session_state.answers[-1]
    st.write(ask_tech_questions(tech_stack))

    if st.button("🔄 Restart"):
        st.session_state.clear()
        st.rerun()

    st.stop()

# -------- QUESTION FLOW --------
st.write(questions[st.session_state.step])

with st.form(key=f"form_{st.session_state.step}"):
    user_input = st.text_input("Type your answer here:")
    submitted = st.form_submit_button("Next")

if submitted:
    if should_exit(user_input):
        st.success("Thank you for your time! Our team will contact you soon.")
        st.stop()

    if user_input.strip() == "":
        st.warning("Please enter a value before continuing.")
        st.stop()

    st.session_state.answers.append(user_input)
    st.session_state.step += 1
    st.rerun()
