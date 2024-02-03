from blockchain import Blockchain


##################################################
# initialize blockchain
##################################################
sender_mnemonic = "mnemonic"
sender_password = "password"
reciever_mnemonic = "mnemonic1"
reciever_password = "password"

blockchain = Blockchain(name="Phils_blockchain")
print(blockchain)
# <Blockchain 'Phils_blockchain'>
print(vars(blockchain.chain[0]))
# {'index': 0, 'previous_hash': '', 'transactions': [], 'accounts': [], 'timestamp': 1706908397.994127}
##################################################
##################################################


##################################################
# Create user
##################################################
sender = blockchain.add_account(mnemonic=sender_mnemonic, password=sender_password)
print(f"{sender = }\n")
# {'success': 'Account has been created.', 'public_key': '20ed537f407342a57fa9de06f6fbbc194f16fac96977f9da0b4b8490cef35620'}

##################################################
# Get users total coins
##################################################
sender_public_key = sender.get("public_key")
sender_PHC_total = blockchain.get_user_PHC_total(public_key=sender_public_key)
print(f"{sender_PHC_total = }\n")
# 0.0

##################################################
# Try to create an account that have mnemonic and password equal user 1
##################################################
sender_error = blockchain.add_account(
    mnemonic=sender_mnemonic, password=sender_password
)
print(f"{sender_error = }\n")
# {'error': 'Please use another mnemonic or password. You have a hash collision.'}

##################################################
# Create second account
##################################################
reciever = blockchain.add_account(
    mnemonic=reciever_mnemonic, password=reciever_password
)
print(f"{reciever = }\n")
# {'success': 'Account has been created.', 'public_key': '605ead40cc9a6535e68f20990bd6f580f37ba203f9e42c3e3fa0005115f108b9'}

##################################################
# Create our first transaction
##################################################
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


for _ in range(100):
    blockchain.add_transaction(
        sender_mnemonic=sender_mnemonic,
        sender_password=sender_password,
        reciever_public_key=reciever_public_key,
        PHC=0,
    )

print(blockchain.chain)
# [<blockchain.blockchain.Block object at 0x10c6abe80>, <blockchain.blockchain.Block object at 0x10c756500>, ... ]

print(blockchain.chain[2].__dict__)
# {'index': 2, 'previous_hash': 'd359501ff3ec75080580acf37dd6d976fda8c00b85c65b025f9dcee653875962', 'transactions': [<blockchain.blockchain.Transaction object at 0x10cca3490>, ... ], 'accounts': [], 'timestamp': 1706964823.571397}

print(blockchain.is_valid())
# (True, -1)

##################################################
# Lets make changes in the chain
##################################################
error_block = blockchain.chain[-1]
blockchain.chain[3] = error_block

print(blockchain.is_valid())
# (False, 3)
