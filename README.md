# 🧠 MindMirror – Cognitive Bias Detector (with OCR)

**MindMirror** is an AI-powered tool that detects cognitive biases in your writing — or even in **images containing text** (e.g., screenshots, notes, posters). It's like Grammarly for your thinking patterns.

Built with `Python`, `Streamlit`, and `Tesseract OCR`, this app analyzes textual content and highlights common cognitive biases such as **confirmation bias**, **negativity bias**, and **anchoring bias** — along with easy-to-understand explanations.

---

## 🚀 Features

✅ Upload or paste text  
✅ Upload `.txt`, `.jpg`, or `.png` files  
✅ OCR-powered text extraction from images  
✅ Rule-based bias detection using NLP  
✅ Visual and readable bias feedback

---

## 📸 Example Use Cases

- Detect bias in social media screenshots or news headlines  
- Analyze journal entries or blog drafts  
- Check personal writing for emotional reasoning patterns

---

## 📦 Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

You also need **Tesseract OCR** installed and configured.

### 🔧 Installing Tesseract (Windows)

1. Download from: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
2. Install and note the install path (e.g. `C:\Program Files\Tesseract-OCR	esseract.exe`)
3. In `app.py`, set:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## 🧪 Running the App

```bash
streamlit run app.py
```

Then open the URL shown in your browser (usually `http://localhost:8501`).

---

## 🧠 Supported Cognitive Biases (MVP)

- **Confirmation Bias**: Tendency to favor information that confirms existing beliefs.
- **Negativity Bias**: Overemphasis on negative outcomes or possibilities.
- **Anchoring Bias**: Reliance on the first piece of information encountered.

More biases can be added easily via `bias_rules.py`.

---

## 🛠 File Structure

```
mindmirror_ocr/
├── app.py               # Main Streamlit app
├── bias_rules.py        # Bias detection logic
├── explanations.py      # Explanations for each bias
├── requirements.txt     # Dependencies list
```

---

## 🌐 Deployment

To deploy this app on [Streamlit Cloud](https://share.streamlit.io):
1. Push your code to a GitHub repo
2. Go to `share.streamlit.io` and connect your repo
3. Set the entry file to `app.py`

---

## ✨ Future Ideas

- Bias severity scoring (0–100)
- Trend tracker (biases over time)
- GPT-based explanations
- More bias categories (optimism bias, sunk cost fallacy, etc.)

---

## 👤 Author

Developed by Sneha Chatwani 
🛠 Solo-built using Python, Streamlit, spaCy, and OCR  

---

## 📃 License

MIT License
