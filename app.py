import streamlit as st
from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

st.title("AI Explanation Generator")

topic = st.text_input("Enter a topic:")

if st.button("Generate Explanation"):
    if topic:
        prompt = f"Explain {topic} in simple terms for a beginner with a real-life example."

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are an expert teacher who explains concepts in simple terms with examples."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        st.write(response.choices[0].message.content)
    else:
        st.write("Please enter a topic.")