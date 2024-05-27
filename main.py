import streamlit as st
from utils import get_results

# List of famous programming languages
languages = ["Python", "JavaScript", "Java", "C++", "C#", "Ruby", "Go", "Swift", "Kotlin", "PHP"]

# Function to get result from a mock LLM (replace this with actual LLM call)
def get_llm_result(input_language, code, language):
    # Mock result for demonstration purposes
    result = get_results(input_language, language, code)
    return f"{input_language} code Processed code in {language}:\n\n{result}"

# Main app function
def main():
    st.title("Convert Code")

    # Create two columns for input and output sections
    left_col, right_col = st.columns(2)

    with left_col:
        st.header("Input Section")

        # Dropdown menu for selecting programming language
        input_language = st.selectbox("Select Programming Language", languages)

        # Large text area for user to paste their code
        user_code = st.text_area("Paste your code here:", height=300)

    with right_col:
        st.header("Output Section")

        # Dropdown menu for selecting programming language
        output_language = st.selectbox("Select Output Language", languages)
        if st.button('Convert'):
        # Get LLM result
            llm_result = get_llm_result(input_language, user_code, output_language)

        # Output container with fixed height and scroll
            st.markdown(llm_result, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
