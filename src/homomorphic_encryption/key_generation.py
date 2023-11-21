import random

def generate_shares(secret_key, number_of_parties):
    # Generate random shares for each party
    shares = []
    for i in range(number_of_parties - 1):
        share_i = random.randint(1, secret_key - 1)
        shares.append(share_i)

    # Calculate the remaining share
    remaining_share = secret_key - sum(shares)
    shares.append(remaining_share)

    return shares

def distribute_shares(shares, number_of_parties):
    # Randomly shuffle the shares
    random.shuffle(shares)

    # Distribute the shares to each party
    distributed_shares = []
    for i in range(number_of_parties):
        distributed_shares.append(shares[i])

    return distributed_shares