const INFURA_ID = "23VXCqsIIKpXHc0sXnAhoaSXhve";

const chains = [
  {
    id: 1,
    token: "ETH",
    label: "Ethereum Mainnet",
    rpcUrl: `https://mainnet.infura.io/v3/${INFURA_ID}`,
  },
  {
    id: 42161,
    token: "ARB-ETH",
    label: "Arbitrum One",
    rpcUrl: "https://rpc.ankr.com/arbitrum",
  },
  {
    id: "0xa4ba",
    token: "ARB",
    label: "Arbitrum Nova",
    rpcUrl: "https://nova.arbitrum.io/rpc",
  },
  {
    id: 137,
    token: "MATIC",
    label: "Matic Mainnet",
    rpcUrl: "https://matic-mainnet.chainstacklabs.com",
  },
  {
    id: "0x2105",
    token: "ETH",
    label: "Base",
    rpcUrl: "https://mainnet.base.org",
  },
];

export default chains;
