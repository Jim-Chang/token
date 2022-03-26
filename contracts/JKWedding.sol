// contracts/KongLongNFT.sol
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract JKWedding is ERC721URIStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    address public owner;
    string private _uri;

    constructor(address[] memory tokenOwners, string memory baseURI)
        ERC721("JKWedding", "JKW")
    {
        owner = msg.sender;
        _uri = baseURI;

        for (uint8 i = 0; i < tokenOwners.length; i++) {
            _mintToken(tokenOwners[i]);
        }
    }

    function _mintToken(address newOwner) private returns (uint256) {
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(newOwner, newItemId);

        return newItemId;
    }

    function tokenURI(uint256 tokenId)
        public
        view
        virtual
        override
        returns (string memory)
    {
        require(
            _exists(tokenId),
            "ERC721Metadata: URI query for nonexistent token"
        );

        string memory _id = Strings.toString(tokenId);
        if (tokenId < 10) {
            _id = string(abi.encodePacked("0", _id));
        }

        return string(abi.encodePacked(_uri, _id, ".json"));
    }
}
