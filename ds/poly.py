class AudioFile:
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename=filename

class Mp3Format(AudioFile):
    ext='mp3'
    def play(self):
        print("file {} is of type mp3".format(self.filename))

class WavFormat(AudioFile):
    ext='wav'
    def play(self):
        print("file {} is of type wav".format(self.filename))

wav=Mp3Format('testfile.mp3')
wav.play()