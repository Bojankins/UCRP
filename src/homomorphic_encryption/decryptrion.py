def homomorphic_decryption(encrypted_message, private_key, public_key):
    # Calculate the inverse of the ciphertext
    inverse_ciphertext = modular_inverse(encrypted_message, public_key[0])

    # Exponentiate the inverse ciphertext with the private key
    decrypted_message = pow(inverse_ciphertext, private_key, public_key[0])

    return decrypted_message