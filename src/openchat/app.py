import streamlit as st
from openchat.ollama_client import get_local_models, generate_chat_response

# Page configuration
st.set_page_config(page_title="OpenChat", page_icon="💬")

st.title("OpenChat 🤖")
st.markdown("A simple chat interface for your local Ollama models.")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar configuration
with st.sidebar:
    st.header("Configuration")

    # Fetch available models
    available_models = get_local_models()
    if not available_models:
        st.error("No local Ollama models found. Please run `ollama pull <model>` in your terminal.")
        # Provide a default list if the server is unreachable just to avoid crash
        available_models = ["llama3", "mistral", "phi3"]

    # Model selection
    selected_model = st.selectbox("Select Model", options=available_models)

    st.divider()

    # Clear chat button
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Ask me anything..."):
    # Display user message and add to state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        # Use st.write_stream for a native streaming effect
        response_generator = generate_chat_response(selected_model, st.session_state.messages)
        full_response = st.write_stream(response_generator)

    # Add assistant response to state
    st.session_state.messages.append({"role": "assistant", "content": full_response})
