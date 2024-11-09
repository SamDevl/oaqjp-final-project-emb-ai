"""
This is the starting file of the server.
It serves api request with appropriate response
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    This function handles the incoming request to analyze the emotions in a given text.
    
    It retrieves the text from the query parameters, passes it to the emotion detection 
    system, and processes the response to extract the emotional scores for 'anger', 
    'disgust', 'fear', 'joy', and 'sadness'. It then checks if the dominant emotion is 
    available and returns a formatted string with the results. If the dominant emotion is 
    not available, it returns a message indicating an invalid input.

    Returns:
        str: A formatted string displaying the emotional scores and dominant emotion.
             If no dominant emotion is found, a message indicating invalid input is returned.
    """
    # Retrieve text to analyze from the request query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detector with the provided text
    response = emotion_detector(text_to_analyze)

    # Extract the emotion scores and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # If there's no dominant emotion, return an error message
    if dominant_emotion is None:
        return "Invalid text! Please try again."

    # Return the formatted result
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
@app.route("/")
def render_index_page():
    """
    It starts server on defined server and port for development. 
    """
    return render_template('index.html')

# Running the application on localhost:5000
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Running on localhost:5000
