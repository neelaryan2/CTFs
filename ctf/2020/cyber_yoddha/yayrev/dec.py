mod_flag = 'lgUBAJu0n_y3tRaQ-C'

mod_flag = [chr(
	ch.islower() and 
	((ord(ch) - 84) % 26) + 97 or 
	ch.isupper() and 
	((ord(ch) - 52) % 26) + 65 or 
	ord(ch)
	) for ch in mod_flag]

mod_flag = ''.join(mod_flag[5:]) + ''.join(mod_flag[:5])

print(mod_flag)
