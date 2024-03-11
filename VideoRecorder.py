import cv2

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Unable to access camera")
        return

    record = False
    recording = False
    filter_contrast = False
    filter_brightness = False
    flip = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame")
            break

        if filter_contrast:
            frame = cv2.convertScaleAbs(frame, alpha=2.0, beta=0)
        if filter_brightness:
            frame = cv2.convertScaleAbs(frame, alpha=1.0, beta=50)
        if flip:
            frame = cv2.flip(frame, 1)

        if record:
            if not recording:
                frame_height, frame_width, _ = frame.shape
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))
                recording = True
            cv2.circle(frame, (50, 50), 30, (0, 0, 255), -1)  # Red circle to indicate recording

        cv2.imshow('Video Recorder', frame)

        key = cv2.waitKey(1)
        if key == 27:  # ESC key to exit
            break
        elif key == ord('p'):  # 'p' key to toggle record mode
            record = not record
        elif key == ord('c'):  # 'c' key to toggle contrast filter
            filter_contrast = not filter_contrast
        elif key == ord('b'):  # 'b' key to toggle brightness filter
            filter_brightness = not filter_brightness
        elif key == ord('f'):  # 'f' key to toggle flip
            flip = not flip

        if key == ord(' '):  # ' ' key to toggle record mode
            if record:
                record = False
                recording = False
                if recording:
                    out.release()
            else:
                record = True

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
