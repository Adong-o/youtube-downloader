#from flask import Flask, render_template, request, jsonify
#from ytdownload import download_video

#app = Flask(__name__)

#@app.route('/')
#def index():
  #  return render_template('index.html')

#@app.route('/download', methods=['POST'])
#def handle_download():
 #   data = request.json
 #   video_url = data.get('videoUrl')
  #  save_directory = r"C:\Users\HP\Desktop\yt download"

   # if not video_url:
   #     return jsonify({'message': 'Please enter youtube link'}), 400

   # try:
    #    download_video(video_url, save_directory)
     #   return jsonify({'message': 'Download completed!', 'path': save_directory})
   # except Exception as e:
   #     return jsonify({'message': 'Download failed', 'error': str(e)}), 500

#if __name__ == '__main__':
 #   app.run(debug=True)

import os
from flask import Flask, render_template, request, jsonify
from ytdownload import download_video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def handle_download():
    data = request.json
    video_url = data.get('videoUrl')

    if not video_url:
        return jsonify({'message': 'Please enter a YouTube link'}), 400

    try:
        # Dynamically determine the user's download directory
        username = os.getlogin()
        download_directory = os.path.join('C:\\Users', username, 'Downloads')
        
        # Download the video to the user's download directory
        download_video(video_url, download_directory)
        
        return jsonify({'message': 'Download completed!', 'path': download_directory})
    except Exception as e:
        return jsonify({'message': 'Download failed', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
