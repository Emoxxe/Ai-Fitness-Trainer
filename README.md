# 🏋️‍♂️ AI Fitness Trainer

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-00A67E?logo=google)

An AI-powered web application that acts as your personal fitness trainer. It uses your webcam to track your body movements in real-time, counts your repetitions, calculates your joint angles, and provides live feedback to ensure you are doing your exercises with the correct form!

🔴 **[Try the Live Web App Here!](https://ai-fitness-trainer-mgpw6cetsfekmvf954hlox.streamlit.app/)**

---

## ✨ Features
* **Real-time Skeleton Tracking:** Uses `mediapipe` to securely track body landmarks directly in your browser using `WebRTC`.
* **Exercise Recognition:** Supports customized tracking for **Bicep Curls**, **Squats**, and **Push-ups**.
* **Repetition Counter:** Automatically increments only when a full range of motion is achieved.
* **Live Form Feedback:** Tells you when to "Keep your back straight" or "Lower your squat more" using math and joint-angle calculations (`numpy`).

---

## 💻 Tech Stack
* **Frontend/UI:** [Streamlit](https://streamlit.io/)
* **Computer Vision:** [MediaPipe](https://developers.google.com/mediapipe) & [OpenCV](https://opencv.org/)
* **Math & Engine:** Python & NumPy
* **Live Streaming:** `streamlit-webrtc`

---

## 🚀 How to Run Locally

If you want to run this application on your own computer:

1. Clone this repository to your machine.
2. Ensure you have Python 3.12 installed.
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```
5. Allow camera permissions and start your workout!
