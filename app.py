import face_recognition
import cv2

# Database of known faces and names
known_faces = []
known_names = []

# Function to load known faces
def load_known_faces():
    # Load and encode known faces (Replace with your images and names)
    image_paths = ["path/to/your/image1.jpg", "path/to/your/image2.jpg"]  # Replace with your image paths
    for path in image_paths:
        image = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(image)[0]  # Assuming one face per image
        known_faces.append(encoding)
        # Extract name from the file name or add it manually
        name = path.split('/')[-1].split('.')[0]  # Extracting name from file path
        known_names.append(name)

def recognize_faces(image):
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        # Draw rectangle and display name
        top, right, bottom, left = face_recognition.face_locations(image)[0]
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(image, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

    return image

# Load known faces
load_known_faces()

# Process images
image_paths = ["path/to/your/test_image1.jpg", "path/to/your/test_image2.jpg"]  # Replace with test image paths
for path in image_paths:
    img = cv2.imread(path)
    output_img = recognize_faces(img)
    cv2.imshow('Facial Recognition', output_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
q
