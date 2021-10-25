## USB Exfiltration  

### Challenge Description

Someone stole data from our servers and you need to figure out exactly what they took or you're fired! We know they zipped the files then transferred them via USB somehow so here's a capture of the USB traffic. You should be able to recover the files from that, right?  

### Writeup
We are given a `pcapng` file which is a capture of the USB traffic. If you look at the packets, you will see that there are some consistently large packets starting from the 415th one. This packet's data starts with `PK`. So we guess that this can be transferred data of a zip file. So we have to collect these data, until the 497th packet and save them as a zip file.  
We can use Wireshark directly and copy the data section of the packets and store them in a file. To do this, select the data section, right-click on it, and copy it as a hex stream. Open an empty file in `010 Editor` and use `Ctrl + Shift + V` to paste them. Copy each packet's data and paste it into the file. The result is a zip file that can be extracted. There are 2 files. `meme.png` and `flag.b64`. Decode the content of `flag.b64` and you get the flag.   
You can also use a script and extract data sections:  
```python
import pyshark
import binascii
import zipfile
import io

cap = pyshark.FileCapture("exfiltration.pcapng", display_filter="usb.data_len > 200")
file = ""
for packet in cap:
    file += packet.data.usb_capdata.raw_value
cap.close()
file = binascii.unhexlify(file)
f = open("output.zip", "wb")
f.write(file)
```