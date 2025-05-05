# Image-Analytics-with-GenAI
This project is a simple Streamlit web application that allows users to upload an image and ask a question about it using Google Gemini AI.

# Features
- Upload an image (PNG, JPG, JPEG).
- Enter a text prompt for analyzing the image.
- Uses **Google Gemini AI** to provide insights based on the image and prompt.



### Set Up API Key  
You need a **Google Gemini API Key** to use this application. Replace the `api_key` variable in `app.py` with your own API key.

### Run the Application
```bash
streamlit run app.py
```

## Usage
1. Upload an image.
2. Enter a text prompt to analyze the image.
3. Click the **"Get RESPONSE"** button to receive AI-generated insights.

## Technologies Used
- **Streamlit** - For building the web UI.
- **Google Generative AI (Gemini)** - For image understanding and text response.
- **PIL (Pillow)** - For image processing.

## License
This project is for educational purposes only.

---

### **Notes**
- Ensure your API key is **valid and active**.
- The Gemini model supports multimodal inputs, so make sure you pass **both** the image and the text correctly.
