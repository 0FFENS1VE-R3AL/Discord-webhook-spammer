# ---------- Webhook spammer for Discord ----------
#
# ----------------------- IMPORTANT -----------------------
# ---------- This programm is only for eduction! ----------
# ---------- Im not responsible for any damage! ----------
# ---------------------------------------------------------

# ---------- Import of all important modules for the project ----------

from dhooks import Webhook
import colorama
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
colorama.init(autoreset=True)

# ---------- Title of the project // Bar to beautify the UI ----------

print(f"""{Fore.BLUE}░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗  ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░  ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
{Fore.GREEN}
▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼
""")

# ---------- Input command so that you can enter the webhook URL // coloured ----------

print(Fore.GREEN + "Enter webhook URL: ", end='')
Webhook1 = input()

# ---------- Spacers for a better overview ----------

print(" ")

# ---------- Redefining the variable ----------

hook = Webhook(Webhook1)

# ---------- Input command so that you can enter the message you want to spam // coloured ----------

print(Fore.GREEN + "Enter spam message: ", end='')
MessageToSpam = input()

# ---------- Note that spamming has now started ----------

print(f"""
{Fore.GREEN}Start spamming...
""")

# ---------- Note that to stop spamming you need to close the window // Bar to beautify the UI ----------

print(f"""{Fore.GREEN}Close window to stop spamming! 

{Fore.GREEN}▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼
""")

# ---------- Loop so that the spam message is sent as often as possible in a row ----------

while True:
    hook.send(f"{MessageToSpam}")







