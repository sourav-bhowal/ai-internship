import streamlit as st
import nltk
from transformers import pipeline
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Initialize the chatbot pipeline 
chatbot = pipeline("text-generation", model="distilgpt2")

# Function to create a healthcare chatbot 
def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        response = "I am not a doctor, but I can help you find information on symptoms."
    elif "appointment" in user_input:
        response = "I can help you find information on how to schedule an appointment."
    elif "prescription" in user_input:
        response = "I can help you find information on how to get a prescription."
    elif "insurance" in user_input:
        response = "I can help you find information on insurance coverage."
    else:
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
    return response[0]['generated_text']

# Create the main function
def main():
    st.title("Health Chatbot")
    user_input = st.text_input("How can I help you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            st.spinner("Chatbot is typing...")
            response = healthcare_chatbot(user_input)
            st.write("Chatbot: ", response)
        else:
            st.write("Please enter a message.")

# Run the main function
main()