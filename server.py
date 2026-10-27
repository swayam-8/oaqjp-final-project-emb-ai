"""Serve the Emotion Detector interface and Watson-backed predictions."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the feedback analysis form."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze textToAnalyze and return the required readable response."""
    text = request.args.get("textToAnalyze", "")
    if len(text) > 10000:
        return "Text is too long. Please use at most 10,000 characters.", 400
    try:
        result = emotion_detector(text)
    except RuntimeError:
        app.logger.warning("Watson emotion prediction failed")
        return "Emotion service unavailable. Please try again later.", 503
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
