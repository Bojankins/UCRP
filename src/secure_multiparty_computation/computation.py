def homomorphic_decryption_computation(encrypted_message, decryption_key_shares, public_key):
    # Calculate the product of the encrypted message and the decryption key shares
    partial_decrypted_messages = []
    for share in decryption_key_shares:
        partial_decrypted_message = homomorphic_multiplication(encrypted_message, share, public_key)
        partial_decrypted_messages.append(partial_decrypted_message)

    # Securely sum the partial decrypted messages
    decrypted_message = secure_summation(partial_decrypted_messages)

    return decrypted_message

    