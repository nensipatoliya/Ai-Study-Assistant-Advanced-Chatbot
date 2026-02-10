#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from chatbot import ask_bot, generate_quiz, notes_answer, study_plan, show_memory

# -----------------------------
# App Title
# -----------------------------
st.title("🎓 AI Study Assistant - Advanced")

st.write("Select feature and ask your question")

# -----------------------------
# Feature Selection
# -----------------------------
option = st.selectbox(
    "Choose Feature",
    [
        "Chatbot",
        "Quiz Generator",
        "Notes Q&A",
        "Study Planner",
        "Show Memory"
    ]
)

# -----------------------------
# User Input
# -----------------------------
user_input = st.text_input("Enter Question / Topic")

# -----------------------------
# Submit Button
# -----------------------------
if st.button("Submit"):

    if option == "Chatbot":
        if user_input:
            answer = ask_bot(user_input)
            st.write("🤖 AI Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question")

    elif option == "Quiz Generator":
        if user_input:
            quiz = generate_quiz(user_input)
            st.write("📝 Quiz:")
            st.write(quiz)
        else:
            st.warning("Enter topic for quiz")

    elif option == "Notes Q&A":
        if user_input:
            notes_ans = notes_answer(user_input)
            st.write("📚 Notes Answer:")
            st.write(notes_ans)
        else:
            st.warning("Enter question from notes")

    elif option == "Study Planner":
        if user_input:
            plan = study_plan(user_input)
            st.write("📅 Study Plan:")
            st.write(plan)
        else:
            st.warning("Enter topic for study plan")

    elif option == "Show Memory":
        mem = show_memory()
        st.write("🧠 Previous Questions:")
        st.write(mem)

