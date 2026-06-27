import streamlit as st

from src.image_processor import load_image
from src.assistant import analyze_image

st.set_page_config(
    page_title="Multimodal AI Safety Assistant",
    page_icon="⚠️",
    layout="centered"
)

st.title("⚠️ Multimodal AI Safety Assistant")

st.write(
    """
Upload an image and ask a question.
The assistant will analyze the image and identify the primary safety hazard.
"""
)

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

question = st.text_input(
    "Ask your question",
    value="What is the primary danger shown in this image?"
)

if uploaded_file:

    image = load_image(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Analyze Image"):

        with st.spinner("Analyzing image..."):

            answer = analyze_image(image, question)

        st.success("Analysis Complete")

        st.subheader("AI Response")

        st.write(answer)