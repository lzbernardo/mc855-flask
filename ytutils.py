from pytube import YouTube
import sys, os.path

def download(url):
    vid =  YouTube(url).streams.filter(subtype='mp4',res='1080p')
    if(len(vid)):
        vid.first().download('/tmp')
        return 'Success'
    else:
        return 'Fail but ok'
