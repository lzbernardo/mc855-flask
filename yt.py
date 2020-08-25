from pytube import YouTube
import sys, os.path

dir_path = os.path.dirname(os.path.abspath(__file__)) + '/videos'

vid =  YouTube('http://www.youtube.com/watch?v=HhGKsMzO-sU').streams.filter(subtype='mp4',res='1080p')
if(len(vid)):
    vid.first().download(dir_path)
else:
    print('There is no 1080p version available for this video. Try again with higher quality or after YouTube has finished uploading')
