def generate_keypair(bit_length):
    # Generate random prime numbers p and q
    p, q = generate_primes(bit_length)

    # Calculate the modulus N = pq
    N = p * q

    # Calculate the public key lambda = phi(N)
    lambda_N = euler_totient_function(N)

    # Choose a random integer e such that 1 < e < lambda_N and gcd(e, lambda_N) = 1
    e = find_coprime(lambda_N)

    # Calculate the private key d = e^-1 (mod lambda_N)
    d = modular_inverse(e, lambda_N)

    return {"public_key": (N, e), "private_key": d}

def encrypt(message, public_key):
    # Convert the message to an integer
    message_int = int(message)

    # Encrypt the message using the public key
    encrypted_message = pow(message_int, public_key[1], public_key[0])

    return encrypted_message

def decrypt(encrypted_message, private_key, public_key):
    # Decrypt the message using the private key
    decrypted_message = pow(encrypted_message, private_key, public_key[0])

    # Convert the decrypted integer to a string
    decrypted_message_str = str(decrypted_message)

    return decrypted_message_str