alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_"
message = [128, 322, 353, 235, 336, 73, 198, 332, 202, 285, 57, 87, 262, 221, 218, 405, 335, 101, 256, 227, 112, 140]
decrypted_message = b""

for l in message:
	decrypted_message += bytes(alphabet[l % len(alphabet)], 'utf-8')

print("picoCTF{" + decrypted_message.decode('utf-8') + "}")
