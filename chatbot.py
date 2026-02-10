#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import google.generativeai as genai
from dotenv import load_dotenv

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv("Dot.env")

# Configure API
genai.configure(api_key=os.getenv("API_KEY"))

# Load Model (Best Recommended)
model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# Memory Storage (Simple)
# -----------------------------
memory = []

# -----------------------------
# Phase 1 → Chatbot
# -----------------------------
def ask_bot(question):
    memory.append(question)

    response = model.generate_content(
        f"User question: {question}\nPrevious questions: {memory}"
    )

    return response.text


# -----------------------------
# Phase 2 → Quiz Generator
# -----------------------------
def generate_quiz(topic):

    prompt = f"""
    Generate 5 MCQ questions with 4 options and correct answer.
    Topic: {topic}
    Format:
    Q1:
    A)
    B)
    C)
    D)
    Answer:
    """

    response = model.generate_content(prompt)

    return response.text


# -----------------------------
# Phase 3 → Notes Q&A (Simple RAG Style)
# -----------------------------
def notes_answer(question):

    try:
        with open("student_notes", "r", encoding="utf-8") as f:
            notes = f.read()
    except:
        return "Notes file not found. Please add study_notes.txt"

    prompt = f"""
    Answer ONLY from these notes.
    If answer not found, say 'Not found in notes'.

    NOTES:
    {notes}

    QUESTION:
    {question}
    """

    response = model.generate_content(prompt)

    return response.text


# -----------------------------
# Phase 4 → Study Planner
# -----------------------------
def study_plan(topic):

    prompt = f"""
    Create a 7 day study plan for learning {topic}.
    Make it student friendly.
    """

    response = model.generate_content(prompt)

    return response.text


# -----------------------------
# Optional → Show Memory
# -----------------------------
def show_memory():
    return memory

