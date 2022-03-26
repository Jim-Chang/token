from brownie import JKWedding, network, config
from scripts.utils import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
import json

jim_addr = "0x90fd1ab785328456cd5d71acb8265fc8b771791c"
kate_addr = "0xB4531a14fd2d92C5026B8EdCA8fAEB3104Bd0a85"

token_owners = [jim_addr]*15 + [kate_addr]*15
token_owners

base_token_uri = 'ipfs://QmWene5pWwrmiqQGPdw1GB8xHZ4bB8o26cBhvmhe5TiWSJ/'



def deploy():
    account = get_account()

    nft = JKWedding.deploy(
        token_owners,
        base_token_uri,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {nft.address}")
    return nft


def get_uri(token_id):
    account = get_account()
    nft = JKWedding[-1]

    uri = nft.tokenURI(
        token_id,
        {"from": account},
    )
    print(uri)
