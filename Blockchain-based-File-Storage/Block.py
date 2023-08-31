from hashlib import sha256
class Block:
    def __init__(self, index, transactions, prev_hash, permission, uploader , nonce=0):
        self.index = index
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.permission = permission
        self.uploader = uploader
        self.nonce = nonce

    def generate_hash(self):
        all_data_combined = str(self.index) + str(self.nonce) + self.prev_hash + str(self.transactions)
        return sha256(all_data_combined.encode()).hexdigest()
    
    def add_t(self, t):
        self.transactions.append(t)