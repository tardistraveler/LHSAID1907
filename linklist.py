class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkList:
    '''
    思路：生成对象即表示一个单链表对象
         对象调用方法可以完成对单链表的各种操作
    '''

    def __init__(self):

        self.head = Node(None)

    def init_list(self, iter):
        p = self.head
        for i in iter:
            p.next = Node(i)
            p = p.next

    def show(self):
        p = self.head.next
        while p:
            print(p.val)
            p = p.next

    def is_empty(self):
        return self.head.next is None


if __name__ == '__main__':
    link = LinkList()
    link.init_list(range(5))
    link.show()
# node1 = Node(1)
