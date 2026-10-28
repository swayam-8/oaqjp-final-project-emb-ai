# Final Project

Emotion detection with Watson NLP and Flask. Forked from the IBM course starter; starter UI and license retained.

Implementation was prepared with AI assistance. Review and understand the code and follow course rules before any submission.

## Run

```sh
python3 -m pip install -r requirements.txt
python3 server.py
```

Open port 5000. Watson must be reachable from the Skills Network lab.

## Live acceptance tests

```sh
RUN_WATSON_TESTS=1 python3 -m unittest test_emotion_detection -v
```

## Static analysis

```sh
python3 -m pip install -r requirements-dev.txt
python3 -m pylint server.py EmotionDetection
```

Local adapter checks passed in the separate emotion-detector-flask repository; live Watson requests from that environment returned HTTP 503. Course lab verification succeeded: all five Watson acceptance cases passed and Pylint scored 10.00/10. See VALIDATION.md. No graded submission has been made.
