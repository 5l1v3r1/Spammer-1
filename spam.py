import requests, random, json, os, easygui, ctypes, time, discord
from colorama import init, Fore
init(convert=True)

clear = lambda : os.system("cls")

class Client:
    def __init__(self, file):
        super().__init__()
        self.file = None

    def RandomColor(self): 
        randcolor = random.randint(0x000000, 0xFFFFFF)
        return randcolor
    
    def spam(self, message: str, channelID: str, tts: bool, tokens: str, amount: int, delay: int):

        jsonData = {
            "content": " ",
            "tts": tts,
            "embed": {
                    'title': message
                }
    
        }
        
        headers = {
            "Content-Type": "application/json",
            "Content-Length": str(len(message)),
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
        }
        with requests.Session() as session:

                for _i in range(amount):
                    
                    token = random.choice(tokens);

                    session.put(f"https://discordapp.com/api/v6/users/@me/connections/skype/{random.randint(1, 10)}", json={ "name": 'icewallowcum,"visibility": 1, "verified": True },headers={"Authorization": token})

                    headers["authorization"] = token

                    jsonData["embed"]["color"] = self.RandomColor()

                    time.sleep(delay)

                    req = session.post(f"https://discordapp.com/api/v6/channels/{channelID}/messages", json=jsonData, headers=headers)

                    _data = req.json()

                    if _data["id"]:
                        print(f"[{Fore.BLUE}!!{Fore.RESET}] Sent the message.")


        self.start()

    def join(self, code: str, tokens: str):

        headers = {
            "Content-Type": 'application/json',
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
        }

        with requests.Session() as session:

            for token in tokens:

                headers["authorization"] = token

                req = session.post(f"https://discordapp.com/api/v6/invites/{code}", headers=headers)

                _data = req.json()
        
                if _data["guild"]:
                    print(f"[{Fore.BLUE}!!{Fore.RESET}] Joined the {_data['guild']['name']} server.")


            self.start()

    def start(self):
        if self.file == None:
            clear()
            print(f"[{Fore.BLUE}>{Fore.RESET}] Tokens File Selection {Fore.RESET}")
            time.sleep(1)
            file = easygui.fileopenbox()
            self.file = file

        clear()

        with open(self.file) as file:
            tokens = file.read().split("\n")

            print(f"{Fore.BLUE}[{Fore.RESET}0{Fore.BLUE}] Return to menu {Fore.RESET}")
            print(f"{Fore.BLUE}[{Fore.RESET}1{Fore.BLUE}] Join Server {Fore.RESET}")
            print(f"{Fore.BLUE}[{Fore.RESET}2{Fore.BLUE}] Spam channel {Fore.RESET}")
            print(f"{Fore.BLUE}[{Fore.RESET}3{Fore.BLUE}] Exit Application {Fore.RESET}")

            option = int(input("> "))

            if option not in [0,1,2,3]:
                print(f"[{Fore.RED}Invalid Option{Fore.RESET}]")
                time.sleep(1)
                self.start()

            if option == 0:
                clear()
                self.start()
                return

            if option == 1:
                clear()

                print(f"[{Fore.BLUE}>{Fore.RESET}] Server Invite {Fore.RESET}")
                code = str(input("> "))

                if "https://discord.gg/" in code:
                    code = code.split("https://discord.gg/")[1]
                else:
                    code = code 
                
                self.join(code, tokens)

            if option == 2:
                clear()

                print(f"[{Fore.BLUE}>{Fore.RESET}] Channel Id {Fore.RESET}")
                channelID = str(input("> "))
                print(f"[{Fore.BLUE}>{Fore.RESET}] Message Content {Fore.RESET}")
                message = str(input("> "))
                print(f"[{Fore.BLUE}>{Fore.RESET}] Amount of messages to send {Fore.RESET}")
                amount = int(input(" "))
                print(f"[{Fore.BLUE}>{Fore.RESET}] Delay (1,2,3)[seconds] {Fore.RESET}")
                delay = int(input(" "))


                self.spam(message, channelID, False, tokens, amount, delay)

            if option == 3:
                clear()
                exit()
            

if __name__ == "__main__":
    Client(None).start()
