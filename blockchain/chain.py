import time
import json
import hashlib


def get_current_time() -> float:
    return time.time()


def compute_hash(b: bytes):
    return hashlib.sha256(string=b, usedforsecurity=True).hexdigest()


class Account:
    def __init__(self, mnemonic: str, password: str):
        self.public_key = compute_hash(f"{mnemonic}{password}".encode())


class Transaction:
    """PHC - phils coin"""

    def __init__(
        self,
        index: int,
        previous_hash: str,
        sender: str,
        reciever: str,
        PHC: float,
        sender_PHC_total: float,
        reciever_PHC_total: float,
    ):
        self.index = index
        self.previous_hash = previous_hash
        self.sender = sender
        self.reciever = reciever
        self.PHC = PHC
        self.sender_PHC_total = sender_PHC_total
        self.reciever_PHC_total = reciever_PHC_total
        self.timestamp = get_current_time()

    @property
    def hash(self):
        b: bytes = json.dumps(self.__dict__, sort_keys=True).encode()
        return compute_hash(b)


class Block:
    def __init__(self, index: int, previous_hash: str):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = []
        self.accounts = []
        self.timestamp = get_current_time()

    @property
    def hash(self):
        b: bytes = json.dumps(self.__dict__, sort_keys=True).encode()
        return compute_hash(b)


class Blockchain:
    MAX_TRANSACTIONS_SIZE = 10

    def __init__(self, name: str):
        self.name = name
        self.chain = []
        self._append_block(self._create_initial_block())

    def __str__(self) -> str:
        return f"<Blockchain '{self.name}'>"

    @property
    def current_block(self) -> Block:
        return self.chain[-1]

    @property
    def blocks_count(self):
        return len(self.chain)

    @property
    def last_transaction(self) -> Transaction | None:
        return self.current_block.transactions[-1]

    def _create_initial_block(self):
        return Block(index=0, previous_hash="")

    def _create_block(self):
        return Block(
            index=self.current_block.index + 1,
            previous_hash=self.current_block.hash,
        )

    def _append_block(self, block: Block):
        self.chain.append(block)

    def _append_transaction(self, transaction: Transaction):
        self.current_block.transactions.append(transaction)

    def get_account_by_public_key(self, public_key: str) -> Account | None:
        for block in self.chain:
            for account in block.accounts:
                if public_key == account.public_key:
                    return account
        return

    def login(self, mnemonic: str, password: str) -> dict:
        account = Account(mnemonic=mnemonic, password=password)
        if self.get_account_by_public_key(public_key=account.public_key):
            return {
                "success": "Login.",
                "public_key": account.public_key,
            }
        return {"error": "Please try again."}

    def get_user_PHC_total(self, public_key: str) -> float:
        for block in self.chain[::-1]:
            for transaction in block.transactions[::-1]:
                if transaction.sender == public_key:
                    return transaction.sender_PHC_total
                elif transaction.reciever == public_key:
                    return transaction.reciever_PHC_total
        return 0.0

    def add_account(self, mnemonic: str, password: str) -> dict:
        new_account = Account(mnemonic=mnemonic, password=password)
        if self.get_account_by_public_key(public_key=new_account.public_key):
            return {
                "error": "Please try again or use a new mnemonic. You have a hash collision."
            }
        self.current_block.accounts.append(new_account)
        return {
            "success": "Account has been created.",
            "public_key": new_account.public_key,
        }

    def add_transaction(
        self,
        sender_mnemonic: str,
        sender_password: str,
        reciever_public_key: str,
        PHC: float,
    ):
        sender_public_key = self.login(
            mnemonic=sender_mnemonic, password=sender_password
        ).get("public_key")
        if sender_public_key is None:
            return {"error": "Can not login."}

        reciever = self.get_account_by_public_key(public_key=reciever_public_key)
        if not reciever:
            return {"error": "Can not build transaction."}

        sender_PHC_total = self.get_user_PHC_total(public_key=sender_public_key)
        reciever_PHC_total = self.get_user_PHC_total(public_key=reciever.public_key)

        if sender_PHC_total - PHC < 0:
            return {"error": "You do not have enough PHC."}

        last_transaction = self.last_transaction
        if last_transaction is None:
            index = 0
            hash = ""
        else:
            index = last_transaction.index
            hash = last_transaction.previous_hash

        transaction = Transaction(
            index=index,
            previous_hash=hash,
            sender=sender_public_key,
            reciever=reciever.public_key,
            PHC=PHC,
            sender_PHC_total=sender_PHC_total - PHC,
            reciever_PHC_total=reciever_PHC_total + PHC,
        )
        self._append_transaction(transaction=transaction)
        if len(self.current_block.transactions) >= Blockchain.MAX_TRANSACTIONS_SIZE:
            block = self._create_block()
            self._append_block(block=block)
        return transaction