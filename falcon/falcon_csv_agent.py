from langchain.agents import create_csv_agent
from langchain.agents import create_pandas_dataframe_agent
from langchain import HuggingFaceHub
from dotenv import load_dotenv
import os
import pandas as pd
import streamlit as st
from streamlit_chat import message
from tempfile import NamedTemporaryFile


def main():
    # --------------------------------------------------------------
    # Load the HuggingFaceHub API token from the .env file
    # --------------------------------------------------------------

    load_dotenv()
    HUGGINGFACEHUB_API_TOKEN = os.environ["HUGGINGFACEHUB_API_TOKEN"]


    # --------------------------------------------------------------
    # Load the LLM model from the HuggingFaceHub
    # --------------------------------------------------------------

    repo_id = "tiiuae/falcon-7b-instruct" 
    falcon_llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": 0.01, "max_new_tokens": 500}
    )

    st.set_page_config(page_title="Ask your CSV")
    st.header("Know your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if csv_file is not None:
        with NamedTemporaryFile() as f: # Create temporary file
            f.write(csv_file.getvalue()) # Save uploaded contents to file
            df = pd.read_csv(f.name)
            #agent = create_csv_agent(falcon_llm, f.name, verbose=True)
            agent = create_pandas_dataframe_agent(falcon_llm, df, verbose=True)
             # Initialize the chat history in the session_state if it doesn't exist
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = []

            user_input = st.text_input("Ask your question:", key="input_field")

            if user_input:
                answer = agent.run(user_input)
                # Add the question and answer to the chat_history
                st.session_state.chat_history.append(("user", user_input))
                st.session_state.chat_history.append(("agent", answer))

            # Display the chat_history in a chat-like format using streamlit-chat
            for i, (sender, message_text) in enumerate(st.session_state.chat_history):
                if sender == "user":
                    message(message_text, is_user=True, key=f"{i}_user")
                else:
                    message(message_text, key=f"{i}")


if __name__ == "__main__":
    main()