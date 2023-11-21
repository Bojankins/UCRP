import random

def distribute_decryption_key_shares(decryption_key, number_of_parties):
    # Generate random shares for the decryption key
    decryption_key_shares = generate_shares(decryption_key, number_of_parties)

    # Shuffle the shares securely
    shuffled_shares = secure_shuffle_and_cut(decryption_key_shares, number_of_parties)

    # Distribute the shuffled shares to each party
    distributed_shares = []
    for i in range(number_of_parties):
        distributed_shares.append(shuffled_shares[i])

    return distributed_shares