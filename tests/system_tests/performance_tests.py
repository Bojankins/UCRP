import time
import ucrp_protocol as ucrp
from homomorphic_encryption import generate_ciphertext
from secure_multiparty_computation import secure_multiparty_computation

def measure_decryption_time(decryption_key_shares, ciphertext, public_key):
    start_time = time.time()
    ucrp.ucrp_decryption(decryption_key_shares, ciphertext, public_key)
    end_time = time.time()
    return end_time - start_time

def measure_mpc_time(trusted_party1, trusted_party2, trusted_party3, ciphertext):
    start_time = time.time()
    secure_multiparty_computation(trusted_party1, trusted_party2, trusted_party3, ciphertext)
    end_time = time.time()
    return end_time - start_time

def run_performance_tests():
    # Generate random public and private keys
    public_key, private_key = ucrp.generate_key_pair(1024)

    # Generate random ciphertext
    ciphertext = generate_ciphertext(10, public_key)

    # Distribute decryption key shares among trusted parties
    decryption_key_shares = ucrp.distribute_decryption_key_shares(private_key, 5)

    # Measure decryption time for different data sizes
    for data_size in range(10, 1000, 10):
        ciphertext = generate_ciphertext(data_size, public_key)
        decryption_time = measure_decryption_time(decryption_key_shares, ciphertext, public_key)
        print(f"Data size: {data_size} | Decryption time: {decryption_time:.3f} seconds")

    # Measure MPC time for different data sizes
    for data_size in range(10, 1000, 10):
        ciphertext = generate_ciphertext(data_size, public_key)
        mpc_time = measure_mpc_time(trusted_party1, trusted_party2, trusted_party3, ciphertext)
        print(f"Data size: {data_size} | MPC time: {mpc_time:.3f} seconds")

if __name__ == "__main__":
    run_performance_tests()