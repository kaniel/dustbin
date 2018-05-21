# -*- coding:utf-8 -*-
__author__ = 'keniel'

# 单链表 单链表 加数


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        # self.__data = value
        # self.__next = None

    # def setData(self, value):
    #     self.__data = value
    #
    # def setNext(self, newNode):
    #     self.__next = newNode
    #
    # def getData(self):
    #     return self.__data
    #
    # def getNext(self):
    #     return self.__next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # self.__head = None
        # self.__tail = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def append_value(self, value):
        node = Node(value)
        print "append node:", node, value
        # print "value:", node.getData(), node.getNext()
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def iter_link(self):
        if not self.head:
            return
        cur = self.head
        yield cur.data
        while cur.next:
            cur = cur.next
            yield cur.data

    def insert_value(self, idx, value):
        print "insert---->", idx, value
        cur = self.head
        cur_idx = 0
        if cur is None:
            raise Exception("This is an empty link!")
        if idx == 0:
            node = Node(value)
            node.next = cur
            self.head = node
            return
        while cur_idx < idx - 1:
            print "diao..."
            cur = cur.next
            if cur is None:
                raise Exception("list length less than index!")
            cur_idx += 1

        node = Node(value)
        node.next = cur.next
        cur.next = node
        print "insert-->data:", cur.data, self.head, self.head.data, node.next.data, self.head.next.data, cur_idx
        if node.next is None:
            self.tail = node

    def remove_value(self, idx):
        print "remove %s..." % idx

    def search_idx(self, idx):
        if self.head is None:
            return
        cur_idx = 0
        cur = self.head
        # value = None
        while cur_idx < idx:
            cur = cur.next
            if cur is None:
                raise Exception("list length less than index!")
            cur_idx += 1
        return cur.data

    def modify_value(self, idx, value):
        print "modify-->", idx, value
        if self.head is None:
            return
        cur_idx = 0
        cur = self.head
        while cur_idx < idx:
            cur = cur.next
            if cur is None:
                raise Exception("list length less than index!")
            cur_idx += 1
        cur.data = value
        print "modify ->", cur.data
        # return cur.data


class Plus:
    def __init__(self, link_list1, link_list2):
        self.link1 = link_list1
        self.link2 = link_list2
        self.len_link1 = 0
        self.len_link2 = 0

    def plus_link(self):
        l1 = self.link1.iter_link()
        print "L1:", type(l1), l1
        l1_len = 0
        for node in l1:
            l1_len += 1
            print "Node is {0}".format(node), type(node)

        l2 = self.link2.iter_link()
        print "L2:", type(l2), l2
        l2_len = 0
        for node in l2:
            l2_len += 1
            print "Node is {0}".format(node), type(node)
        print l1_len, l2_len
        self.len_link1 = l1_len
        self.len_link2 = l2_len
        if l1_len >= l2_len:
            plus_list = range(l1_len - l2_len, l1_len)
            l2_list = range(l2_len)
            print "plus_list:", plus_list[::-1]
            plus_list_reverse = plus_list[::-1]
            plus_list_l2 = l2_list[::-1]
            print "plus_list:", plus_list_reverse, plus_list_l2
            increase_num = 0
            for item in range(len(plus_list_reverse)):
                num1 = self.link1.search_idx(plus_list_reverse[item])
                num2 = self.link2.search_idx(plus_list_l2[item])
                print "res:", type(num1), num1, type(num2), num2
                total = num1 + num2 + increase_num
                increase_num = total / 10
                num = total % 10
                print "set...", increase_num, num
                self.link1.modify_value(plus_list_reverse[item], num)
            print "len_link:", self.len_link1, self.len_link2
            inser_idx = self.len_link1 - self.len_link2 - 1
            while True:

                if increase_num != 0:
                    print "modify l2:", increase_num, inser_idx
                    if inser_idx < 0:
                        print "insert value:", increase_num
                        self.link1.insert_value(0, increase_num)
                        break
                    num1 = self.link1.search_idx(inser_idx)
                    print "num1:", num1
                    total = increase_num + num1
                    increase_num = total / 10
                    num = total % 10
                    print "increase:", increase_num, num, total
                    self.link1.modify_value(inser_idx, num)
                    inser_idx -= 1
                else:
                    break
        else:
            print "..."

    def get_result(self):
        return [str(item) for item in self.link1.iter_link()]

if __name__ == "__main__":
    linked1 = LinkedList()
    for item in [1, 1, 1, 1, 1, 1, 1]:
        linked1.append_value(item)

    linked2 = LinkedList()
    for item in [1, 1, 1, 1, 1, 1, 1]:
        linked2.append_value(item)

    p = Plus(linked1, linked2)
    p.plus_link()
    res = p.get_result()
    result = ''.join(res)
    print "res===>", result

