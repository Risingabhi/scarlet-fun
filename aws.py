import requests
import streamlit as st

# Define the Streamlit app
st.title("AWS Chat App Endpoint")

# Input field for user query
user_query = st.text_input("Enter your query:")

# Button to trigger API request
if st.button("Submit"):
    # Endpoint URL
    endpoint_url = (
        "https://vuepff1fc7.execute-api.us-east-1.amazonaws.com/test/myresource"
    )

    # Request payload
    data = {"queryStringParameters": {"query": user_query}}

    try:
        # Send POST request
        response = requests.post(endpoint_url, json=data)

        # Check response status code
        if response.status_code == 200:
            result = response.json()
            generated_text = result.get("body", "").split(":")[-1].strip()
            st.write("Generated Text:")
            st.write(generated_text)
        else:
            st.error(
                f"Inference request failed with status code: {response.status_code}"
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")
