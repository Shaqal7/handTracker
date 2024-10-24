# Hand Gesture Controlled Window Minimizer

This project uses Python along with OpenCV and MediaPipe to detect hand gestures via a webcam. When a specific gesture (clenching the thumb and forefinger) is detected, the currently active window is minimized.

## Features

- Real-time hand tracking using a webcam.
- Gesture recognition to minimize the active window.
- Uses OpenCV for video capture and display.
- Utilizes MediaPipe for hand landmark detection.
- Integrates with Windows API to control window states.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- pywin32

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/hand-gesture-minimizer.git
    cd hand-gesture-minimizer
    ```

2. Install the required packages:
    ```sh
    pip install opencv-python mediapipe numpy pywin32
    ```

## Usage

1. Run the script:
    ```sh
    python main.py
    ```

2. The webcam feed will open in a window. Show your hand to the camera.

3. When the thumb and forefinger tips are close to the palm center, the currently active window will be minimized.

4. Press 'q' to quit the application.

## Code Overview

- `main.py`: The main script that captures video, processes hand landmarks, and minimizes the window based on the detected gesture.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [pywin32](https://github.com/mhammond/pywin32)

Feel free to contribute to this project by submitting issues or pull requests.