import streamlit as st
import google.generativeai as genai
import os

# Set Streamlit page configuration
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
        .stApp { background-image: linear-gradient(to right, #87ceeb, #b0e0e6); color: #2f4f4f; }
        .title { font-size: 2.5em; font-weight: bold; color: #000000; text-shadow: 2px 2px 5px #000; }
        textarea { background: rgba(255, 255, 255, 0.8) !important; border-radius: 5px !important; }
        button[kind="primary"] { background-color: #4CAF50 !important; color: white !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar content
st.sidebar.title("🚀 Gen-AI Code Reviewer Features")
st.sidebar.markdown("---")
st.sidebar.subheader("✨ How to Use?")
st.sidebar.info("""
1. **Enter your Python code**: Paste or type your Python code into the input section.
2. **Review Output**: Receive a detailed analysis, including:
   - Bug reports 🐞
   - Optimization tips ⚡
   - Feedback for better coding practices 💡.
""")
st.sidebar.markdown("---")
st.sidebar.subheader("📌 Pro Tip!")
st.sidebar.success("“Good code is not written; it’s rewritten.” Always review your code for potential enhancements.")

# Title and Description
st.markdown("<h1 style='text-align: center; color: black;'>🤖 AI Code Reviewer 🔎</h1>", unsafe_allow_html=True)
st.write("""
Welcome to **Gen-AI Code Reviewer**! Paste your Python code and let our smart AI assistant review it for bugs, offer suggestions, and guide you with best practices.
""")

# Input for the code
human_code = st.text_area("📝 Enter your code here for review:")

# Button to trigger code review
if st.button("✨ Generate"):
    if human_code:
        try:
            # Configure API key using environment variable (preferred for deployment)
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                st.error("❌ GOOGLE_API_KEY is not set. Please configure your API key.")
            else:
                # Configure API key
                genai.configure(api_key=api_key)
                
                # Use Google's generative AI model
                response = genai.generate_text(
                    prompt=f"Review the following Python code and identify any bugs:\n{human_code}",
                    model="text-bison-001"  # Use the correct model name
                )
                
                # Display the AI-generated response
                st.markdown("<h3 style='text-align: center;'>🔎 Code Review 📝</h3>", unsafe_allow_html=True)
                st.write("**Bug Report:**")
                st.write(response.result)
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
    else:
        st.error("❌ Please enter some code before generating the review!")
