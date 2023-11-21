import unittest
from homomorphic_encryption import *

class HomomorphicEncryptionTests(unittest.TestCase):

    def test_homomorphic_addition(self):
        # Generate random public and private keys
        public_key, private_key = generate_key_pair(1024)

        # Generate random ciphertexts
        ciphertext1 = generate_ciphertext(10, public_key)
        ciphertext2 = generate_ciphertext(20, public_key)

        # Calculate the expected sum of the plaintexts
        expected_sum = (ciphertext1.plaintext + ciphertext2.plaintext) % public_key[0]

        # Calculate the homomorphic sum
        summed_ciphertext = homomorphic_addition(ciphertext1, ciphertext2, public_key)

        # Decrypt the summed ciphertext and compare it to the expected sum
        decrypted_sum = homomorphic_decryption(summed_ciphertext, private_key, public_key)
        self.assertEqual(decrypted_sum.plaintext, expected_sum)

    def test_homomorphic_multiplication(self):
        # Generate random public and private keys
        public_key, private_key = generate_key_pair(1024)

        # Generate a random ciphertext and a scalar
        ciphertext = generate_ciphertext(10, public_key)
        scalar = random.randint(2, 100)

        # Calculate the expected product of the plaintext and the scalar
        expected_product = (ciphertext.plaintext * scalar) % public_key[0]

        # Calculate the homomorphic product
        multiplied_ciphertext = homomorphic_multiplication(ciphertext, scalar, public_key)

        # Decrypt the multiplied ciphertext and compare it to the expected product
        decrypted_product = homomorphic_decryption(multiplied_ciphertext, private_key, public_key)
        self.assertEqual(decrypted_product.plaintext, expected_product)

if __name__ == "__main__":
    unittest.main()