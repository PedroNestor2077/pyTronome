from time import sleep
import threading
import pygame

class Metronome(threading.Thread):
    running=True
    playing = False
    beats_per_minutes = 100
    frequency = 0
    bar = 4
    upper_on = 1
    current_beat = 1
    volume = 100
    pygame.mixer.init()
    
    click = pygame.mixer.Sound('click.wav')
    upper_click = pygame.mixer.Sound('upper_click.wav')
    
    def run(self,*args,**kwargs):
        while True:
            if self.playing:
                self.process_current_beat()
                self.play()
                sleep(self.frequency)
            if(not self.running):
                break
            
            
    def start_play(self):
        self.frequency = 60/self.beats_per_minutes
        self.playing = True
    
    
    def stop(self):
        self.playing = False
        self.current_beat = 1


    def play(self):
        self.click.set_volume(self.volume)
        self.upper_click.set_volume(self.volume)

        if(self.isUpperBeat()):
            self.upper_click.play()
        else:
            self.click.play()
            
        self.current_beat += 1

    
    def process_current_beat(self):
        if(self.current_beat > self.bar):
            self.current_beat = 1
        
        
    def isUpperBeat(self):
        return self.current_beat == self.upper_on


    def set_bar(self,bar):
        self.bar = bar
        self.current_beat = 1
    
    
    def set_upper_on(self,beat):
        self.upper_on = beat
        self.current_beat = 1
        
        
    def set_volume(self,volume):
        self.volume = volume
        
    def is_playning(self):
        return self.playing
    
    def terminate(self):
        self.running = False
        
    def set_frequency(self,beats_per_minutes):
        self.beats_per_minutes=beats_per_minutes
        self.frequency = 60/beats_per_minutes
        
    