import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nLungo tak anti-anti kapan nggonmu bali", 0.16),
        ("Mecak ing endahing wengi kutooo Nganjuk ikiiii......", 0.15),
        ("Sumilir angin aatis gugah kangene ati", 0.17),
        ("Opo kang mas ora ngerteni?", 0.15),
        ("Koe mas tak kangeni", 0.19),
       
    ]
    
    delays = [0.3, 4.3, 7.9, 11.6, 16.0, 19.3, 23.3, 27.0, 30.5, 34.0]

    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()