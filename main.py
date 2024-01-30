# from blockchain.block import Block
# b = Block(previous_block="12039jegrig", index=1)
# print(b)
# print(vars(b))


from blockchain import Blockchain, Account


chain = Blockchain(name="Phils_blockchain")
print(chain)


for i in range(20):
    chain.add_transaction(i)


# -------------

print(vars(chain.chain[0]))
print()

print(vars(chain.chain[1]))
print()

print(vars(chain.chain[-1]))
print()

mnemonic = "Привет как дела"
password = "password"
account = Account(mnemonic=mnemonic, password=password)

print(account)
print(vars(account))
