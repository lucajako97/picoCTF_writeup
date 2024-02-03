for l in [128, 322, 353, 235, 336, 73, 198, 332, 202, 285, 57, 87, 262, 221, 218, 405, 335, 101, 256, 227, 112, 140]:
    print("picoCTF{"+"abcdefghijklmnopqrstuvwxyz0123456789_"[l%37],end='') if l == 128 else print("}") if l == 140 else print("abcdefghijklmnopqrstuvwxyz0123456789_"[l%37],end='')
