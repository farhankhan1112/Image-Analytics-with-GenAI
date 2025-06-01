# Image-Analytics-with-GenAI
This project is a simple Streamlit web application that allows users to upload an image and ask a question about it using Google Gemini AI.

# Features
- Upload an image (PNG, JPG, JPEG).
- Enter a text prompt for analyzing the image.
- Uses **Google Gemini AI** to provide insights based on the image and prompt.

# Project Interface :
- Interactive chat interface
- Easy to Use

![Alt text](https://github.com/farhankhan1112/Image-Analytics-with-GenAI/blob/53f8e0fadb1110192800013b36aee7baaff75688/Screenshot/Project%20Interface.png)

# Project Output :
![Alt text](https://github.com/farhankhan1112/Image-Analytics-with-GenAI/blob/53f8e0fadb1110192800013b36aee7baaff75688/Screenshot/Project%20output.png)

# 1️⃣ Upload an Image
- The user uploads an image (PNG, JPG, JPEG) by:
- Dragging and dropping it, or
- Clicking the Browse Files button.

# 2️⃣ Enter a Text Query
- Who is that actor?

# 3️⃣ AI-Powered Response Generation
- The AI analyzes the image and the question together.
- Based on the visual and text input, the AI generates a response like:
- That's Shah Rukh Khan. He's a very famous Indian actor, often referred to as "King Khan" in Bollywood.

# 4️⃣ Response Display
- The response is displayed on the Streamlit web page below the image.
- The user can see both the image and the response in one place.

# Technologies Used
- **Streamlit** - For building the web UI.
- **Google Generative AI (Gemini)** - For image understanding and text response.
- **PIL (Pillow)** - For image processing.


# Set Up API Key  
You need a **Google Gemini API Key** to use this application. Replace the `api_key` variable in `app.py` with your own API key.

# Run the Application
```bash
streamlit run app.py
```

# License
This project is for educational purposes only.

---

# **Notes**
- Ensure your API key is **valid and active**.
- The Gemini model supports multimodal inputs, so make sure you pass **both** the image and the text correctly.
