#import os
#from pytube import YouTube

#def on_progress(stream, chunk, bytes_remaining):
 #   total_size = stream.filesize
  #  bytes_downloaded = total_size - bytes_remaining
   # percentage = (bytes_downloaded / total_size) * 100
   # print(f"Downloading... {percentage:.2f}% done")

#def download_video(video_url, save_directory):
  #  try:
   #     yt = YouTube(video_url, on_progress_callback=on_progress)
   #     stream = yt.streams.get_highest_resolution()  
    #    print("Downloading:", yt.title)
        
     #   filename = ''.join(c for c in yt.title if c.isalnum() or c in [' ', '.', '_']).rstrip()
        
      #  save_path = os.path.join(save_directory, filename + ".mp4")
        
       # stream.download(output_path=save_directory, filename=filename)
        
       # print("Download completed! Saved as:", save_path)
   # except Exception as e:
    #    print("Error:", str(e))

#video_url = "https://www.youtube.com/shorts/fmb24baqaBA"  
#save_directory = r"C:\Users\HP\Desktop\yt download"  

#download_video(video_url, save_directory)



import os
from pytube import YouTube

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Downloading... {percentage:.2f}% done")

def download_video(video_url, save_directory):
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
        stream = yt.streams.get_highest_resolution()  
        print("Downloading:", yt.title)
        
        filename = ''.join(c for c in yt.title if c.isalnum() or c in [' ', '.', '_']).rstrip()
        
        save_path = os.path.join(save_directory, filename + ".mp4")
        
        stream.download(output_path=save_directory, filename=filename)
        
        print("Download completed! Saved as:", save_path)
    except Exception as e:
        print("Error:", str(e))

