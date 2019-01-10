import pdb

class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        pdb.set_trace()
        print("playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print("playing {} as wav".format(self.filename))

class OggFile(AudioFile):
    ext = "ogg"
    def play(self):
        print("playing {} as ogg".format(self.filename))

#ogg = OggFile("myfile.ogg")
#ogg.play()

#print(ogg.__dict__)

#nada = OggFile("nada")

#soymptres = MP3File("myfile.mp3")
#soymptres.play()

class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Excpetion ("Invalid file format")
        self.filename = filename

    def play(self):
        print("playing {} as flac.".format(self.filename))

oso = FlacFile("oso.flac")
oso.play()