from pytube import YouTube
import sys, os.path

dir_path = os.path.dirname(os.path.abspath(__file__)) + '/videos'

def download(url):
    vid =  YouTube(url).streams.filter(subtype='mp4',res='1080p')
    if(len(vid)):
        vid.first().download(dir_path)
        return 'Success'
    else:
        return 'Fail but ok'
