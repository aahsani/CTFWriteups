## Oracle of Blair

### Challenge Description

...  

### Writeup

We are given a server and its code which wants input from user. Every `{}` in the input will be replaced with  flag. After performing a padding on it, the result will be decryted using AES.  
First we tested it on server. If you insert `7b7d` (which is {}) it will use flag as decryption input. We inserted `7b7d`. The result is something 32 bytes long. we tested some additional bytes to see when it expands to 64 bytes. If you insert 'A'*14 + '7b7d' as input (we added 7 additional bytes) it is still 32 bytes long. Adding one another bytes will expand result to 64 bytes. So we understand that the flag is 25 bytes long.  
In AES-CBC mode decryption, we have 16 byte blocks that each of them is an input for decryption. Then the `xor` openration with input of previos block  will be applied on it. So without any need for having key, we can compare equality of 2 blocks (except first block wich uses an iv and it is random!). The 'iv' has just effect on first block. So we fill the first 16 bytes of input with `0`s.  
The second and third block will be our test blocks. At each iteration we bruteforce all 256 bytes in a specific index. Once the block is equal with the corresponding byte in flag, we add it to result list and proceed to check next index. 
But where is the flag? we store flag in fourth and fifth blocks in a way that first character of flag in these two blocks be in the same index with first charachter that we tested.  
Here we know that the first part of flag is `actf{`. So we know the first 5 bytes and we have to predict 6th byte in first step. 
In each step we generate input using function bellow. The `byte` variable is the current byte that is going to be tested and the `counter` variable is holding index value.  
```python
def generate_input(counter, byte):
    res = "0" * 32
    res += "0" * (32 - counter) * 2
    for i in resultList:
        res += hex(i)[2:]
    if (len(hex(byte)) == 3): res += "0"
    res += hex(byte)[2:]
    res += "0" * (32 - counter) * 2
    res += "7b7d"
    return res
```
We get the result and check if the inserted byte satisties the condition or not using function bellow:  
```python
def process_result(res, a1, a3, byte):
    blocksLen = int(int(len(res) / 2) / 16)
    blocks = []
    start = 0
    end = 32
    for i in range(0, blocksLen):
        blocks.append(res[start:end])
        start = start + 32
        end = end + 32
    r1 = int(blocks[2], 16) ^ int(a1, 16)
    r2 = int(blocks[4], 16) ^ int(a3, 16)
    if (r1 == r2):
        resultList.append(byte)
        print(printFlag())
        return True
    return False
```
Finally after `counter = 25` we have the flag:  
```
actf{cbc_more_like_ecb_c}
```