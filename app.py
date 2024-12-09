import streamlit as st
import google.generativeai as genai

# Load the API key from the file
with open(r"C:\Users\Lenovo\Downloads\code reviever\GOOGLE_API_KEY.txt") as f:
    key = f.read().strip()

# Configure your API key
genai.configure(api_key=key)


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
        /* Background styling */
        .stApp {
            background-image: linear-gradient(to right, #87ceeb, #b0e0e6);color: #2f4f4f;
        }

        /* Title styling */
        .title {
            font-size: 2.5em;
            font-weight: bold;
            color: #000000;
            text-shadow: 2px 2px 5px #000;
            margin-bottom: 10px;
        }

        /* Text area styling */
        textarea {
            background: rgba(255, 255, 255, 0.8) !important;
            border: 1px solid #ddd !important;
            color: #000 !important;
            border-radius: 5px !important;
            font-size: 20px !important;
        }

        /* Button styling */
        button[kind="primary"] {
            background-color: #4CAF50 !important;
            color: white !important;
            border-radius: 8px !important;
            font-size: 18px !important;
            padding: 10px 20px !important;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        }

        /* Subheader styling */
        .stMarkdown h2 {
            color: #000000;
            text-shadow: 1px 1px 2px #000;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.title("🚀 Gen-AI Code Reviewer Features")
st.sidebar.markdown("---")
# Introduction
st.sidebar.subheader("✨ How to Use?")
st.sidebar.info("""
1. **Enter your Python code**: Paste or type your Python code into the input section.
2. **Review Output**: Receive a detailed analysis, including:
   - Bug reports 🐞
   - Optimization tips ⚡
   - Feedback for better coding practices 💡.
""")

st.sidebar.markdown("---")

# Features Highlight
st.sidebar.subheader("🌟 Features")
st.sidebar.write("""
- **Fast & Accurate**: Quickly identifies issues in your code.
- **Actionable Feedback**: Suggestions to improve readability and performance.
- **Beginner-Friendly**: Simple interface for all skill levels.
""")

st.sidebar.markdown("---")

# Call-to-Action
st.sidebar.subheader("📌 Pro Tip!")
st.sidebar.success("“Good code is not written; it’s rewritten.” Always review your code for potential enhancements.")


# Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>🤖 AI Code Reviewer 🔎</h1>",
    unsafe_allow_html=True
)
# Description
# Description
st.write("""
Welcome to **Gen-AI Code Reviewer**! 🔍  
Paste your Python code and let our smart AI assistant do the heavy lifting.💻It will instantly spot errors, offer suggestions to optimize performance, and guide you with best practices for cleaner, more efficient code.✨With every review, become a better coder and elevate your coding game to new heights! 🚀
""")

# Input for the human prompt
human_code = st.text_area("📝 Enter your code here for review:")

# Button to trigger code review
if st.button("✨ Generate"):
    if human_code:
        # Initialize the generative model
        genai.configure(api_key=key)
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        
        # Send the user code for review
        chatbot = model.start_chat(history=[])
        response = chatbot.send_message(f"Review the following Python code and identify any bugs:\n{human_code}")
        #response = chatbot.send_message(f"Review the following Java code and identify any bugs:\n{human_code}")
        # Display the AI-generated response
        st.markdown("<h3 style='text-align: center;'>🔎 Code Review 📝</h3>",unsafe_allow_html=True)
        st.markdown("**Bug Report:**")
        st.write(response.text)  # Display AI response
    else:
        st.error("❌ Please enter some code before generating the review!")

# Footer
st.markdown("---")
#st.markdown("Made by Rakesh")

