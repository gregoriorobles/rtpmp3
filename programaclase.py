import simplertp
import socket
import sys

if __name__== "__main__":
    a = simplertp.RtpHeader()
    a.setHeader(2, 0, 0, 0, 0, 90, 1000)
    b = simplertp.RtpPayloadMp3()
    b.setAudio('archivo.mp3')
    simplertp.SendRtpPacket(2, a, b, '127.0.0.1', 33332, 2)
