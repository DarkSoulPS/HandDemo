"""Video stream interface."""

import time
import threading

# import autopy
import cv2

CAMERA_WARMUP_SECONDS = 2
FRAME_GRAB_WARMUP_SECONDS = 1

# SCREEN_WIDTH, SCREEN_HEIGHT = autopy.screen.size()


class Stream:
    """Camera video stream handler."""

    def __init__(self, device_index):
        self._device_index = device_index
        self.capture = None
        self.frame = None

    def start(self) -> None:
        """Start video stream."""
        self.capture = cv2.VideoCapture(self._device_index)
        # self.capture.set(3, SCREEN_WIDTH)
        # self.capture.set(4, SCREEN_WIDTH)
        time.sleep(CAMERA_WARMUP_SECONDS)
        self._stream()

    def _stream(self) -> None:
        """Start thread to stream frames from the camera."""
        thread = threading.Thread(target=self._read_frames)
        thread.daemon = True
        thread.start()
        time.sleep(FRAME_GRAB_WARMUP_SECONDS)

    def _read_frames(self) -> None:
        """Continuously read frames from the camera."""
        while True:
            self._read_frame()

    def _read_frame(self) -> None:
        """Read a single frame from the camera while stream is open."""
        if self.capture.isOpened():
            _, self.frame = self.capture.read()

    def stop(self) -> None:
        """Stop video stream."""
        self.capture.release()
