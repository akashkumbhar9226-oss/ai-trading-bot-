import google.generativeai as genai
import streamlit as st

st.set_page_config(page_title="AI Trading Assistant", page_icon="📈", layout="centered")

st.title("📈 AI Trading Bot & Market Analyzer")
st.write("Welcome to your mobile-friendly AI trading assistant powered by Google Gemini.")

st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    try:
        # Check available models automatically to prevent 404 errors
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model_name = 'gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0].replace('models/', '')
        model = genai.GenerativeModel(model_name)
        st.sidebar.success(f"Connected using model: {model_name}")
    except Exception as e:
        model = genai.GenerativeModel('gemini-pro')
        st.sidebar.success("API Key configured successfully!")
else:
    st.sidebar.warning("Please enter your Gemini API Key to start analysis.")

st.subheader("🤖 Ask AI Trading Assistant")
user_prompt = st.text_area("Enter your trading strategy, currency pair, or market question:", placeholder="e.g., Analyze XAUUSD trend for today or suggest a scalp strategy.")

if st.button("Generate Analysis"):
    if not api_key:
        st.error("Please provide your Gemini API Key in the sidebar first.")
    elif not user_prompt:
        st.warning("Please enter a question or prompt for the AI.")
    else:
        with st.spinner("Analyzing market conditions..."):
            try:
                response = model.generate_content(f"Act as an expert Forex and Gold (XAUUSD) trading bot and algorithmic trading mentor. Provide professional insights for: {user_prompt}")
                st.subheader("📊 AI Insights & Strategy:")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
