import streamlit as st
from PIL import Image
import pytesseract
from bias_rules import detect_biases
from explanations import explain_bias
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


st.set_page_config(page_title="MindMirror – Cognitive Bias Detector (with OCR)")
st.title("🧠 MindMirror: Bias Detector with OCR")
st.markdown("Upload text, a .txt file, or an image containing text. The app will detect cognitive biases.")


user_input = ""

uploaded_file = st.file_uploader("Upload a .txt or .png/.jpg image file", type=["txt", "png", "jpg", "jpeg"])
if uploaded_file is not None:
    if uploaded_file.name.endswith(".txt"):
        user_input = uploaded_file.read().decode("utf-8")
    elif uploaded_file.name.endswith((".png", ".jpg", ".jpeg")):
        image = Image.open(uploaded_file)
        user_input = pytesseract.image_to_string(image)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        st.text_area("Extracted Text from Image", value=user_input, height=150, disabled=True)

if not user_input:
    user_input = st.text_area("Or type/paste text here:", height=200)

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter or upload some text.")
    else:
        biases = detect_biases(user_input)
        if biases:
            st.success(f"Detected biases: {', '.join(biases)}")
            for bias, explanation in zip(biases, explain_bias(biases)):
                st.markdown(f"**{bias.replace('_', ' ').title()}**: {explanation}")
        else:
            st.info("No known biases detected. Well done!")
