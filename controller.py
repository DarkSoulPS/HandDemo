"""Show camera stream in a display controller."""

import cv2

import detectors.hand_tracker
import gestures.registry
import video.camera


class Controller:
    """Shows a camera stream in a display controller."""

    def __init__(self):
        self.camera = video.camera.Camera()
        self.camera.start()
        self.detector = detectors.hand_tracker.HandDetector(detectionCon=0.8)
        self.gesture_registry = gestures.registry.REGISTRY

    def start(self) -> None:
        """Open display controller."""
        while self.camera.is_streaming:

            image = self.camera.photograph()
            hands, marked_image = self.detector.findHands(image)

            self.run(self.detector, image, hands)

            cv2.imshow("Camera stream", marked_image)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self._stop()

    def run(self, detector, image, hands):
        """Run gesture controls."""
        for gesture in self.gesture_registry.registry:
            gesture.run(detector, image, hands)

    def _stop(self) -> None:
        """Open display controller."""
        self.camera.shutdown()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    controller = Controller()
    controller.start()
