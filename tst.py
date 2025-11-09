class TSTNode:
    def __init__(self, _character):
        self.character = _character
        self.val = None
        self.left = None
        self.right = None
        self.middle = None


class TST:
    def __init__(self):
        self.root = None

    def put(self, sequence, val):
        self.root = self.put(self.root, sequence, val, 0)

    def _put(self, current_node, sequence, val, index):
        character = sequence[index]
        if current_node is None:
            current_node = TSTNode(character)

        if current_node.character == character:
            if index == len(sequence) - 1:  # last char in sequence
                current_node.val = val
            else:
                current_node.middle = self._put(current_node.middle, sequence, val, index + 1)
        elif character < current_node.character:
            current_node.left = self._put(current_node.left, sequence, val, index)
        else:
            current_node.right = self._put(current_node.right, sequence, val, index)

        return current_node


    def contains(self, sequence):
        return self.get(sequence) is not None

    def get(self, sequence):
        node = self._get(self.root, sequence, 0)
        if node is None:
            return None
        return node.val

    def _get(self, current_node, sequence, index):
        if current_node is None:
            return None
        character = sequence[index]
        if current_node.character == character:
            if index == len(sequence) - 1:  # last char in sequence
                return current_node.val
            else:
                return self._get(current_node.middle, sequence, index + 1)
        elif character < current_node.character:
            return self._get(current_node.left, sequence, index)
        else:
            return self._get(current_node.right, sequence, index)
