from langchain.agents import create_csv_agent
from langchain.llms import GooseAI
from dotenv import load_dotenv
import os
import streamlit as st
from streamlit_chat import message
from tempfile import NamedTemporaryFile

def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("GOOSEAI_API_KEY") is None or os.getenv("GOOSEAI_API_KEY") == "":
        print("GOOSEAI_API_KEY is not set")
        exit(1)
    else:
        print("GOOSEAI_API_KEY is set")
    
    st.set_page_config(page_title="Ask your CSV")
    st.header("Know your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if csv_file is not None:
        with NamedTemporaryFile() as f: # Create temporary file
            f.write(csv_file.getvalue()) # Save uploaded contents to file
            agent = create_csv_agent(
                GooseAI(temperature=0), csv_file, verbose=True)
            
            # Initialize the chat history in the session_state if it doesn't exist
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = []

            user_question = st.text_input("Ask your question:", key="input_field")

            if user_question is not None and user_question != "":
                prompt = """
                For the following query, if it requires drawing a table, reply as follows:
                {"table": {"columns": ["column1", "column2", ...], "data": [[value1, value2, ...], [value1, value2, ...], ...]}}

                If the query requires creating a bar chart, reply as follows:
                {"bar": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}

                If the query requires creating a line chart, reply as follows:
                {"line": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}

                There can only be two types of chart, "bar" and "line".

                If it is just asking a question that requires neither, reply as follows:
                {"answer": "answer"}
                Example:
                {"answer": "The title with the highest rating is 'Gilead'"}

                If you do not know the answer, reply as follows:
                {"answer": "I do not know."}

                Return all output as a string.

                All strings in "columns" list and data list, should be in double quotes,

                For example: {"columns": ["title", "ratings_count"], "data": [["Gilead", 361], ["Spider's Web", 5164]]}

                Lets think step by step.

                Below is the query.
                Query: 
                """ + user_question

                with st.spinner(text="In progress..."):
                    answer = agent.run(user_question)
                    # Add the question and answer to the chat_history
                    st.session_state.chat_history.append(("user", user_question))
                    st.session_state.chat_history.append(("agent", answer))
                    st.write(agent.run(user_question))

            # Display the chat_history in a chat-like format using streamlit-chat
            for i, (sender, message_text) in enumerate(st.session_state.chat_history):
                if sender == "user":
                    message(message_text, is_user=True, key=f"{i}_user")
                else:
                    message(message_text, key=f"{i}")

if __name__ == "__main__":
    main()