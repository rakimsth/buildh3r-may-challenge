from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams,
    PayParams, 
)

algorand = AlgorandClient.default_local_net()
dispenser = algorand.account.dispenser()
print("Dispenser: ",dispenser.address)
creator = algorand.account.random()
print("Creator: ",creator.address)

algorand.send.payment(
 PayParams(
    sender=dispenser.address,
    receiver=creator.address,
    amount=1_000_000,
 )
)
# print("Creator Information: ",algorand.account.get_information(creator.address))

sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total=50,
        asset_name="BUILDH3R",
        unit_name="HER",
    )
)

asset_id = sent_txn['confirmation']['asset-index']
print("Asset ID: ", asset_id)

#Receiver A
receiver_acct = algorand.account.random()
print("Receiver A Acc: ",receiver_acct.address)
#Fund the receiver account
algorand.send.payment(
 PayParams(
    sender=dispenser.address,
    receiver=receiver_acct.address,
    amount=1_000_000,
 )
)
#Opt in to select the asset to prevent Spam
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=receiver_acct.address,
        asset_id=asset_id,
    )
)
#Transfer the asset
asset_transfer = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=receiver_acct.address,
        asset_id=asset_id,
        amount=10
    )
)
print("Receiver A Information: ",algorand.account.get_information(receiver_acct.address))

#Receiver B
receiver_acct_b = algorand.account.random()
print("Receiver B Acc: ",receiver_acct_b.address)
#Fund the receiver account
algorand.send.payment(
 PayParams(
    sender=dispenser.address,
    receiver=receiver_acct_b.address,
    amount=1_000_000,
 )
)
#Opt in to select the asset to prevent Spam
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=receiver_acct_b.address,
        asset_id=asset_id,
    )
)
#Transfer the asset
asset_transfer_b = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=receiver_acct_b.address,
        asset_id=asset_id,
        amount=15,
    )
)
print("Receiver B Information: ",algorand.account.get_information(receiver_acct_b.address))

#Receiver C
receiver_acct_c = algorand.account.random()
print("Receiver C Acc: ",receiver_acct_c.address)
#Fund the receiver account
algorand.send.payment(
 PayParams(
    sender=dispenser.address,
    receiver=receiver_acct_c.address,
    amount=1_000_000
 )
)
#Opt in to select the asset to prevent Spam
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=receiver_acct_c.address,
        asset_id=asset_id,
    )
)
#Transfer the asset
asset_transfer_c = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=receiver_acct_c.address,
        asset_id=asset_id,
        amount=15,
       last_valid_round=1000
    )
)
print("Receiver C Information: ",algorand.account.get_information(receiver_acct_c.address))
