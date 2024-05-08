PROGRAM_ID="token_raktim"

snarkos developer deploy \
--private-key <my-leo-wallet-private-key> \
--query https://api.explorer.aleo.org/v1 \
--priority-fee 0 \
"${PROGRAM_ID}.aleo" \
--path ./build/ \
--broadcast https://api.explorer.aleo.org/v1/testnet3/transaction/broadcast