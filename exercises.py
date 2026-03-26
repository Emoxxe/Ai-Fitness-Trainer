from utils import calculate_angle

class Exercise:
    def __init__(self):
        self.counter = 0
        self.stage = None # "down" or "up"
        self.feedback = ""

    def process_landmarks(self, landmarks):
        raise NotImplementedError

class BicepCurl(Exercise):
    def process_landmarks(self, landmarks):
        # MediaPipe IDs: 11 (left shoulder), 13 (left elbow), 15 (left wrist)
        if len(landmarks) > 15:
            shoulder = [landmarks[11][1], landmarks[11][2]]
            elbow = [landmarks[13][1], landmarks[13][2]]
            wrist = [landmarks[15][1], landmarks[15][2]]

            angle = calculate_angle(shoulder, elbow, wrist)

            # Curl logic
            if angle > 160:
                self.stage = "down"
                self.feedback = "Curl up"
            if angle < 30 and self.stage == 'down':
                self.stage = "up"
                self.counter += 1
                self.feedback = "Full rep completed! Lower arms."
            elif angle < 30:
                self.feedback = "Lower arms"
            elif 30 <= angle <= 160 and self.stage == 'up':
                self.feedback = "Lower your arms further"
            elif 30 <= angle <= 160 and self.stage == 'down':
                self.feedback = "Curl up further"

            return angle
        return None

class Squat(Exercise):
    def process_landmarks(self, landmarks):
        # MediaPipe IDs: 23 (left hip), 25 (left knee), 27 (left ankle)
        if len(landmarks) > 27:
            hip = [landmarks[23][1], landmarks[23][2]]
            knee = [landmarks[25][1], landmarks[25][2]]
            ankle = [landmarks[27][1], landmarks[27][2]]

            angle = calculate_angle(hip, knee, ankle)

            # Squat logic
            if angle > 160:
                self.stage = "up"
                self.feedback = "Lower your squat"
            if angle < 90 and self.stage == 'up':
                self.stage = "down"
                self.counter += 1
                self.feedback = "Full rep completed! Stand up."
            elif angle < 90:
                self.feedback = "Stand up"
            elif 90 <= angle <= 160 and self.stage == 'down':
                self.feedback = "Stand up further"
            elif 90 <= angle <= 160 and self.stage == 'up':
                self.feedback = "Lower your squat more"
            
            return angle
        return None

class PushUp(Exercise):
    def process_landmarks(self, landmarks):
        # Using shoulder(11), elbow(13), wrist(15) angle for push up extension
        if len(landmarks) > 15:
            shoulder = [landmarks[11][1], landmarks[11][2]]
            elbow = [landmarks[13][1], landmarks[13][2]]
            wrist = [landmarks[15][1], landmarks[15][2]]

            angle = calculate_angle(shoulder, elbow, wrist)

            # Push-up logic
            if angle > 160:
                self.stage = "up"
                self.feedback = "Lower yourself"
            if angle < 90 and self.stage == 'up':
                self.stage = "down"
                self.counter += 1
                self.feedback = "Full rep completed! Push up."
            elif angle < 90:
                self.feedback = "Push up"
            elif 90 <= angle <= 160 and self.stage == 'down':
                self.feedback = "Push up further"
            elif 90 <= angle <= 160 and self.stage == 'up':
                self.feedback = "Lower yourself more"
                
            return angle
        return None
