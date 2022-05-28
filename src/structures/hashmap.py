from typing import List


class HashMap:
    INC_CAPACITY_INDEX = 0.7
    INC_CAPACITY_COFF = 1.5

    class Node:
        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next: HashMap.Node = next

        def __repr__(self):
            return f"<Node key: {self.key.__repr__()} data: {self.value.__repr__()}>"

    class LinkedList:
        def __init__(self):
            self.head: HashMap.Node = None
            self.tail: HashMap.Node = None

        def __iter__(self):
            self.cur = self.head
            return self

        def __next__(self):
            if self.cur is None:
                raise StopIteration
            else:
                now_node = self.cur
                self.cur = self.cur.next
                return now_node

        def __len__(self):
            cur = self.head
            cnt = 0
            while cur is not None:
                cur = cur.next
                cnt += 1
            return cnt

        def __setitem__(self, key, value):
            cur = self.head
            while cur is not None:
                if cur.key == key:
                    cur.value = value
                    return
                cur = cur.next
            self.insert_to_end(key, value)

        def __getitem__(self, key):
            cur = self.head
            while cur is not None:
                if cur.key == key:
                    return cur
                cur = cur.next
            assert KeyError

        def __contains__(self, key):
            cur = self.head
            while cur is not None:
                if cur.key == key:
                    return True
                cur = cur.next
            return False

        def insert_to_end(self, key, value):
            new_node = HashMap.Node(key, value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

        def insert(self, key, value, pos):
            if pos == 0:
                new_node = HashMap.Node(key, value, self.head)
                self.head = new_node
                return
            new_node = HashMap.Node(key, value)
            cur = self.head
            now_pos = 0
            while (cur is not None) and now_pos + 1 < pos:
                cur = cur.next
                now_pos += 1
            if cur is None:
                assert IndexError
            else:
                if cur.next is None:
                    cur.next = new_node
                else:
                    new_node.next = cur.next
                    cur.next = new_node

        def __repr__(self):
            cur = self.head
            response = []
            while cur is not None:
                response.append(repr(cur))
                cur = cur.next
            if response == '':
                return 'Empty LinkedList'
            return ', '.join(response)

    def __init__(self, capacity=10):
        self.bucket: List[HashMap.LinkedList] = [HashMap.LinkedList() for _ in range(capacity)]
        self.capacity = capacity
        self.size = 0

    def update_capacity(self, new_capacity):
        new_bucket: List[HashMap.LinkedList] = [HashMap.LinkedList() for _ in range(new_capacity)]
        for strike in self.bucket:
            for node in strike:
                h = hash(node.key) % new_capacity
                new_bucket[h].insert_to_end(node.key, node.value)
        self.bucket = new_bucket
        self.capacity = new_capacity

    def __setitem__(self, key, value):
        h = hash(key) % len(self.bucket)
        if key in self.bucket[h]:
            self.bucket[h][key] = value
        else:
            self.bucket[h].insert_to_end(key, value)
            self.size += 1
        if self.size / self.capacity > HashMap.INC_CAPACITY_INDEX:
            self.update_capacity(int(self.capacity * HashMap.INC_CAPACITY_COFF))

    def __getitem__(self, key):
        h = hash(key) % len(self.bucket)
        if key in self.bucket[h]:
            return self.bucket[h][key]
        else:
            assert KeyError

    def __len__(self):
        return self.size

    def __contains__(self, key):
        h = hash(key) % len(self.bucket)
        return key in self.bucket[h]

    def __repr__(self):
        resp = []
        for i in range(len(self.bucket)):
            resp.append(str(i) + ': ' + self.bucket[i].__repr__())
        return '\n'.join(resp)

    def write_to_file(self, path):
        f = open(path, 'x')
        for ll in self.bucket:
            lst = []
            for item in ll:
                lst.append(item.key.__repr__() + '#' + item.value.__repr__())
            f.write(';'.join(lst) + '\n')
        f.close()

    @classmethod
    def read_from_file(cls, path):
        lst = open(path, 'r').readlines()
        lst = list(filter(lambda x: x != '', map(lambda x: x[:-1], lst)))
        instance = HashMap()
        for strike in lst:
            strike_lst = strike.split(';')
            print(strike_lst)
            for item in strike_lst:
                print(item)
                item_lst = item.split('#')
                print(item_lst)
                key = item_lst[0]
                value = item_lst[1]
                if key[0] == key[-1] == "'":
                    instance[key[1:-1]] = int(value)
                elif key.isdigit() and value.isdigit():
                    instance[int(key)] = int(value)
        return instance

    @classmethod
    def one_from_a_lot(cls, path_lst, write=False):
        instance = HashMap()
        for path in path_lst:
            lst = open(path, 'r').readlines()
            lst = list(filter(lambda x: x != '', map(lambda x: x[:-1], lst)))
            for strike in lst:
                strike_lst = strike.split(';')
                print(strike_lst)
                for item in strike_lst:
                    print(item)
                    item_lst = item.split('#')
                    print(item_lst)
                    key = item_lst[0]
                    value = item_lst[1]
                    if key[0] == key[-1] == "'":
                        instance[key[1:-1]] = int(value)
                    elif key.isdigit() and value.isdigit():
                        instance[int(key)] = int(value)

        return instance

    # ll.insert_to_end('14', 14)
    # print(repr(ll))
    # ll.insert(key='1', value=1, pos=2)
    # print(repr(ll))
    # print('1' in ll)
    # print('12' in ll)
    # print('5' in ll)
    # print(ll['12'])
