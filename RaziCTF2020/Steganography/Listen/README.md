## Listen  

### Challenge Description  
Listen carefully, what do you hear? Look closely, what do you see? To Submit the flag, put it in UPPERCASE and in this format RaziCTF{}. like this: RaziCTF{FLAG}  

### Writeup  
In this challenge you are given a mp3 file, named `enc.mp3`.  
Use `Audacity` tool to see signals. When you open this mp3 which audacity, if you choose `Spectrogram` you see image below:  
![Audacity](https://github.com/aahsani/RaziCTFWriteups/raw/master/Steganography/Listen/Screenshot%20from%202020-11-05%2006-24-12.png)

This image is a morse code, and the code is:  
```
- .... .  .-. . .- .-..  ..-. .-.. .- --.  .. ...  ... .---- -- .--. .-.. ...-- -- ----- .-. ... ...--
```

You can use online tools to translate this morse code: 
```
THEREALFLAGISS1MPL3M0RS3
```  
`S1MPL3M0RS3` is your flag.  
