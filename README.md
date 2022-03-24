# importSecretKeyToOpenEthereum
web3.py script to import secret key to creating OpenEthereum node account

---

importing your secret key and create an account on OpneEthereum Node

このスクリプトを使うことでMetamaskなど他アカウントで作成したイーサリアムアカウントの秘密鍵をOpenEthereumノードにインポートしてOpenEthereum上のアカウントを作成できます。

---

## Prerequisites

* Python 3.x
* pip or pipenv, poetry, or other package management tool to install packages in requirements.txt
* Your own OpenEthereum node

---

## Usage

1. clone this repository to your local directory
```sh
$ git clone https://github.com/cclefjp/importSecretKeyToOpenEthereum.git
```
2. move to project directory
```sh
$ cd importSecretKeyToOpenEthereum
```
3. install required package

If using pip:
```sh
$ pip -r requirements.txt
```

If using pipenv:
```sh
$ pipenv --python 3.x # specify you like
$ pipenv install -r requirements.txt
$ pipenv shell # dive into virutal environment
```

4. set your private key to environmental variable
```sh
$ export PRIVATE_KEY="your_private_key_to_import"
```

5. set your new passphrase to environmental variable
```sh
$ export PASSWORD="set_your_new_password"
```

6. set your node URL to environmental viriable
```sh
$ export PARITY_NODE="https://your_node:8545"
```

7. run the script
```sh
$ python ./import_secret_key.py
```
