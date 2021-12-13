import pyshark
import os
import datetime
import subprocess

def main():
    raw = open('Raw/file.raw','wb')
    Capture = pyshark.FileCapture('./Pcap/Capture.pcap')
    Payload = []
    for array in Capture:
        try:
            Rtp = array[3]
            if Rtp.payload :
                Payload.append(Rtp.payload.split(':'))
                k = k+1
        except :
            pass

    for Stream in Payload :
        packet = "".join(Stream)
        byteStream = bytearray.fromhex(packet)
        raw.write(byteStream)
    raw.close()
    name = get_date_now()
    sucess = subprocess.Popen('sox --channels 1 --type raw --rate 8000 -S -e u-law Raw/file.raw Audio/'+name+'.wav tempo 2 ',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
    print(str(sucess[1]).replace('b',''))
    os.system('rm Raw/file.raw')
def get_date_now():
    date = datetime.datetime.today().strftime('%y_%m_%d_%Hh_%Mmn_%Ss')
    return date

    

if __name__ == '__main__':
    main()

