from brownie import KongLongCoin, network, config
from scripts.utils import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy():
    account = get_account()

    coin = KongLongCoin.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {coin.address}")
    return coin


def mint(amount):
    account = get_account()
    coin = KongLongCoin[-1]

    coin.mint(account, amount, {"from": account})

    total_supply = coin.totalSupply({"from": account})
    print(f"mint successfully, total supply: {total_supply}")


def airdrop(receiver, amount):
    account = get_account()
    coin = KongLongCoin[-1]

    coin.transfer(receiver, amount, {"from": account})
    receiver_balance = coin.balanceOf(receiver, {"from": account})

    print(f"account {receiver} has {receiver_balance} token")


def balance_of(target_acc):
    account = get_account()
    coin = KongLongCoin[-1]

    balance = coin.balanceOf(target_acc, {"from": account})
    print(f"account {target_acc} has {balance} token")


def burn(amount):
    account = get_account()
    coin = KongLongCoin[-1]

    coin.burn(amount, {"from": account})

    total_supply = coin.totalSupply({"from": account})
    print(f"burn successfully, total supply: {total_supply}")


def total_supply():
    account = get_account()
    coin = KongLongCoin[-1]

    total_supply = coin.totalSupply({"from": account})
    print(f"total supply: {total_supply}")