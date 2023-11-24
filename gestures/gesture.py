"""Gesture abstract class."""

import abc

ORIGIN = 0, 0


class Gesture(abc.ABC):
    """Gesture abstract class."""

    previous_x, previous_y = ORIGIN
    current_x, current_y = ORIGIN

    @abc.abstractmethod
    def run(self, detector, image, hands):
        """Run gesture."""
