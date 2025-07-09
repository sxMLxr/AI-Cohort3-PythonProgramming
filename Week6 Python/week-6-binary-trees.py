class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def calc_height(node):
    if node:
        val = max(calc_height(node.left),
                  calc_height(node.right)) + 1
    else:
        val = 0
    return val

def print_inorder(root):  #DEPTH FIRST TRAVERSALS
    if root:
        print_inorder(root.left)
        print(root.val) 
        print_inorder(root.right)
    return
 
def print_postorder(root):   #DEPTH FIRST TRAVERSALS
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.val)
    return
 
def print_preorder(root):  # used for DFS   #DEPTH FIRST TRAVERSALS
    if root:
        print(root.val)
        print_preorder(root.left)
        print_preorder(root.right)
    return
 
def print_level_order(root): # used for BRSearch or Breadth-First Traversal
    queue = []
    if root:
        queue.append(root)
        while len(queue):
            node = queue.pop()
            print(node.val)
            if node.left: queue.insert(0, node.left) 
            if node.right: queue.insert(0, node.right)
    return
 
# Driver code
def fill_tree(size):
    queue = []
    root = None
    index = 1

    for x in range(size):
        queue.append(Node(x+1))
        
    while len(queue):
        node = queue.pop(0)
        index -= 1
        if not root: root = node
        if index < len(queue):
            node.left = queue[index]
            index += 1
        if index < len(queue):
            node.right = queue[index]
            index += 1

    return root

root = fill_tree(6)

print("Height of the tree is: ", end="")
print(calc_height(root))

print("\nPreorder traversal of binary tree is")
print_preorder(root)
 
print("\nInorder traversal of binary tree is")
print_inorder(root)
 
print("\nPostorder traversal of binary tree is")
print_postorder(root)

print("\nLevel order traversal of binary tree is")
print_level_order(root)

# to implement a search, just add logic to stop
# when the node is found with the value desired.