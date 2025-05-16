import streamlit as st
import cv2
import numpy as np
from PIL import Image

# App Configuration
st.set_page_config(
    page_title="AI Cosmetic Preview",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Main Title ---
st.title("AI-Powered Cosmetic Procedure Preview")
st.markdown("""
This prototype shows a visual prediction of facial appearance after common cosmetic procedures such as **Botox** and **fillers**.  
> *Note: This is a simulated preview for demonstration only.*
""")

# --- Upload Image ---
uploaded_file = st.file_uploader("Upload a face image", type=["jpg", "jpeg", "png"])

# --- Cosmetic Simulation Logic ---
def simulate_cosmetic_procedure(image):
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    smoothed = cv2.bilateralFilter(image, d=15, sigmaColor=75, sigmaSpace=75)
    result_image = cv2.cvtColor(smoothed, cv2.COLOR_BGR2RGB)
    return Image.fromarray(result_image)

# --- Display Results ---
if uploaded_file:
    col1, col2 = st.columns(2)

    original_image = Image.open(uploaded_file)
    processed_image = simulate_cosmetic_procedure(original_image)

    with col1:
        st.subheader("👈 Original")
        st.image(original_image, use_container_width=True)

    with col2:
        st.subheader("👉 Predicted (After)")
        st.image(processed_image, use_container_width=True)

    st.markdown("✅ *This simulation smooths skin and enhances softness to represent typical Botox/filler effects.*")

else:
    st.warning("Please upload a facial image to begin.")

# --- Footer ---
st.markdown("---")
st.markdown(
    "<small>Prototype built for demonstration. Not medical advice. Final AI model will provide personalized, data-driven predictions.</small>",
    unsafe_allow_html=True
)
