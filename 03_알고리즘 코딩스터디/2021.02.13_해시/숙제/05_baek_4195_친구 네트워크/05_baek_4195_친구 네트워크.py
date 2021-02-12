

class FriendNetwork :
    def __init__(self) :
        self.arr = []
        self.index_dict = {}
        self.index = 0

    def getArr(self, friend) :
        if friend not in self.index_dict.keys() :
            self.index_dict[friend] = self.index
            self.arr.append(self.index)
            self.index += 1


    def getParent(self, friend_index) :
        if self.arr[friend_index] == friend_index :
            return friend_index
        else :
            return self.getParent(self.arr[friend_index])

    def getUnion(self, friend01, friend02) :
        friend01_idx = self.index_dict[friend01]
        friend02_idx = self.index_dict[friend02]

        friend01_parent = self.getParent(friend01_idx)
        friend02_parent = self.getParent(friend02_idx)

        if friend01_parent < friend02_parent :
            self.arr[friend02_idx] = friend01_parent
            while friend02_parent in self.arr  :
                index = self.arr.index(friend02_parent)
                self.arr[index] = friend01_parent
        else :
            self.arr[friend01_idx] = frined02_parent
            while friend01_parent in self.arr :
                index = self.arr.index(friend01_idx)
                self.arr[index] = friend02_parent

    def print_network(self) :
        print(self.arr.count(0))

import sys


def solution() :
    fast_input = sys.stdin.readline
    T = int(fast_input().rstrip())
    for _ in range(T) :
        instance = FriendNetwork()
        F = int(fast_input().rstrip())
        for _ in range(F) :
            F1, F2 = list(fast_input().rstrip().split())
            instance.getArr(F1)
            instance.getArr(F2)
            
            instance.getUnion(F1, F2)
            instance.print_network()
        

solution()

