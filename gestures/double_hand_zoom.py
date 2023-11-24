"""Image zoom gesture."""

import cv2
import pyautogui

import gestures.gesture


class ImageZoomGesture(gestures.gesture.Gesture):
    """Image zoom gesture."""

    startDist = None
    startLength = None
    scale = 0
    cx, cy = 500, 500

    def zoom(self, distance):
        if abs(distance) > 3.5:
            pyautogui.keyDown('ctrl')
            pyautogui.scroll(int(distance*5))
            pyautogui.keyUp('ctrl')

    def run(self, detector, image, hands):
        """Run gesture."""
        if len(hands) == 2:

            if detector.fingers_up(hands[0]) == [1, 1, 0, 0, 0] and detector.fingers_up(
                hands[1]
            ) == [1, 1, 0, 0, 0]:

                length, info, image = detector.findDistance(
                    hands[0]["center"],
                    hands[1]["center"],
                    image,
                )
                
                if self.startDist is None:
                    self.startDist = length

                self.scale = int((length - self.startDist) // 2)
                self.cx, self.cy = info[4:]

                if self.startLength is not None:
                    distance = length - self.startLength
                    self.zoom(distance)

                self.startLength = length

        else:
            self.startDist = None
            self.startLength = None

        try:
            h1, w1, _ = image.shape
            new_h, new_w = ((h1 + self.scale) // 2) * 2, ((w1 + self.scale) // 2) * 2
            image = cv2.resize(image, (new_w, new_h))

            image[
                self.cy - new_h // 2 : self.cy + new_h // 2,
                self.cx - new_w // 2 : self.cx + new_w // 2,
            ] = image
        except:
            pass
