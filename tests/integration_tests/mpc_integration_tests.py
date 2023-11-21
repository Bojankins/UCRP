import unittest
from ucrp_protocol import *
from secure_multiparty_computation import *
from homomorphic_encryption import *

class MPCIntegrationTests(unittest.TestCase):

    def test_mpc_integration_with_key_distribution(self):
        # Generate random public and private keys
        public_key, private_key = generate_key_pair(1024)

        # Distribute decryption key shares among trusted parties
        decryption_key_shares = distribute_decryption_key_shares(private_key, 5)

        # Simulate device1 requesting decryption assistance
        trusted_party1 = TrustedParty(public_key)
        trusted_party1.receive_decryption_request(device1_ciphertext)

        # Trusted party1 contributes its decryption key share and MPC data
        trusted_party1.contribute_decryption_key_share(device1_decryption_key_shares[0])
        trusted_party1.contribute_mpc_data(device1_ciphertext)

        # Simulate device2 requesting decryption assistance
        trusted_party2 = TrustedParty(public_key)
        trusted_party2.receive_decryption_request(device1_ciphertext)

        # Trusted party2 contributes its decryption key share and MPC data
        trusted_party2.contribute_decryption_key_share(device1_decryption_key_shares[1])
        trusted_party2.contribute_mpc_data(device1_ciphertext)

        # Simulate device3 requesting decryption assistance
        trusted_party3 = TrustedParty(public_key)
        trusted_party3.receive_decryption_request(device1_ciphertext)

        # Trusted party3 contributes its decryption key share and MPC data
        trusted_party3.contribute_decryption_key_share(device1_decryption_key_shares[2])
        trusted_party3.contribute_mpc_data(device1_ciphertext)

        # Combine decryption key shares and MPC data using MPC
        combined_decryption_key_shares, combined_mpc_data = secure_multiparty_computation(trusted_party1, trusted_party2, trusted_party3)

        # Decrypt the ciphertext using the combined key and MPC data
        decrypted_message = ucrp_decryption(combined_decryption_key_shares, combined_mpc_data, public_key)

        # Verify that the decrypted message is the original plaintext
        self.assertEqual(decrypted_message.plaintext, device1_ciphertext.plaintext)

if __name__ == "__main__":
    unittest.main()