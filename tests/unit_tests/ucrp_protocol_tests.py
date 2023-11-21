import unittest
from ucrp_protocol import *

class UCRPProtocolTests(unittest.TestCase):

    def test_ucrp_decryption(self):
        # Generate random public and private keys
        public_key, private_key = generate_key_pair(1024)

        # Generate random ciphertext and decryption key shares
        ciphertext = generate_ciphertext(10, public_key)
        decryption_key_shares = distribute_decryption_key_shares(private_key, 5)

        # Decrypt the ciphertext using UCRP
        decrypted_message = ucrp_decryption(ciphertext, decryption_key_shares, public_key)

        # Verify that the decrypted message is the original plaintext
        self.assertEqual(decrypted_message.plaintext, ciphertext.plaintext)

if __name__ == "__main__":
    unittest.main()