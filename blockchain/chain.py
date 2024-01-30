import time
import json
import hashlib


def compute_hash(b: bytes):
    return hashlib.sha256(string=b, usedforsecurity=True).hexdigest()


class Account:
    def __init__(self, mnemonic: str, password: str):
        self.mnemonic_hash = compute_hash(mnemonic.encode())
        self.password_hash = compute_hash(password.encode())
        self.coins = 100


class Transaction:
    """PHC - phils coin"""

    def __init__(self, sender: Account, reciever: Account, PHC: int):
        self.sender = sender
        self.reciever = reciever
        self.PHC = PHC


class Block:
    def __init__(self, index: int, previous_hash: str):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = []
        self.accounts = []
        self.timestamp = time.time()

    @property
    def hash(self):
        b: bytes = json.dumps(self.__dict__, sort_keys=True).encode()
        return compute_hash(b)


class Blockchain:
    def __init__(self, name: str):
        self.name = name
        self.MAX_TRANSACTIONS_SIZE = 10
        self.chain = []
        self._append_block(self._create_initial_block())

    def __str__(self) -> str:
        return f"<Blockchain '{self.name}'>"

    def _append_block(self, block: Block):
        self.chain.append(block)

    def _create_initial_block(self):
        return Block(index=0, previous_hash="")

    def _create_block(self):
        block = Block(
            index=self.current_block.index + 1,
            previous_hash=self.current_block.hash,
        )

        self._append_block(block)

    @property
    def current_block(self) -> Block:
        return self.chain[-1]

    @property
    def blocks_count(self):
        return len(self.chain)

    def add_transaction(self, transaction):
        self.current_block.transactions.append(transaction)
        if len(self.current_block.transactions) >= self.MAX_TRANSACTIONS_SIZE:
            self._create_block()

    def get_account():
        ...

    def add_account(self, mnemonic: str, password: str):
        self.current_block.accounts.append()
