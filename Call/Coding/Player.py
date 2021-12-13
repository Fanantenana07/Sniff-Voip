
from re import S
from PyQt5 import QtCore, QtGui, QtWidgets
import audioplayer

class Thread_Audio(QtCore.QThread):
    signal = QtCore.pyqtSignal(int)
    def __init__(self,parent=None,file = None):
        self.file = "Audio/"+file
        self.audio = audioplayer.AudioPlayer(self.file)
        super(Thread_Audio,self).__init__(parent)
        self.signal.connect(self.stop)

    def play(self):
        self.audio.play()
        
    
    def pause(self):
        self.audio.pause()
    
    def stop(self,value):
        print(value)
        self.audio.stop()
    
    def resume(self):
        self.audio.resume()
    

        
    def stop(self):
        self.stop_sniffing = True
        
        
    
   