// Token mint and transfer

program token.aleo {

record Token{
    owner: address,
    amount: u64
}

transition mint(owner: address, amount: u64) -> Token {
    return Token {
        owner: owner,
        amount: amount
    };
}

transition transfer(token: Token, to: address, amount: u64)-> (Token, Token) {
    let difference: u64 = token.amount - amount;

        // Produce a token record with the change amount for the sender.
        let sender: Token = Token {
            owner: token.owner,
            amount: difference,
        };

        // Produce a token record for the specified receiver.
        let recipient: Token = Token {
            owner: to,
            amount: amount,
        };
    return (recipient, sender);
}

}