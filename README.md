### About

This script is written for completing Nubela/LandX developer test.
It is a small script to handle ethereum transaction with with the help of web3.
It is written in python and compiled to linux executable with pyinstaller.

### Source Code For Vault Program

Run virtual environment:

source bin/activate

Install dependencies:

pip install -r requirements.txt

To compile executable, head to /src directory,
then run:

pyinstaller vault.py --onefile

The executable should be there in /dist directory
