## data-backup

### Challenge Description  

The backup of our data was somehow corrupted. Recover the data and be rewarded with a flag.  

### Writeup
We are given `data-backup` file. first 4 byte of this file is `jctf`. So the magic number is edited. If we perform binwalk on the file, we see there is some files inside it. So we guess it may be a zip file. We put `50 4B 03 04` instead of `4A 43 54 46` in order to make it a zip file. Now we can extract the content. Flag is stored in ``flag.pdf`.  