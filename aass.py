import google.generativeai as genai
import streamlit as st

# Configure your API key
# genai.configure(api_key="YOUR_API_KEY_HERE")

st.title("📈 AI Trading Bot & Market Analyzer")
st.write("Welcome to your mobile-friendly AI trading assistant powered by Google Gemini.")

st.subheader("💬 Ask AI Trading Assistant")
user_query = st.text_input(
    "Enter your trading strategy, currency pair, or market question:",
    value="XAUUSD Trend",
)

if st.button("Generate Analysis"):
  if user_query:
    try:
      # Updated model name to gemini-3.8-flash
      model = genai.GenerativeModel("gemini-3.8-flash")
      response = model.generate_content(user_query)

      st.success("Analysis Result:")
      st.write(response.text)
    except Exception as e:
      st.error(f"An error occurred: {e}")
  else:
    st.warning("Please enter a valid query or strategy.")
