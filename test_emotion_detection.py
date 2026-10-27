"""Live Watson acceptance tests; run inside the Skills Network environment."""

import os
import unittest

from EmotionDetection import emotion_detector


@unittest.skipUnless(os.environ.get("RUN_WATSON_TESTS") == "1",
                     "Set RUN_WATSON_TESTS=1 in a Watson-enabled environment")
class TestEmotionDetection(unittest.TestCase):
    """Verify the five statements required by the course against real Watson."""

    def test_required_emotions(self):
        """Assert each specified statement's dominant emotion."""
        cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        for statement, expected in cases.items():
            with self.subTest(statement=statement):
                self.assertEqual(emotion_detector(statement)["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main()
