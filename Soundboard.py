import audioop
import shlex
import subprocess

class Soundboard:
  # fixed 48000 hz, 2 channels, 2 bytes per frame, signed, little endian

  def __init__(self):
    self.sounds = []

  def load(self, file):
    outrate = 48000
    cmd = "ffmpeg -loglevel quiet -i " + file + " -f s16le -ar {} -ac 2 pipe:1".format(outrate)
    args = shlex.split(cmd)
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    new_sound = {
        'stream': proc.stdout,
        'proc': proc
    }
    self.sounds.append(new_sound)
    print("adding new sound")
    print(self.sounds)

  def nico(self):
    load(self, 'nico.wav')

  def read(self, n):
    buff = bytearray(n)

    if not self.sounds:
      print("no more sounds")
      return bytes(0)

    for sound in self.sounds:
      data = sound['stream'].read(n)
      length = len(data)

      buff[:length] = audioop.add(buff[:length], data, 2)

      if (length < n):
        self.sounds.remove(sound)
        #print("end of sound")

    #print("rb", len(buff), "/", n)
    return bytes(buff)

  def clear(self):
    for sound in self.sounds:
      proc = sound['proc']
      if not proc.poll():
        proc.kill()
      sound['stream'].close()
    self.sounds = []
