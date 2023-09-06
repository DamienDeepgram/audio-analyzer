import os
import json
from flask import Flask, request
from mutagen.mp3 import MP3
# import soundfile as sf
from soundfile import SoundFile
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/info', methods=['POST', 'GET'])
@cross_origin()
def predictWithDb():
  print('info', request.method)
  if request.method == 'POST':
    print('info')
    save_path = os.path.join('./audio/', "temp.mp3")
    request.files['music_file'].save(save_path)
    audio_info = MP3('./audio/temp.mp3').info

    data = SoundFile('./audio/temp.mp3')
    print('soundfile info')
    print('channels:', data.channels)
    print('format:', data.format)
    # print('subtype_info:', data.subtype_info)
    print('subtype:', data.subtype)
    print('extra_info:', data.extra_info)
    print('format_info:', data.format_info)
    # print(samplerate)
    data.close()
    # print('mutagen info')
    # print('sketchy', audio_info.sketchy)
    # print('mode', audio_info.mode)
    # print('version', audio_info.version)
    # print('layer', audio_info.layer)
    # print('protected', audio_info.protected)
    # print('padding', audio_info.padding)
    print('bitrate', audio_info.bitrate)
    print('sample_rate', audio_info.sample_rate)
    # print('length', audio_info.length)

    bitrate = audio_info.bitrate
    sample_rate = audio_info.sample_rate
    channels = data.channels
    # print('xxx', channels)
    # info = ''
    # info2 = '' + str(data.extra_info)#[:] #.split("\n").join(' - ') #replace("\\r\\n", " - ")
    # print('xxx', info2)
    x = '{"bitrate": %d, "sample_rate": %d, "channels": %d}' % (
      bitrate, sample_rate, channels)
    print(x)
    y = json.loads(x)
    return y


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3000)
