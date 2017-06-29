import heap

class node(object):
    def __init__(self, weight, left = None, right = None, parent = None, value = None):
        self.left = left
        self.right = right
        self.parent = parent
        self.weight = weight
        self.value = value

    def __str__(self):
        return self.value

def huffman(values):
    """Argument is a list of lists containing two elements, a value, and the value's weight"""
    tree = heap.heap()
    for value in values:
        tree.insert([node(weight = value[1], value = value[0]), value[1]])
    while len(tree.list) > 1:
        min1 = tree.extractmin()
        min2 = tree.extractmin()
        tree.insert([node(left = min1, right = min2, weight = min1[1] + min2[1]), min1[1] + min2[1]])
    return tree.list[0]

def tableofvalues(atree,table,path):
    if atree[0].left:
        table = tableofvalues(atree[0].left, table, path+"0")
        table = tableofvalues(atree[0].right, table, path+"1")
    else:
        table[atree[0].value] = path
    return table

def frequency(astring):
    frequencies = []
    for char in astring:
        found = False
        for pair in frequencies:
            if char == pair[0]:
                pair[1] = pair[1] + 1
                found = True
        if not found:
            frequencies.append([char,1])
    return frequencies

def encode(atable, astring):
    return "".join([atable[char] for char in astring])

def decode(atree, astring):
    result = ""
    i = 0
    while i < len(astring):
        anode = atree[0]
        while anode.left:
            j = astring[i]
            if int(j):
                anode = anode.right[0]
            else:
                anode = anode.left[0]
            i += 1
        result += anode.value
    return result



if __name__ == '__main__':
    string = "The quick brown fox jumps over the lazy dog."
    tree = huffman(frequency(string))
    table = tableofvalues(tree,{},"")
    encoding = encode(table, string)
    print decode(tree, encoding)
