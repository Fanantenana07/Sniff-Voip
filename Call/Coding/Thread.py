
from PyQt5 import QtCore
import pyshark

class Thread_Sniffing_Class(QtCore.QThread):
    signal = QtCore.pyqtSignal(object,str)
    end = QtCore.pyqtSignal(bool)
    def __init__(self,parent=None,interface = None ,name = None):
        self.stop_sniffing = False
        self.interface = interface
        self.name = name
        super(Thread_Sniffing_Class,self).__init__(parent)

    def run(self):
        self.file = "Pcap/"+self.name+".pcap"
        self.capture = pyshark.LiveCapture(interface=self.interface,output_file=self.file)
        try :
            for packet in self.capture.sniff_continuously():
                    if not self.stop_sniffing :
                        self.signal.emit(packet,self.name+".pcap")
                    else :
                        self.capture.close()
                        
        except pyshark.capture.capture.TSharkCrashException:
            self.capture.close_async()
            self.capture._cleanup_subprocess()
            self.capture.close()
            return 

    def stop(self):
        self.stop_sniffing = True
        
        
    
   