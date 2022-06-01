import cv2
import mediapipe as mp

class Chehro:
    def __init__(self, image):
        self.image = image 

    def detect(self, draw=True):
        mp_face_detection = mp.solutions.face_detection
        mp_drawing = mp.solutions.drawing_utils

        image = self.image

        with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
             image.flags.writeable = False
             image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
             results = face_detection.process(image)

             bounding_boxes = []
             for face in results.detections:
                x_min = face.location_data.relative_bounding_box.xmin
                y_min = face.location_data.relative_bounding_box.ymin

                x_max = face.location_data.relative_bounding_box.xmin + face.location_data.relative_bounding_box.width
                y_max = face.location_data.relative_bounding_box.ymin + face.location_data.relative_bounding_box.height

                rect_start = mp_drawing._normalized_to_pixel_coordinates(x_min, y_min, image.shape[1], image.shape[0])
                rect_end = mp_drawing._normalized_to_pixel_coordinates(x_max, y_max, image.shape[1], image.shape[0])

                bounding_boxes.append([x_min, y_min, x_max, y_max])

                if draw:
                    cv2.rectangle(image, rect_start, rect_end, (0, 255, 0), 2)
                
        return image, bounding_boxes