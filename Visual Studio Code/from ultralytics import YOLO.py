from ultralytics import YOLO
import cv2

# =========================
# 1. Load your trained model
# =========================
model = YOLO("best.pt")  # make sure best.pt is in same folder

# =========================
# 2. YOUR ESP32 STREAM URL
# =========================
url = "http://10.14.225.164:81/stream"

# Open video stream
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("❌ Cannot open ESP32 stream")
    exit()

# =========================
# 3. LIVE YOLO DETECTION LOOP
# =========================
while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to grab frame")
        break

    # Run YOLO model
    results = model(frame)

    # Draw detections
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("PPE Detection - ESP32 + YOLO", annotated_frame)

    # press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()