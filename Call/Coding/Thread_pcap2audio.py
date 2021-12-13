import subprocess
from PyQt5 import QtCore
import pyshark
import json

class Thread_Pcap_to_Audio_Class(QtCore.QThread):
    signal = QtCore.pyqtSignal(str,str)
    datebase_signal = QtCore.pyqtSignal(bool)
    def __init__(self,parent = None,file = None,port = None):
        self.port = port
        self.file = file
        super(Thread_Pcap_to_Audio_Class,self).__init__(parent)
        
    def run(self):
        name = self.file.replace(".pcap","")
        raw = open('Raw/'+name+'.raw','wb')
        Capture = pyshark.FileCapture(input_file='./Pcap/'+self.file,decode_as={'udp.port='+self.port:'rtp'})
        payload = []
        sequence = 0
        new_Payload = []
        for Layer in Capture:
            try:
                RTP = Layer['RTP']
                if RTP.payload and RTP.get_field_by_showname("Sequence number").showname_value != sequence:
                    data = {"sequence": sequence ,"payload" : RTP.payload.split(':')}
                    js_data = json.dumps(data)
                    payload.append(js_data)
                    if sequence == 0:
                        first_seq = RTP.get_field_by_showname("Sequence number").showname_value
                        first_payload =  RTP.payload.split(':')
                    sequence = RTP.get_field_by_showname("Sequence number").showname_value  
                    
                else :
                    pass
            except :
                pass
        Capture.close()
        int_first_seq = int(first_seq)+1
        last_seq = int (sequence)
        # new_Payload.append(first_payload)
        find = True
        while int_first_seq != last_seq:
            for item in payload :
                val = json.loads(item)
                if str(val['sequence'])== str(int_first_seq):
                    find = True
                    array_payload = val['payload']
                    break
                else :
                    find = False
                    pass
            if find :
                new_Payload.append(array_payload)
            else :
                new_Payload.append(" ")
            int_first_seq += 1
        for Stream in new_Payload :
            packet = "".join(Stream)
            byteStream = bytearray.fromhex(packet)
            raw.write(byteStream)
        raw.close()
        task = subprocess.Popen('sox --channels 1 --type raw --rate 8000 -S -e u-law Raw/'+name+'.raw Audio/Audio_record_'+name+'.wav',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
        self.signal.emit(str("Audio_record_"+name+".wav"),str(self.file))
    
    def stop (self):
        self.terminate()
    