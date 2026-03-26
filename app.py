import streamlit as st
import cv2
import av
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
from pose_detector import PoseDetector
from exercises import BicepCurl, Squat, PushUp

st.set_page_config(page_title="AI Fitness Trainer", layout="wide")
st.title("AI Fitness Trainer 🏋️‍♂️")
st.markdown("Real-time pose detection and exercise feedback via WebRTC.")

# Sidebar
st.sidebar.header("Settings")
exercise_mode = st.sidebar.selectbox("Choose Exercise", ["Bicep Curl", "Squat", "Push-up"])

# WebRTC Video Processor Class
class PoseVideoProcessor:
    def __init__(self):
        self.detector = PoseDetector(detect_con=0.5, track_con=0.5)
        self.mode = "Bicep Curl"
        self.exercise = BicepCurl()

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")
        
        img = self.detector.find_pose(img, draw=True)
        landmarks = self.detector.get_landmarks(img)

        if landmarks:
            angle = self.exercise.process_landmarks(landmarks)
            
            if angle is not None:
                # Top left margin for text
                cv2.rectangle(img, (0, 0), (700, 180), (0, 0, 0), -1)
                
                # Display Angle
                cv2.putText(img, f"Angle: {int(angle)}", (10, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                
                # Display Reps
                cv2.putText(img, f"Reps: {self.exercise.counter}", (10, 100), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3, cv2.LINE_AA)
                
                # Display Feedback
                cv2.putText(img, f"Feedback: {self.exercise.feedback}", (10, 150), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2, cv2.LINE_AA)

        return av.VideoFrame.from_ndarray(img, format="bgr24")

# Configure WebRTC ICE servers for STUN/TURN 
# (Necessary for real-world cloud deployment NAT traversal)
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

# Start WebRTC Streamer
ctx = webrtc_streamer(
    key="pose-estimation",
    video_processor_factory=PoseVideoProcessor,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True
)

# If the video stream is active, update the processor's exercise state if the user changes the UI dropdown
if ctx.video_processor:
    if ctx.video_processor.mode != exercise_mode:
        ctx.video_processor.mode = exercise_mode
        if exercise_mode == "Bicep Curl":
            ctx.video_processor.exercise = BicepCurl()
        elif exercise_mode == "Squat":
            ctx.video_processor.exercise = Squat()
        else:
            ctx.video_processor.exercise = PushUp()

st.markdown("---")
st.markdown("**Instructions:** Ensure you grant camera permissions to the browser. Step back so your full body (or upper body) is visible to the camera for accurate tracking.")
