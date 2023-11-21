from homomorphic_encryption import *
from secure_multiparty_computation import *


def ucrp_decryption(encrypted_message, decryption_key, public_key, number_of_parties):
    # Generate and distribute decryption key shares
    decryption_key_shares = distribute_decryption_key_shares(decryption_key, number_of_parties)

    # Perform homomorphic decryption computation using MPC
    decrypted_message = homomorphic_decryption_computation(encrypted_message, decryption_key_shares, public_key)

    return decrypted_message