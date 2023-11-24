"""Gesture registry."""

import gestures.double_hand_zoom
import gestures.single_hand_left_mouse_down
import gestures.single_hand_right_mouse_down
import gestures.single_hand_track


class GestureRegistry:
    """Gesture registry."""

    registry = []

    def register(self, gesture):
        """Register a gesture."""
        self.registry.append(gesture())


REGISTRY = GestureRegistry()
REGISTRY.register(gestures.double_hand_zoom.ImageZoomGesture)
REGISTRY.register(gestures.single_hand_left_mouse_down.SingleHandLeftMouseDown)
REGISTRY.register(gestures.single_hand_right_mouse_down.SingleHandRightMouseDown)
REGISTRY.register(gestures.single_hand_track.SingleHandTrack)
