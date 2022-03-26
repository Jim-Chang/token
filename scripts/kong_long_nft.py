from brownie import KongLongNFT, network, config
from scripts.utils import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
import json


def deploy():
    account = get_account()

    kong_long = KongLongNFT.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {kong_long.address}")
    return kong_long


def auto_mint():
    nft = KongLongNFT[-1]
    account = get_account()
    current_token_id = nft.getCurrentTokenId({"from": account})

    with open("static/kong_long/kong_long.json", "r") as f:
        data = json.load(f)

    for item in data:
        if item["id"] > current_token_id:
            mint(item["uri"], item["owner"], account)


def mint(uri, receiver=None, account=None):
    nft = KongLongNFT[-1]
    if account is None:
        account = get_account()

    if receiver is None:
        receiver = account

    nft.mintToken(
        receiver,
        f"ipfs://{uri}",
        {"from": account},
    )

    current_token_id = nft.getCurrentTokenId({"from": account})
    print(f"mint successfully, token id: {current_token_id}")


def get_uri(nft_id):
    nft = KongLongNFT[-1]
    account = get_account()
    uri = nft.tokenURI(nft_id, {"from": account})
    print(f"ntf_id {nft_id} uri is {uri}")


def get_owner(nft_id):
    nft = KongLongNFT[-1]
    account = get_account()
    owner = nft.ownerOf(nft_id, {"from": account})
    print(f"ntf_id {nft_id} owner is {owner}")
