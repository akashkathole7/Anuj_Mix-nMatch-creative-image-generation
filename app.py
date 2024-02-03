# Importing necessary libraries
import streamlit as st
import replicate
import os

# Setting Replicate API Token
st.session_state['replicate_api_token'] = st.sidebar.text_input("Replicate API Token", type='password')
os.environ['REPLICATE_API_TOKEN'] = st.session_state['replicate_api_token']

# Checking if Replicate API Token is provided
if not st.session_state['replicate_api_token']:
    st.sidebar.warning('Please enter your Replicate API Token to continue!!')
    st.sidebar.info("You can get your Replicate API Token from here: [Replicate](https://replicate.com/account/api-tokens)")
    st.stop()

# Function to generate images based on user input
def generate_images():
    prompt = st.text_input("Enter prompt", help="Write something you can imagine...")
    negative_prompt = st.text_input("Enter Negative prompt", help="Write what you don't want to see in the generated images")
    submit = st.button("Submit")

    if submit:
        output = replicate.run(
            "stability-ai/sdxl:8beff3369e81422112d93b89ca01426147de542cd4684c244b673b105188fe5f",
            input={
                "prompt": prompt, 
                "negative_prompt": negative_prompt, 
                "num_outputs": 4
            },
        )
        col1, col2 = st.columns(2)
        with col1:
            st.image(output[0])
            st.image(output[2])
        with col2:
            st.image(output[1])
            st.image(output[3])

# Display the image generation page
generate_images()
