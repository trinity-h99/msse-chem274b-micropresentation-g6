class TSTNode:
    """
    Ternary Search Trie (TST)

    Each node stores:
    - a single character
    - an optional value if this character is the end of a full key
    - three child pointers: left, middle, right
    """
    def __init__(self, _character):
        #Each node stores a single character from the key 
        self.character = _character
        #Value only stored at the final character of a full key
        self.val = None
        #Three-way branching
        self.left = None
        self.right = None
        self.middle = None

    def __repr__(self):
        if self.val:
            return f"{self.character} ({self.val})"
        return self.character


class TST:
    def __init__(self):
        #Root node of the TST
        self.root = None

    def put(self, sequence, val):
        """
        Insert a sequence into the TST.
        'val' is whatever value we want to store at the terminal node. 
        """
        self.root = self._put(self.root, sequence, val, 0)

    def _put(self, current_node, sequence, val, index):
        character = sequence[index]
        #Create a new node if needed
        if current_node is None:
            current_node = TSTNode(character)
        #Navigate or insert based on character comparisons
        if current_node.character == character:
            if index == len(sequence) - 1:  # last char in sequence
                current_node.val = val
            else:
                #for sunsequent characters, continued down the middle
                current_node.middle = self._put(current_node.middle, sequence, val, index + 1)
        elif character < current_node.character:
            #Searching left subtree for smaller characters
            current_node.left = self._put(current_node.left, sequence, val, index)
        else:
            #Searching right subtree for larger characters
            current_node.right = self._put(current_node.right, sequence, val, index)

        return current_node


    def contains(self, sequence):
        #Checking if a full sequence exists in the TST
        return self.get(sequence) is not None

    def get(self, sequence):
        # Retrieving the value associated with a full sequence, if none found it returns None
        node = self._get(self.root, sequence, 0)
        if node is None:
            return None
        return node.val

    def _get(self, current_node, sequence, index):
        if current_node is None:
            return None
        character = sequence[index]
        #Character matches: move forward in the string
        if current_node.character == character:
            if index == len(sequence) - 1:  # last char in sequence
                return current_node
            else:
                return self._get(current_node.middle, sequence, index + 1)
        #Otherwise navigate left or right    
        elif character < current_node.character:
            return self._get(current_node.left, sequence, index)
        else:
            return self._get(current_node.right, sequence, index)
        

class IterativeTST:
    """
    Iterative implementation of a Ternary Search Trie.
    Eliminates recursion, this has the same behavior but more memory efficient.
    """
    def __init__(self):
        self.root = None

    def put(self, key, value):
        # Insert key but not using recursion
        if not key:
            return
        # Initilize root if empty
        if self.root is None:
            self.root = TSTNode(key[0])
        node = self.root
        index = 0
        # Loop until full key is inserted
        while True:
            c = key[index]
            #Navigate left
            if c < node.character:
                if node.left is None:
                    node.left = TSTNode(c)
                node = node.left
                #Navigate right
            elif c > node.character:
                if node.right is None:
                    node.right = TSTNode(c)
                node = node.right
            else:  # c == node.char
                index += 1
                if index == len(key):
                    node.val = value
                    return
                if node.middle is None:
                    node.middle = TSTNode(key[index])
                node = node.middle

    def get(self, key):
        """
        Iterative search implementation.
        Returns stored value or None if key not found.
        """
        if not key or self.root is None:
            return None
        node = self.root
        index = 0
        while node:
            c = key[index]
            if c < node.character:
                node = node.left
            elif c > node.character:
                node = node.right
            else:
                index += 1
                if index == len(key):
                    return node.val
                node = node.middle
        #If traversal ends with no match
        return None

    def contains(self, key):
        return self.get(key) is not None
