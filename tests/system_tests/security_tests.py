import unittest
from ucrp_protocol import *
from homomorphic_encryption import *
from secure_multiparty_computation import *

class SecurityTests(unittest.TestCase):

    def test_key_privacy(self):
        # Generate random public and private keys
        public_key, private_key = generate_key_pair(1024)

        # Distribute decryption key shares among trusted parties
        decryption_key_shares = distribute_decryption_key_shares(private_key, 5)

        # Simulate a malicious trusted party attempting to reconstruct the private key
        malicious_trusted_party = TrustedParty(public_key)
        malicious_trusted_party.contribute_decryption_key_share(decryption_key_shares[0])

        # Verify that the malicious trusted party cannot reconstruct the private key using its own share
        reconstructed_private_key = malicious_trusted_party.reconstruct_private_key()
        self.assertNotEqual(reconstructed_private_key, private_key)

    def test_mpc_security(self):
        # Generate random public and private keys
        public_key, private_key = generate_key_pair(1024)

        # Generate random ciphertext for device1
        device1_ciphertext = generate_ciphertext(10, public_key)

        # Distribute decryption key shares among trusted parties
        decryption_key_shares = distribute_decryption_key_shares(private_key, 5)

        # Simulate a malicious trusted party attempting to learn the plaintext during MPC
        malicious_trusted_party = TrustedParty(public_key)
        malicious_trusted_party.receive_decryption_request(device1_ciphertext)
        malicious_trusted_party.contribute_decryption_key_share(decryption_key_shares[0])

        # Verify that the malicious trusted party cannot learn the plaintext without the combined key
        decryption_attempt = malicious_trusted_party.decrypt_ciphertext(device1_ciphertext, public_key)
        self.assertNotEqual(decryption_attempt.plaintext, device1_ciphertext.plaintext)

if __name__ == "__main__":
    unittest.main()