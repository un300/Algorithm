

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
        else :
            self.arr[friend01_idx] = frined02_parent



def solution() :
    T = int(input())
    for _ in range(T) :
        instance = FriendNetwork()
        F = int(input())
        for _ in range(F) :
            F1, F2 = list(input().split())
            instance.getArr(F1)
            instance.getArr(F2)
            
            instance.getUnion(F1, F2)

            print(instance.arr)
            print(instance.index_dict)


solution()

