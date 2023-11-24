"""Single hand click."""

import gestures

import pyautogui

CLOSED_FIST = [0, 0, 0, 0, 0]

pyautogui.FAILSAFE = False


class SingleHandRightMouseDown(gestures.gesture.Gesture):
    """Track single hand click."""

    mouse_down = False

    def run(self, detector, image, hands):
        """Run gesture."""
        if len(hands) == 1:
            # 1. Check which fingers are up
            fingers = detector.fingers_up(hands[0])

            # 2. Index finger is up (Clicking gesture)
            if fingers == CLOSED_FIST and not self.mouse_down:
                pyautogui.mouseDown(button='right')
                self.mouse_down = True

            if fingers != CLOSED_FIST and self.mouse_down:
                pyautogui.mouseUp(button='right')
                self.mouse_down = False
