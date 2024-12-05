from flask import Flask, send_file # type: ignore

app = Flask(__name__)

@app.route('/get_audio')
def get_audio():

    audio_file_path = 'C:/Users/adwai/Desktop/Third Eye/Backend/audio_files/sample.mp3'

    return send_file(audio_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='192.168.43.188', port=5000)