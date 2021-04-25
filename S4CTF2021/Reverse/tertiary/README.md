## tertiary

### Challenge Description

The tertiary period began with the demise of the non-avian dinosaurs!  

### Writeup

We are given an elf file. Decomiple it and rewrite the code and run it. It will give you the flag:  
```python
local_28 = ["Y_rssr_3_UOSTr3e50_s_lsR_c_0cf", "0}3om7tRy__4F3r__oeY_e_a4U{foe", "ua__4!heog_C{vsis04}{7gb_p}_F3"]

local_88 = [0]*200

local_c = 0
while local_c < 0x1e:
	local_10 = 0
	while local_10 < 3:
		uVar2 = local_28[local_10][local_c]
		local_88[local_10 + local_c * 3] = local_28[local_10][local_c]
		local_10 = local_10 + 1
	local_c = local_c + 1
print("".join(local_88[:90]))
print(uVar2)

```
The result of this code is:  
```
Y0u_}ar3_so_sm4r7!_th3Re_yoU_gO__S4CTF{r3v3rse_i5_s0o0_e4sY}__{le7s_gRab_4_cUp_{}0f_coFfe3
```
And the flag is:  
```
S4CTF{r3v3rse_i5_s0o0_e4sY}
```