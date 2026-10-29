
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid input! Please enter some text.", 400

    result = emotion_detector(text_to_analyze)

    if not result or result.get("dominant_emotion") is None:
        return "Unable to detect emotions. Please try again.", 400

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
