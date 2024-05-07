// SPDX-License-Identifier: MIT
pragma solidity 0.8.22;

import "@api3/contracts/api3-server-v1/proxies/interfaces/IProxy.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PriceFeed is Ownable {
    address public ethPriceFeed;
    address public btcPriceFeed;

    constructor() Ownable(msg.sender) {}

    function setupEthFeed(address _ethPriceFeed) external onlyOwner {
        ethPriceFeed = _ethPriceFeed;
    }

    function setupBtcFeed(address _btcPriceFeed) external onlyOwner {
        btcPriceFeed = _btcPriceFeed;
    }

    function readDataFeed()
        public
        view
        returns (uint256, uint256, uint256, uint256)
    {
        (int224 ethValue, uint256 ethTimestamp) = IProxy(ethPriceFeed).read();
        uint256 ethPrice = uint224(ethValue);
        (int224 btcValue, uint256 btcTimestamp) = IProxy(btcPriceFeed).read();
        uint256 btcPrice = uint224(btcValue);
        return (ethPrice, ethTimestamp, btcPrice, btcTimestamp);
    }
}
// ETH/USD API3 Proxy Address (Sepolia Testnet)
// 0x7ca46444D0F56594E251a02efA5422e8bc21bDA8
// BTC/USD API3 Proxy Address (Sepolia Testnet)
// 0xbCE2db9B25095e704D4B3e094cC5E44AFe956c0F
