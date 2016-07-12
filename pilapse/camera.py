"""Handles the PiCamera module."""

from time import sleep
from picamera import PiCamera


def take_still(output_path):
    """Take a still picture."""
    camera = PiCamera()
    camera.start_preview()

    sleep(3)
    camera.capture("test.jpg")
    camera.stop_preview()
