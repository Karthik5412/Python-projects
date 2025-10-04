import datetime as dt
import pygame 
import time
import keyboard as key

def alaram(set_time):
    print(f'"Alaram set for {set_time}"')
    pygame.mixer.init()
    sound = 'D:/python_programs/Python-projects/alaram clock/sound.mp3'
    is_running = True
    main_time = dt.datetime.strptime(set_time,'%H:%M:%S').time()

    while is_running:
        current = dt.datetime.now().strftime('%H:%M:%S')

        print(current)
        time.sleep(1)

        if current == main_time.strftime('%H:%M:%S'):
            print('Wake up')
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
                
                
                if key.is_pressed('enter'):
                    pygame.mixer.music.stop()
                    is_running = False
                    print('Have a nice day')
                elif key.is_pressed('space'):
                    pygame.mixer.music.pause() 
                    main_time = dt.datetime.now() + dt.timedelta(seconds=10)
                    print()
                    print(f'I will remaind you at {main_time.strftime('%H:%M:%S')}')
                    print()
                    time.sleep(5)
                    break
                    
    

def main():
    set_time = input('Enter alaram time in this format (HH:MM:SS):')
    alaram(set_time)

if __name__ == "__main__":
    main()



