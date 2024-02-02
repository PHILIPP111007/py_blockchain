from blockchain import Blockchain


sender_mnemonic = "mnemonic"
sender_password = "password"
reciever_mnemonic = "mnemonic1"
reciever_password = "password"

blockchain = Blockchain(name="Phils_blockchain")
print(blockchain)
# <Blockchain 'Phils_blockchain'>
print(vars(blockchain.chain[0]))
# {'index': 0, 'previous_hash': '', 'transactions': [], 'accounts': [], 'timestamp': 1706908397.994127}


sender = blockchain.add_account(mnemonic=sender_mnemonic, password=sender_password)
print(f"{sender = }\n")
# {'success': 'Account has been created.', 'public_key': '20ed537f407342a57fa9de06f6fbbc194f16fac96977f9da0b4b8490cef35620'}

sender_public_key = sender.get("public_key")
sender_PHC_total = blockchain.get_user_PHC_total(public_key=sender_public_key)
print(f"{sender_PHC_total = }\n")
# 0.0

sender_error = blockchain.add_account(
    mnemonic=sender_mnemonic, password=sender_password
)
print(f"{sender_error = }\n")
# {'error': 'Please try again or use a new mnemonic. You have a hash collision.'}

reciever = blockchain.add_account(
    mnemonic=reciever_mnemonic, password=reciever_password
)
print(f"{reciever = }\n")
# {'success': 'Account has been created.', 'public_key': '605ead40cc9a6535e68f20990bd6f580f37ba203f9e42c3e3fa0005115f108b9'}

reciever_public_key = reciever.get("public_key")
transaction = blockchain.add_transaction(
    sender_mnemonic=sender_mnemonic,
    sender_password=sender_password,
    reciever_public_key=reciever_public_key,
    PHC=0,
)
print(f"{transaction.__dict__ = }\n")
# {'index': 0, 'previous_hash': '', 'sender': '20ed537f407342a57fa9de06f6fbbc194f16fac96977f9da0b4b8490cef35620', 'reciever': '605ead40cc9a6535e68f20990bd6f580f37ba203f9e42c3e3fa0005115f108b9', 'PHC': 0.0, 'sender_PHC_total': 0.0, 'reciever_PHC_total': 0.0, 'timestamp': 1706907895.782774}

transaction = blockchain.add_transaction(
    sender_mnemonic=sender_mnemonic,
    sender_password=sender_password,
    reciever_public_key=reciever_public_key,
    PHC=0,
)
print(f"{transaction.__dict__ = }\n")
# {'index': 1, 'previous_hash': '87c2a28e1e031e6b4e1b6bbffa878c63dfca3638c61515ba88ed0361987e30da', 'sender': '20ed537f407342a57fa9de06f6fbbc194f16fac96977f9da0b4b8490cef35620', 'reciever': '605ead40cc9a6535e68f20990bd6f580f37ba203f9e42c3e3fa0005115f108b9', 'PHC': 0.0, 'sender_PHC_total': 0.0, 'reciever_PHC_total': 0.0, 'timestamp': 1706907895.7828639}


print(vars(blockchain.chain[-1]))
# {'index': 0, 'previous_hash': '', 'transactions': [<blockchain.blockchain.Transaction object at 0x10537cbb0>, <blockchain.blockchain.Transaction object at 0x10537cbe0>], 'accounts': [<blockchain.blockchain.Account object at 0x105317d30>, <blockchain.blockchain.Account object at 0x10537fd30>], 'timestamp': 1706907895.782631}
