import sys
input = sys.stdin.readline

L = [-1]*26
R = [-1]*26

n = int(input())
for _ in range(n):
    p, l, r = input().split()
    pi = ord(p)-65
    L[pi] = -1 if l=='.' else ord(l)-65
    R[pi] = -1 if r=='.' else ord(r)-65

def preorder(u):
    if u==-1: 
        return
    print(chr(65+u), end='')
    preorder(L[u])
    preorder(R[u])

def inorder(u):
    if u==-1: 
        return
    inorder(L[u])
    print(chr(65+u), end='')
    inorder(R[u])

def postorder(u):
    if u==-1: 
        return
    postorder(L[u])
    postorder(R[u])
    print(chr(65+u), end='')

root = 0
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
