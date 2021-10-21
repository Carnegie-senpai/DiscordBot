import os
from typing import Tuple
import youtube_dl
QUEUE_PATH = "./assets/queue"
os.makedirs(QUEUE_PATH,exist_ok=True)

"""
File name format is #_NAME.mp3
"""

def parsedQueue()->Tuple[int,str,str]:
    """Returns a list of tuples representing the queue
    (SONG_NUMBER,SONG_NAME,SONG_PATH)
    """
    parsed= []
    queue = os.listdir(QUEUE_PATH)
    for song in queue:
        split = song.split("_.")
        parsed.append((int(split[0]),split[1],QUEUE_PATH+song))
    parsed.sort(lambda x: x[0])
    return parsed

def queueStatus():
    """Returns a string detailing the current queue status
    """
    queue = parsedQueue()
    returnMessage = "current Queue "+str(len(queue))+"/10:\n"
    for song in queue:
        returnMessage += song[0] + ". " + song[1]+ "\n"
    return returnMessage

def nextUp()-> str:
    """Returns the path to the next up song
    """
    return QUEUE_PATH + sorted(parsedQueue)[0]

def pushQueue(songName: str)-> str: 
    """Returns an empty string on success, else the reason it failed
    """
    queue = parsedQueue()
    if len(queue) >= 10:
        return "Too many songs in the queue"
    
    
