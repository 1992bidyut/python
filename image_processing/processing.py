# https://www.youtube.com/watch?v=6wI6tzRogZQ
import cv2
rtsp_url = 'rtsp://192.168.0.44:554/Streaming/Channels/1'

cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
# cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    print("Video Width:", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("Video Height:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("Video FPS:", cap.get(cv2.CAP_PROP_FPS))
    # exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break
    cv2.imshow('IP Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()