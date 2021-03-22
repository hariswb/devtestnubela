## About

This script is written for completing Nubela/LandX developer test.
It is a small script to handle ethereum transaction with with the help of web3.
It is written in python and compiled to linux executable with pyinstaller.

## Private Key

Store the private key of from_address in .env variable

## How to use

Run this in the executable directory:

```

./vault /path/to/socket/socket_python.s
```

Head over the socket directory and:

```

nc -U socket_python.s
```

## Request Example

Make sure that from and to address are checksummed. If not, check here https://ethsum.netlify.app/

```
{"id": "1","type": "sign_transfer","from_address": "0x00000000000000000000000000000","to_address": "0x000000000000000000000000000000","amount": "10000000"}
```

## Check The Result

At the terminal where you are running ./vault program, you will get response with field {id, tx}. Pass the hexbyte text to https://ropsten.etherscan.io/pushTx to see transaction details.
