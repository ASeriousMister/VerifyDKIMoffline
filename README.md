# VerifyDKIMoffline (alpha)
This tool allows to verify DKIM signature of an .eml file providing a DKIM key stored in a .txt file that might not be available on DNS server.

## Disclaimer
This is an alpha version that is intended to be used *only* for educational purposes.

## How to configure the tool
Install dependencies
```
sudo apt install python3-full python3-virtualenv python3-pip git
```
Download the tool
```
git clone https://github.com/ASeriousMister/VerifyDKIMoffline
```
Move your terminal to the tool's folder
```
cd VerifyDKIMoffline
```
Before running it for the first time run the first_run.sh script
```
chmod +x first_run.sh
```
```
./firstrun.sh
```
## How to run the tool
Move to the tool's directory
```
cd VerifyDKIMoffline
```
Enable the virtual environment to use the customized library
```
source dkve/bin/activate
```
### GUI
Run the GUI version of the tool with
```
python3 verifyDKIM_GUI.py
```
and provide the .eml file containing the email to be verified and the .txt file containing the DKIM key to use into the verification progress.
### CLI
Run the command line version specifying the .eml file containing the email to be verified with the `-e` option and the .txt file containing the DKIM key to use into the verification progress with the `-k` option
```
python3 verifyDKIM_CLI.py -e emlfile.eml -k dkimkey.txt
```

