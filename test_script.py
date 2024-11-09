# test_script.py (in the parent directory of EmotionDetection)

from EmotionDetection.emotion_detection import emotion_detector

# Test the function with a text
text = "I hate working long hours."
result = emotion_detector(text)
print(result)