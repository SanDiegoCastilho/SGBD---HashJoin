class HashTable:
    ht = [[]]

    def __init__(self, tsize):
        self.ht = [[] for _ in range(tsize)]

    def showHT(self):
        print(self.ht)

    def insert(self, key, value):
        hashk = hash(key) % len(self.ht)
        bucket = self.ht[hashk]
        bucket.append(value)

    def search(self, key):
        hash_key = hash(key) % len(self.ht)
        bucket = self.ht[hash_key]
        for i in range(0, len(bucket)):
            for z in range(0, len(bucket[i])):
                if bucket[i][z] == key:
                    return bucket[i]
        return None









