
local_c = 0;
buf1 = [0xb4,0x7f,0xb8,0x8,0x6f,0x4b,0x86,0x20,0xa0,0xda,0x1b,0x83,0x4e,0x98,0x62,0x39,0x61,0x37,0xc4,0xe2,0x89,0x91,0x1d,0xac,0x75,0x38,0xb3,0xe0,0xb7,0xd8,0x30,0x9a,0xe8,0x39,0xcb,0x59,0xf2]
buf2 = [0xde,0x1c,0xcc,0x6e,0x14,0x27,0xb6,0x10,0xcb,0xef,0x44,0xb2,0x27,0xd3,0x51,0x66,0x14,0x68,0xa2,0xd2,0xdc,0xff,0x79,0xf3,0x18,0xb,0xec,0xd0,0x86,0xe0,0x51,0xaa,0xd1,0x5d,0xfd,0x24,0xf8]
res = []
while (local_c < 0x25) :
  t = buf1[local_c] ^ buf2[local_c];
  res.append(chr(t))
  local_c = local_c + 1;

#write(5,buf1,0x25);
print("".join(res))

# jctf{l00k5_1iK3_u_f0Und_m3_018a09d6}