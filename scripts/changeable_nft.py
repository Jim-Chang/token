from brownie import ChangeableNFT, network, config
from scripts.utils import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
import json

URI = 'https://koding.work/token-metadata.json?preview=true'

def deploy():
    account = get_account()

    nft = ChangeableNFT.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {nft.address}")
    return nft


def mint():
    nft = ChangeableNFT[-1]
    account = get_account()

    nft.mintToken(
        account,
        URI,
        {"from": account},
    )

    current_token_id = nft.getCurrentTokenId({"from": account})
    print(f"mint successfully, token id: {current_token_id}")


def get_uri(nft_id):
    nft = ChangeableNFT[-1]
    account = get_account()
    uri = nft.tokenURI(nft_id, {"from": account})
    print(f"ntf_id {nft_id} uri is {uri}")
