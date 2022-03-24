#!/usr/bin/env python

from web3 import Web3
import os
from pprint import pprint

import requests

def getenv() -> tuple:
    ''' get environmental variables '''
    priv_key = os.getenv('PRIVATE_KEY')
    passphrase = os.getenv('PASSWORD')
    nodeurl = os.getenv('PARITY_NODE')

    if priv_key is None or passphrase is None or \
        nodeurl is None:
        raise RuntimeError('Please set environmental variables' + \
            'PRIVATE_KEY, PASSWORD, PARITY_NODE.')
    else:
        return priv_key, passphrase, nodeurl

def import_privkey(privatekey: str, password: str, nodeurl: str) -> None:
    ''' importing private key to OpenEthereum '''
    assert privatekey is not None
    assert isinstance(privatekey, str)
    assert password is not None
    assert isinstance(password, str)
    assert nodeurl is not None
    assert isinstance(nodeurl, str)

    ''' establish connection to OpenEthereum node '''
    w3 = Web3(Web3.HTTPProvider(nodeurl))

    ''' confirm connected '''
    connected = w3.isConnected()
    if not connected:
        print('Web3 is not connected. Aborting.')
        return
    else:
        print('Web3 connection to OpenEthereum confirmed.')

    ''' Before importing, print your accounts '''
    print('Pre_existing OpenEthereum Accounts:')
    accounts = w3.eth.accounts
    pprint(accounts)

    ''' import secret key '''

    ''' We are using raw HTTP call because web3.py have not yet impolemented JSON RPC
    API parity_newAccountFromSecret '''
    headers = {
        'Content-Type': 'application/json',
    }

    # private key check if key starts with '0x' prefix
    if not privatekey.startswith('0x'):
        privatekey = '0x' + privatekey

    data = {
        'method': 'parity_newAccountFromSecret',
        'params': [privatekey, password],
        'id': 1,
        'jsonrpc': '2.0'
    }

    response = requests.post(nodeurl, headers=headers, json=data)
    print(response.text)

    ''' After importing, print your accounts '''
    print('OpenEthereum accounts after importing:')
    accounts = w3.eth.accounts
    pprint(accounts)

    return

if __name__ == '__main__':
    try:
        key, phrase, url = getenv()
        import_privkey(key, phrase, url)
        print('Done')
    except:
        import traceback
        traceback.print_exc()
    


    