from gtts import gTTS
import pygame
import os

def speak(text):
    print(f"Text to speak: {text}")  # Print the text first
    
    # Make sure the language is set to 'bn' for Bangla
    tts = gTTS(text, lang='bn')
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load and play the audio
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():  # Wait until audio is finished
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

# Test with Bangla text
speak("আপনি কেমন আছেন?")
