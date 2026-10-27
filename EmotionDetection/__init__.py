"""Emotion detection package backed by IBM Watson NLP."""

# The package name is required by the course's import contract.
# pylint: disable=invalid-name

from .emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
