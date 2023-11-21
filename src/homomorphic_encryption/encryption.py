def homomorphic_addition(ciphertext_1, ciphertext_2, public_key):
    # Calculate the product of the two ciphertexts
    product = ciphertext_1 * ciphertext_2 % public_key[0]

    return product

def homomorphic_multiplication(ciphertext, scalar, public_key):
    # Calculate the exponentiation of the ciphertext
    exponentiation = pow(ciphertext, scalar, public_key[0])

    return exponentiation