import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

# =========================================
# CONFIGURATION
# =========================================

# 🔑 Put your real Gemini API key here:
GOOGLE_API_KEY = "AIzaSyBTDwIzEwJY3OhdBEOuBRfTmHiqaZZgaWE".strip()

# Streamlit page config
st.set_page_config(page_title="Gramin Vigyan", page_icon="🌾")

st.title("🌾 Gramin Vigyan (Village Science)")
st.subheader("Learn Science in Your Language, With Your Examples.")

# Validate and configure the API key
if not GOOGLE_API_KEY or GOOGLE_API_KEY == "AIzaSyAvgI4218AZWF8vDKBJjYrshAmKJYgMRl0":
    st.warning(
        "⚠️ Google API key is not set.\n\n"
        "Please open the code and replace "
        "`AIzaSyAvgI4218AZWF8vDKBJjYrshAmKJYgMRl0` with your actual Gemini API key."
    )
    genai_configured = False
else:
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        genai_configured = True
    except Exception as e:
        st.error(f"Failed to configure Google Generative AI: {e}")
        genai_configured = False


# =========================================
# ANALOGY ENGINE
# =========================================
def get_analogy(concept: str, language_name: str) -> str:
    """
    Call Gemini to generate an explanation with a rural Indian analogy.
    Raises RuntimeError with a clear message instead of raw exceptions.
    """
    if not genai_configured:
        raise RuntimeError("Google Generative AI is not configured correctly.")

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        raise RuntimeError(f"Could not load Gemini model: {e}")

    prompt = f"""
    Explain the scientific concept '{concept}' to a rural Indian student.
    1. First, give a 1-sentence standard definition.
    2. Then, explain it using a culturally relevant analogy from an Indian village or daily life
       (like farming, cricket, festivals, or traffic).
    3. Finally, explain it in the language: {language_name}.
    Output ONLY the explanation in {language_name}.
    """

    try:
        response = model.generate_content(prompt)
    except Exception as e:
        raise RuntimeError(f"Error while generating explanation from the AI model: {e}")

    # Safely handle empty or unexpected responses
    text = getattr(response, "text", None)
    if not text:
        # Fallback for older response formats
        try:
            parts = response.candidates[0].content.parts
            text = "".join(p.text for p in parts if hasattr(p, "text"))
        except Exception:
            text = None

    if not text:
        raise RuntimeError("The AI model returned an empty response. Try again.")

    return text


# =========================================
# FRONTEND
# =========================================

# 1. Inputs
concept = st.text_input("Enter a Science Topic (e.g., Gravity, Photosynthesis):")
language = st.selectbox(
    "Select Your Language",
    ["Hindi", "Tamil", "Telugu", "Bengali", "Marathi"],
    index=0,
)

# 2. The Magic Button
if st.button("Explain to Me"):
    if not concept.strip():
        st.error("Please enter a topic first!")
    elif not genai_configured:
        st.error(
            "Google API key is missing or invalid. "
            "Please configure it correctly and reload the app."
        )
    else:
        with st.spinner("Asking the Village Teacher..."):
            try:
                # Call the AI
                explanation = get_analogy(concept.strip(), language)

                # Show Text
                st.success("Here is your explanation:")
                st.markdown(explanation)

                # Generate Audio (accessibility)
                lang_map = {
                    "Hindi": "hi",
                    "Tamil": "ta",
                    "Telugu": "te",
                    "Bengali": "bn",
                    "Marathi": "mr",
                }

                lang_code = lang_map.get(language)
                if not lang_code:
                    st.warning("Audio language code not found for this language.")
                else:
                    try:
                        tts = gTTS(text=explanation, lang=lang_code, slow=False)
                        audio_file = "explanation.mp3"
                        tts.save(audio_file)
                        st.audio(audio_file)
                    except Exception as e:
                        st.warning(f"Audio generation failed: {e}")

            except RuntimeError as e:
                st.error(str(e))
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")


# =========================================
# SIDEBAR
# =========================================
st.sidebar.title("About")
st.sidebar.info(
    "Bridging the vernacular gap in STEM education using GenAI context localization.\n\n"
    "This app explains science topics using analogies from Indian village life and "
    "translates them into regional languages with audio support."
)
