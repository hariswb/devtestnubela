from pathlib import Path
import os.path
import os
import time
import socket
import ast
import sys
import json
from web3 import Web3, HTTPProvider

from dotenv import load_dotenv
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
private_key = os.getenv("PRIVATE_KEY")


path = sys.argv[1]


def get_signed_transaction(request):
    project_id = "3134bd59fcfb4e919c3ee5ad94a5fc60"
    provider = "https://ropsten.infura.io/v3/"+project_id

    w3 = Web3(HTTPProvider(provider))

    acct = w3.eth.account.privateKeyToAccount(private_key)

    amount = int(request['amount'])
    fee = int(0.1 * amount)
    amount_sent = amount - fee
    nonce = w3.eth.get_transaction_count(acct.address)
    transaction = {
        'to': request["to_address"],
        'value': amount,
        'gas': fee,
        'gasPrice': w3.toWei('21', 'gwei'),
        'nonce': nonce,
        'chainId': 3,
    }

    signed = acct.sign_transaction(transaction)
    result = {"id": request["id"], "tx": signed.rawTransaction}

    return result


def linuxsocket(path):
    if os.path.exists(path):
        os.remove(path)

    print("Waiting for socket connection")

    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    with server as server:
        server.bind(path)
        server.listen()

        conn, addr = server.accept()
        with conn:
            print("Establish connection!")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
                data = data.strip().decode('utf8')
                request = ast.literal_eval(data)

                result = get_signed_transaction(request)

                print(result)


linuxsocket(path)
