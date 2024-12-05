import requests # type: ignore
import json
import time
import base64
from gtts import gTTS # type: ignore
import os
import glob
MONITOR_FOLDER="C:/Users/adwai/Desktop/Third Eye/Backend/received_images"
sent_files = set()
language = "en"
while True:
     
    files = set(os.listdir(MONITOR_FOLDER))

     
    new_files = files - sent_files

     
    if new_files:
        time.sleep(2)
        first_file = list(new_files)[0]  
        if first_file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_path = os.path.join(MONITOR_FOLDER, first_file)
            sent_files.add(first_file)
    else:
        continue

   

    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llava",
        "prompt": "what is infront of me? do not say image anywhere in the response.",
        "stream": False,
        "images": [encoded_string]
    }


    response = requests.post(url, data=json.dumps(payload))


    substring_start = response.text.find('"response":"') + len('"response":"')
    substring_end = response.text.find('","done"')
    output = response.text[substring_start:substring_end]

    print(output)



    audio_folder = "C:/Users/adwai/Desktop/Third Eye/Backend/audio_files"

   
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
    else:
        
        files = glob.glob(os.path.join(audio_folder, "*.mp3"))
        for file in files:
            os.remove(file)

   
    audio_path = os.path.join(audio_folder, "sample.mp3")
    speech = gTTS(text=output, lang=language, slow=False)
    speech.save(audio_path)

    time.sleep(1)


