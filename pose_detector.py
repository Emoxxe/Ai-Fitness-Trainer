import cv2
import mediapipe as mp

class PoseDetector:
    def __init__(self, mode=False, complexity=1, smooth=True, detect_con=0.5, track_con=0.5):
        self.mode = mode
        self.complexity = complexity
        self.smooth = smooth
        self.detect_con = detect_con
        self.track_con = track_con

        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.pose = self.mp_pose.Pose(
            static_image_mode=self.mode,
            model_complexity=self.complexity,
            smooth_landmarks=self.smooth,
            min_detection_confidence=self.detect_con,
            min_tracking_confidence=self.track_con
        )
        self.results = None

    def find_pose(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)
        
        if self.results.pose_landmarks and draw:
            self.mp_drawing.draw_landmarks(
                img, 
                self.results.pose_landmarks, 
                self.mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style()
            )
        return img

    def get_landmarks(self, img):
        landmarks = []
        if self.results and self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append([id, cx, cy, lm.visibility])
        return landmarks
