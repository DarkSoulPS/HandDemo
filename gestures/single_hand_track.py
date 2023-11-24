"""Mouse control gesture."""

import autopy
import numpy as np

import gestures.gesture

ORIGIN = 0, 0

FRAME_R = 100
SMOOTHENING = 4

SCREEN_WIDTH, SCREEN_HEIGHT = autopy.screen.size()


class SingleHandTrack(gestures.gesture.Gesture):
    """Track single hand movement."""

    def run(self, detector, image, hands):
        """Run gesture."""
        image_w = image.shape[1]
        image_h = image.shape[0]

        if len(hands) == 1:
            # 1. Get the tip of the index and middle fingers
            landmarks, _ = detector.findPosition(image)
            landmarks = hands[0]["lmList"]
            x1, y1 = (
                int((landmarks[0][0] + landmarks[5][0] + landmarks[17][0]) / 3),
                int((landmarks[0][1] + landmarks[5][1] + landmarks[17][1]) / 3),
            )

            # 2. Convert coordinates
            x3 = np.interp(x1, (FRAME_R, image_w - FRAME_R), (ORIGIN[0], SCREEN_WIDTH))
            y3 = np.interp(y1, (FRAME_R, image_h - FRAME_R), (ORIGIN[1], SCREEN_HEIGHT))

            # 3. Smoothen values
            self.current_x = self.previous_x + (x3 - self.previous_x) / SMOOTHENING
            self.current_y = self.previous_y + (y3 - self.previous_y) / SMOOTHENING

            # 4. Move mouse
            autopy.mouse.move(SCREEN_WIDTH - self.current_x, self.current_y)
            self.previous_x, self.previous_y = self.current_x, self.current_y
