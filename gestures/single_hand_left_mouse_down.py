"""Single hand click."""

import gestures

import pyautogui

THUMB_INDEX_MIDDLE = [1, 1, 1, 0, 0]

pyautogui.FAILSAFE = False


class SingleHandLeftMouseDown(gestures.gesture.Gesture):
    """Track single hand click."""

    mouse_down = False

    def run(self, detector, image, hands):
        """Run gesture."""
        if len(hands) == 1:
            # 1. Check which fingers are up
            fingers = detector.fingers_up(hands[0])

            # 2. Index finger is up (Clicking gesture)
            if fingers == THUMB_INDEX_MIDDLE and not self.mouse_down:
                pyautogui.mouseDown()
                self.mouse_down = True

            if fingers != THUMB_INDEX_MIDDLE and self.mouse_down:
                pyautogui.mouseUp()
                self.mouse_down = False
