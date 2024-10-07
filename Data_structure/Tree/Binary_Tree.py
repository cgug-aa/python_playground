#이진 트리를 위한 BinaryTree 클래스
class BinaryTree:
    
    #이진 트리에 포함된 노드
    class Node:
        def __init__(self, item, left=None, right=None):
            self.item=item
            self.left=left
            self.right=right
            
    def __init__(self):
        self.root=None

    #전위순회
    def preorder(self, n):
        if n!=None:
            print(str(n.item), end=" ")
            if n.left!=None:
                self.preorder(n.left)
            if n.right!=None:
                self.preorder(n.right)
    
    #중위 순회
    def inorder(self, n):
        if n!=None:
            if n.left!=None:
                self.inorder(n.left)
            print(str(n.item), end=" ")
            if n.right!=None:
                self.inorder(n.right)
    
    #후위 순회
    def postorder(self, n):
        if n!=None:
            if n.left!=None:
                self.postorder(n.left)
            if n.right!=None:
                self.postorder(n.right)
            print(str(n.item), end=" ")

    #레벨 순회(BFS)
    def levelorder(self, root):                # 레벨순회는 어차피 root부터 시작
        queue=[]
        queue.append(root)
        while len(queue)!=0:
            n=queue.pop(0)
            print(str(n.item), end=" ")
            if n.left!=None:
                queue.append(n.left)           # while문 때문에 재귀함수는 필요없음
            if n.right!=None:
                queue.append(n.right)

    #트리의 높이 계산
    def height(self, root):
        if root==None:
            return 0
        return max(self.height(root.left), self.height(root.right))+1
    
    #노드 개수 계산
    def size(self, root):
        if root is None:
            return 0
        else:
            return 1+self.size(root.left)+self.size(root.right)