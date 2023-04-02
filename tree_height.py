import random

class HashTable:
    def __init__(self):
        # Initialize the hash table with 500 buckets, a random prime number,
        # and an arbitrary multiplier value
        self.bucket_count = 500
        self._multiplier = 1234
        self._prime = random.randint(0,200)
        self.buckets = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, query):
        # Private method that takes a string and returns a hash value
        ans = 0
        for c in reversed(query):
            ans = (ans * self._multiplier + ord(c) % self._prime)
        return ans % self.bucket_count

    def add(self, string, string2):
        # Method that adds a key-value pair to the hash table
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        # If the key is already present in the bucket, update the value
        for i in range(len(bucket)):
            if bucket[i][0] == string:
                bucket[i] = (string, string2)
                return
        # Otherwise, append the new key-value pair to the bucket
        bucket.append((string, string2))

    def delete(self, string):
        # Method that deletes a key-value pair from the hash table
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        # Search for the key in the bucket, and remove it if found
        for i in range(len(bucket)):
            if bucket[i][0] == string:
                bucket.pop(i)
                break

    def find(self, string):
        # Method that finds the value associated with a given key
        hashed = self._hash_func(string)
        # Search for the key in the appropriate bucket, and return the value if found
        for elem in self.buckets[hashed]:
            if elem[0] == string:
                return elem[1]
        # Return "not found" if the key is not found in the hash table
        return "not found"

if __name__ == '__main__':
    # Main function that reads input queries and executes them on the hash table
    result = []
    n = int(input())
    hash_table = HashTable()  
    for query in range(n):
        query = input().split()
        if query[0] == 'add':
            hash_table.add(query[1], query[2])
        elif query[0] == 'find':
            result.append(hash_table.find(query[1]))
        elif query[0] =='del':
            hash_table.delete(query[1])
    # Print the results of the find queries
    for rez in result:
        print(rez)
