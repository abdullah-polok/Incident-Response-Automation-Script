# listner for test purposes only
import socket

s = socket.socket()
s.bind(("0.0.0.0", 4444))
s.listen(1)

print("Listening on port 4444...")
while True:
    conn, addr = s.accept()
    print("Connected:", addr)
