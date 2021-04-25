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
