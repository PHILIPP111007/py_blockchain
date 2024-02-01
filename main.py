# from blockchain.block import Block
# b = Block(previous_block="12039jegrig", index=1)
# print(b)
# print(vars(b))


from blockchain import Blockchain


blockchain = Blockchain(name="Phils_blockchain")
print(blockchain)


sender_mnemonic = "mnemonic"
sender_password = "password"
sender = blockchain.add_account(mnemonic=sender_mnemonic, password=sender_password)
print(f"{sender = }")

sender_public_key = sender.get("public_key")
sender_PHC_total = blockchain.get_user_PHC_total(public_key=sender_public_key)
print(f"{sender_PHC_total = }")

sender_error = blockchain.add_account(
    mnemonic=sender_mnemonic, password=sender_password
)
print(f"{sender_error = }")


reciever_mnemonic = "mnemonic1"
reciever_password = "password"
reciever = blockchain.add_account(
    mnemonic=reciever_mnemonic, password=reciever_password
)
print(f"{reciever = }")

reciever_public_key = reciever.get("public_key")
transaction = blockchain.add_transaction(
    sender_mnemonic=sender_mnemonic,
    sender_password=sender_password,
    reciever_public_key=reciever_public_key,
    PHC=1,
)
print(f"{transaction = }")


print(vars(blockchain.chain[-1]))
