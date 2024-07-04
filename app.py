import streamlit as st
from transformers import pipeline
from gtts import gTTS
import os

# Initialize translation pipelines for different languages
models = {
    "French": "Helsinki-NLP/opus-mt-en-fr",
    "Spanish": "Helsinki-NLP/opus-mt-en-es",
    "Hebrew": "Helsinki-NLP/opus-mt-en-he"
}

# Mapping for gTTS language codes
language_codes = {
    "French": "fr",
    "Spanish": "es"
}

st.title("Interactive Language Translator")
st.write("Input a phrase to translate and choose the target language.")

phrase = st.text_input("Enter a phrase in English:")

language = st.selectbox(
    "Select the language to translate to:",
    options=["French", "Spanish", "Hebrew"]
)

if st.button("Translate"):
    if phrase:
        model_name = models[language]
        translator = pipeline("translation", model=model_name)
        translation = translator(phrase)[0]['translation_text']
        st.write(f"Translation in {language}: {translation}")
        
        lang_code = language_codes.get(language)
        if lang_code:
            try:
                tts = gTTS(translation, lang=lang_code)
                tts.save("translation.mp3")
                st.audio("translation.mp3")
            except Exception as e:
                st.write(f"Error generating audio: {e}")
        else:
            st.write("Audio output is not supported for this language.")
    else:
        st.write("Please enter a phrase.")
















