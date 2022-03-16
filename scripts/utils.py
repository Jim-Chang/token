from brownie import network, config, accounts
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
ALL_LOCAL_ENVIRONMENTS = LOCAL_BLOCKCHAIN_ENVIRONMENTS + FORKED_LOCAL_ENVIRONMENTS

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    network_name = network.show_active()
    if network_name in ALL_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.load(config["networks"][network_name]["account"])
