// contracts/KongLongCoin.sol
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";

contract KongLongCoin is ERC20Burnable {
    address public admin;

    constructor() ERC20("KongLongCoin", "KLC") {
        admin = msg.sender;
    }

    function mint(address account, uint256 amount) public onlyAdmin {
        _mint(account, amount);
    }

    function decimals() public view virtual override returns (uint8) {
        return 2;
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only the admin can do this");
        _;
    }
}
