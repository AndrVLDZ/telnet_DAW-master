# pyinstaller -F -i 'C:\Users\vldnd\Desktop\EXE\D.ico' server.py    

import socket
import subprocess
import keyboard
#import pyautogui
import autoit
import time

def print_logo(logo=''):
    LOGO_DAFAULT = """

   /\                 /\\
  / \\'._   (\_/)   _.'/ \\
 /_.''._'--('.')--'_.''._\\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
   `      \(/|\)/        `
           " ` "
     DAW_Start_By_VLDZ 

"""
    if logo != '':
        print(logo)
    else:
        print(LOGO_DAFAULT)

print_logo()
port = int(input('Set the server port: '))
SERVER_ADDR = ('0.0.0.0', port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(SERVER_ADDR)
sock.listen(1)
connections = []
ip = socket.gethostbyname(socket.getfqdn())
print('Host IP: ' + str(ip))

def handle_event_msg(data):
    
    if str(data, "utf-8") == "s\r\n":
        subprocess.Popen(['C:\Program Files\PreSonus\Studio One 4\\Studio One.exe'])
        keyboard.send('space', do_press=True, do_release=True)
        print("\nKeypress event 'Strat/Stop'")
    elif str(data, "utf-8") == "b\r\n":
        subprocess.Popen(['C:\Program Files\PreSonus\Studio One 4\\Studio One.exe'])
        keyboard.send('shift + b')
        print("\nKeypress event 'Goto Previous Мarker'")
    elif str(data, "utf-8") == "n\r\n":
        subprocess.Popen(['C:\Program Files\PreSonus\Studio One 4\\Studio One.exe'])
        keyboard.send('shift + n')
        print("\nKeypress event 'Goto Next Мarker'")


        
    elif str(data, "utf-8") == "c100\r\n":
#        subprocess.Popen(['C:\Games\Cyberpunk 2077\bin\x64\\Cyberpunk2077.exe'])
        print("\nMouse 1000 clicks")
        clickCounter = 0
        while clickCounter < 100:
            clickCounter += 1
            autoit.mouse_down("left")
            time.sleep(0.1)
            autoit.mouse_up("left")
            time.sleep(0.05)

    elif str(data, "utf-8") == "c500\r\n":
#        subprocess.Popen(['C:\Games\Cyberpunk 2077\bin\x64\\Cyberpunk2077.exe'])
        print("\nMouse 1000 clicks")
        clickCounter = 0
        while clickCounter < 500:
            clickCounter += 1
            autoit.mouse_down("left")
            time.sleep(0.1)
            autoit.mouse_up("left")
            time.sleep(0.05)

    elif str(data, "utf-8") == "c1000\r\n":
#        subprocess.Popen(['C:\Games\Cyberpunk 2077\bin\x64\\Cyberpunk2077.exe'])
        print("\nMouse 1000 clicks")
        clickCounter = 0
        while clickCounter < 1000:
            clickCounter += 1
            autoit.mouse_down("left")
            time.sleep(0.1)
            autoit.mouse_up("left")
            time.sleep(0.05)


    elif str(data, "utf-8") == "c5000\r\n":
#        subprocess.Popen(['C:\Games\Cyberpunk 2077\bin\x64\\Cyberpunk2077.exe'])
        print("\nMouse 5000 clicks")
        clickCounter = 0
        while clickCounter < 5000:
            clickCounter += 1
            autoit.mouse_down("left")
            time.sleep(0.1)
            autoit.mouse_up("left")
            time.sleep(0.05)

    elif str(data, "utf-8") == "c10000\r\n":
#        subprocess.Popen(['C:\Games\Cyberpunk 2077\bin\x64\\Cyberpunk2077.exe'])
        print("\nMouse 10000 clicks")
        clickCounter = 0
        while clickCounter < 10000:
            clickCounter += 1
            autoit.mouse_down("left")
            time.sleep(0.1)
            autoit.mouse_up("left")
            time.sleep(0.05)
        
            

    else:
        print("\nJust a msg")
        print(str(data, "utf-8"))


def handler(current_conn: socket.socket, addr):
    global connections
    while True:
        data: bytes = current_conn.recv(1024)
        handle_event_msg(data)
        for c in connections:
            c.send(bytes(str.encode('\n=>> ') + data))
        if not data:
            connections.remove(current_conn)
            current_conn.close()
            break


# Wait for an incoming connection.
while True:
    # new socket representing the connection
    conn: socket.socket
    conn, addr = sock.accept()  # Accept new connection
    handler(conn, addr)
    connections.append(conn)
    print(connections)
    print()
