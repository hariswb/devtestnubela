## Source Code For Vault Program

Run virtual environment:

source bin/activate

Install dependencies:

pip install -r requirements.txt

To compile executable, head to /src directory,
then run:

pyinstaller vault.py --onefile

The executable should be there in /dist directory
