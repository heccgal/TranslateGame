init python:
    class SoundManager():
        def __init__(self):
            pass
        
        def __new__(self):
            self.music_channels = ["music", "music2", "music3"]
            self.sound_channels = ["sound", "sound2", "sound3"]
            self.channels = ["music", "music2", "music3", "sound", "sound2", "sound3"]
            pass
        
        @classmethod
        def play_sound(self, name = "", fade = 0.7, loop = True, multi = False):
            if name == "":
                renpy.music.stop("sound", fadeout = fade)
                renpy.music.stop("sound2", fadeout = fade)
                renpy.music.stop("sound3", fadeout = fade)
            elif renpy.sound.get_playing("sound") == name or renpy.sound.get_playing("sound2") == name or renpy.sound.get_playing("sound3") == name:
                return True
            elif not renpy.music.is_playing("sound") and renpy.sound.get_playing("sound") != name:
                if multi == False:
                    renpy.music.stop("sound2", fadeout = fade)
                    renpy.music.stop("sound3", fadeout = fade)
                renpy.music.play(name, "sound", loop = loop, fadein = fade)
            elif not renpy.music.is_playing("sound2") and renpy.sound.get_playing("sound2") != name:
                if multi == False:
                    renpy.music.stop("sound", fadeout = fade)
                    renpy.music.stop("sound3", fadeout = fade)
                renpy.music.play(name, "sound2", loop = loop, fadein = fade)
            elif not renpy.music.is_playing("sound3") and renpy.sound.get_playing("sound3") != name:
                if multi == False:
                    renpy.music.stop("sound", fadeout = fade)
                    renpy.music.stop("sound2", fadeout = fade)
                renpy.music.play(name, "sound3", loop = loop, fadein = fade)
        
        @classmethod
        def play_music(self, name = "", fade = 0.7, loop = True, multi = False):
            if name == "":
                renpy.music.stop("music", fadeout = fade)
                renpy.music.stop("music2", fadeout = fade)
                renpy.music.stop("music3", fadeout = fade)
            elif renpy.music.get_playing("music") == name or renpy.music.get_playing("music2") == name or renpy.music.get_playing("music3") == name:
                return True
            elif not renpy.music.is_playing("music") and renpy.music.get_playing("music") != name:
                if multi == False:
                    renpy.music.stop("music2", fadeout = fade)
                    renpy.music.stop("music3", fadeout = fade)
                renpy.music.play(name, "music", loop = loop, fadein = fade)
            elif not renpy.music.is_playing("music2") and renpy.music.get_playing("music2") != name:
                if multi == False:
                    renpy.music.stop("music", fadeout = fade)
                    renpy.music.stop("music3", fadeout = fade)
                renpy.music.play(name, "music2", loop = loop, fadein = fade)
            elif not renpy.music.is_playing("music3") and renpy.music.get_playing("music3") != name:
                if multi == False:
                    renpy.music.stop("music", fadeout = fade)
                    renpy.music.stop("music2", fadeout = fade)
                renpy.music.play(name, "music3", loop = loop, fadein = fade)
        
        @classmethod
        def is_playing(self, sound):
            return sound in [renpy.music.get_playing(s) for s in self.channels]
        
        @classmethod
        def door_sfx(self, locked=False):
            if locked:
                return "audio/sfx_door1_lock{}.ogg".format(random.randint(1,2))
            else:
                return "audio/sfx_door1_{}.ogg".format(random.randint(1,2))


    def playSound(name = "", fade = 0.7, loop = True, multi = False):
        if name == "":
            renpy.music.stop("sound", fadeout = fade)
            renpy.music.stop("sound2", fadeout = fade)
            renpy.music.stop("sound3", fadeout = fade)
        elif renpy.sound.get_playing("sound") == name or renpy.sound.get_playing("sound2") == name or renpy.sound.get_playing("sound3") == name:
            return True
        elif not renpy.music.is_playing("sound") and renpy.sound.get_playing("sound") != name:
            if multi == False:
                renpy.music.stop("sound2", fadeout = fade)
                renpy.music.stop("sound3", fadeout = fade)
            renpy.music.play(name, "sound", loop = loop, fadein = fade)
        elif not renpy.music.is_playing("sound2") and renpy.sound.get_playing("sound2") != name:
            if multi == False:
                renpy.music.stop("sound", fadeout = fade)
                renpy.music.stop("sound3", fadeout = fade)
            renpy.music.play(name, "sound2", loop = loop, fadein = fade)
        elif not renpy.music.is_playing("sound3") and renpy.sound.get_playing("sound3") != name:
            if multi == False:
                renpy.music.stop("sound", fadeout = fade)
                renpy.music.stop("sound2", fadeout = fade)
            renpy.music.play(name, "sound3", loop = loop, fadein = fade)

    def getPlayingSound(name):
        if renpy.sound.get_playing("sound") == name or renpy.sound.get_playing("sound2") == name or renpy.sound.get_playing("sound3") == name:
            return False
        return True

    def playMusic(name = "", fade = 0.7, loop = True, multi = False):
        if name == "":
            renpy.music.stop("music", fadeout = fade)
            renpy.music.stop("music2", fadeout = fade)
            renpy.music.stop("music3", fadeout = fade)
        elif renpy.music.get_playing("music") == name or renpy.music.get_playing("music2") == name or renpy.music.get_playing("music3") == name:
            return True
        elif not renpy.music.is_playing("music") and renpy.music.get_playing("music") != name:
            if multi == False:
                renpy.music.stop("music2", fadeout = fade)
                renpy.music.stop("music3", fadeout = fade)
            renpy.music.play(name, "music", loop = loop, fadein = fade)
        elif not renpy.music.is_playing("music2") and renpy.music.get_playing("music2") != name:
            if multi == False:
                renpy.music.stop("music", fadeout = fade)
                renpy.music.stop("music3", fadeout = fade)
            renpy.music.play(name, "music2", loop = loop, fadein = fade)
        elif not renpy.music.is_playing("music3") and renpy.music.get_playing("music3") != name:
            if multi == False:
                renpy.music.stop("music", fadeout = fade)
                renpy.music.stop("music2", fadeout = fade)
            renpy.music.play(name, "music3", loop = loop, fadein = fade)

    def getPlayingMusic(name):
        if renpy.music.get_playing("music") == name or renpy.music.get_playing("music2") == name or renpy.music.get_playing("music3") == name:
            return False
        return True

    def sfxDoor(locked = False):
        if not locked:
            tmp = randomizer("audio/sfx_door1_{}.ogg", 1, 2)
        else:
            tmp = randomizer("audio/sfx_door1_lock{}.ogg", 1, 2)
        return tmp
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
