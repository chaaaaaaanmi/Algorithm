# 전위순회: 루트-왼-오
def preorder(root):
    if root != ".":
        print(root, end="") # 루트
        preorder(tree[root][0]) # 왼
        preorder(tree[root][1]) # 오

# 중위순회: 왼-루트-오
def inorder(root):
    if root != ".":
        inorder(tree[root][0]) # 왼
        print(root, end="") # 루트
        inorder(tree[root][1]) # 오

# 후위순회: 왼-오-루트
def postorder(root):
    if root != ".":
        postorder(tree[root][0]) # 왼
        postorder(tree[root][1]) # 오
        print(root, end="") # 루트


n = int(input())
tree = {}

for _ in range(n):
    node, left, right = input().split()
    tree[node] = [left, right]

preorder("A")
print()
inorder("A")
print()
postorder("A")