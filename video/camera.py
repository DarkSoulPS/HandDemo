"""Camera interface."""

import numpy as np

import video.stream

DEFAULT_CAMERA_INDEX = 0


class Camera:
    """Camera interface."""

    def __init__(self, device_index=DEFAULT_CAMERA_INDEX):
        self._stream = video.stream.Stream(device_index)

    @property
    def is_streaming(self) -> bool:
        """Whether the camera is streaming.

        Returns:
            Whether camera is streaming or not.
        """
        return self._stream.capture.isOpened()

    def start(self):
        """Start up the camera."""
        self._stream.start()

    def photograph(self) -> np.ndarray:
        """Take a photograph.

        Returns:
            Camera frame.
        """
        return self._stream.frame

    def shutdown(self):
        """Shut down the camera."""
        self._stream.stop()
