"""Call the Watson NLP emotion endpoint and normalize its response."""

import json
import math
import os

import requests

EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")
DEFAULT_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)


def _empty_result():
    """Return the documented invalid-input result."""
    return dict.fromkeys((*EMOTIONS, "dominant_emotion"))


def emotion_detector(text_to_analyze):
    """Return five emotion scores and the highest-scoring emotion.

    Blank input and Watson HTTP 400 responses return None for every key.
    Transport failures and invalid upstream payloads raise RuntimeError;
    these must not be presented as successful predictions.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()
    try:
        response = requests.post(
            os.environ.get("WATSON_EMOTION_URL", DEFAULT_URL),
            json={"raw_document": {"text": text_to_analyze}},
            headers={
                "grpc-metadata-mm-model-id":
                "emotion_aggregated-workflow_lang_en_stock"
            },
            timeout=20,
        )
        if response.status_code == 400:
            return _empty_result()
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError("Emotion service is unavailable.") from exc

    try:
        payload = json.loads(response.text)
        scores = payload["emotionPredictions"][0]["emotion"]
        result = {name: float(scores[name]) for name in EMOTIONS}
        if any(not math.isfinite(value) or not 0 <= value <= 1
               for value in result.values()):
            raise ValueError("Emotion scores must be finite and between 0 and 1.")
    except (ValueError, TypeError, KeyError, IndexError) as exc:
        raise RuntimeError("Emotion service returned an invalid response.") from exc
    result["dominant_emotion"] = max(result, key=result.get)
    return result
