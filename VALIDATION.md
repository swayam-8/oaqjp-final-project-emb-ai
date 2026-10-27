# Verified in Skills Network lab — 27 October 2026

- Cloned this public fork into `/home/project/final_project`.
- Installed requirements successfully.
- `RUN_WATSON_TESTS=1 python3 -m unittest test_emotion_detection -v`: passed. This executes five subtests using the five required statements and real Watson predictions.
- `python3 -m pylint server.py EmotionDetection`: 10.00/10.
- Started Flask on port 5000 using the lab preview.
- Browser test `I think I am having fun`: joy, score 0.876574; anger 0.029103195; disgust 0.0067921067; fear 0.027528232; sadness 0.06151191.
- Browser blank-input test: `Invalid text! Please try again!`.

Screenshots were captured from the real app. No graded submission or own-work declaration was made. The implementation was AI-assisted; the learner should review it and comply with course rules.
