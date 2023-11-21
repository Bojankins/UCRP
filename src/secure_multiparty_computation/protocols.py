import random

def secure_shuffle_and_cut(shares, number_of_parties):
    # Randomly shuffle the shares
    random.shuffle(shares)

    # Cut the shuffled shares into two halves
    cut_index = random.randint(1, number_of_parties - 1)
    first_half = shares[:cut_index]
    second_half = shares[cut_index:]

    # Shuffle each half independently
    random.shuffle(first_half)
    random.shuffle(second_half)

    # Combine the shuffled halves
    shuffled_shares = first_half + second_half

    return shuffled_shares

def secure_summation(shares):
    # Sum up the shares
    summed_shares = sum(shares)

    return summed_shares