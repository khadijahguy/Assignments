# Creator: Khady Gueye

""" This program stores key-value pairs using a hash function with collision detection. """

class MyCustomMap:
    def __init__(self, N):
        self.size = N
        self.keys = [None] * self.size  # Stores keys
        self.values = [None] * self.size  # Stores corresponding values

    def hash(self, key):
        if isinstance(key, int):
            return key % self.size

        elif isinstance(key, float):
            # Get the fractional part as an integer
            fractional_str = str(key).split('.')[-1]
            fractional_int = int(fractional_str)
            return fractional_int % self.size

        elif isinstance(key, str):
            # Polynomial hash function
            hash_code = 0
            p = 31
            m = 1_000_000_009
            for i, char in enumerate(key):
                hash_code = (hash_code + ord(char) * pow(p, i, m)) % m
            return hash_code % self.size

        else:
            raise Exception("The given key is not supported!")

    def put(self, key, value):
        index = self.hash(key)
        if self.keys[index] is not None and self.keys[index] != key:
            raise Exception("Collision occurred!")
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash(key)
        if self.keys[index] == key:
            return self.values[index]
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)


# Example usage
map = MyCustomMap(11)
map.put(10, 'a')
map.put(22, 'b')
map.put(31, 'c')
map[9] = 'd'
map[15] = 'e'

print(map.get(31))
print(map[15])
print(map.get(44))


