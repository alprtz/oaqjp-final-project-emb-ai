import requests 
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 200:
        try:
            formatted_response = response.json() 
            
            anger = formatted_response["emotionPredictions"][0]["emotion"].get("anger", 0)
            disgust = formatted_response["emotionPredictions"][0]["emotion"].get("disgust", 0)
            fear = formatted_response["emotionPredictions"][0]["emotion"].get("fear", 0)
            joy = formatted_response["emotionPredictions"][0]["emotion"].get("joy", 0)
            sadness = formatted_response["emotionPredictions"][0]["emotion"].get("sadness", 0)

            
            list_of_emotions = [anger, disgust, fear, joy, sadness]
            dominant_emotion_index = list_of_emotions.index(max(list_of_emotions))
            emotion_keys = ["anger", "disgust", "fear", "joy", "sadness"]
            dominant_emotion_key = emotion_keys[dominant_emotion_index]

        except KeyError as e:
            print(f"Error parsing response: {e}")
            anger = disgust = fear = joy = sadness = None
            dominant_emotion_key = None

    elif response.status_code == 400:
        anger = disgust = fear = joy = sadness = None
        dominant_emotion_key = None
        print("Bad request (400) received")

    result = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion_key
    }
    
    return result

