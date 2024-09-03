import email
import dkim
import os
import argparse


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def verify_dkim_signature(eml_file):
    with open(eml_file, 'r') as f:
        msg = email.message_from_string(f.read())

    try:
        return dkim.verify(msg.as_bytes())
    except dkim.DKIMException:
        return False


parser = argparse.ArgumentParser(description='Offline DKIM signature checker')
parser.add_argument('-e', metavar='email_file', type=str, required=True, help='email file in .eml format')
parser.add_argument('-k', metavar='dkim_key', type=str, required=True, help='text file containing dkim key')
args = parser.parse_args()
eml_file = args.e
dkim_key = args.k

temp_key_path = open('temp_key', 'w')
temp_key_path.write(dkim_key)
temp_key_path.close()

if verify_dkim_signature(eml_file):
    print(color.GREEN + 'DKIM signature is valid' + color.END)
else:
    print(color.RED + 'DKIM signature is NOT valid' + color.END)
os.remove('temp_key')
