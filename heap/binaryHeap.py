
# this heap is meant for dijkstras and not meant to contain duplicate values


class CustomHeap:
    def __init__(self):
        self.aHeap = []
        self.pos = {}
        self.aHeapsize = len(self.aHeap) - 1

    def insert(self,value):
        self.aHeap.append(value)
        self.aHeapsize += 1
        self.pos[value] = self.aHeapsize

        _child_idx = self.aHeapsize
        _parent_idx = (_child_idx-1)//2

        while _child_idx >  0 and self.aHeap[_child_idx] > self.aHeap[_parent_idx]:

            self.pos[self.aHeap[_child_idx]] = _parent_idx
            self.pos[self.aHeap[_parent_idx]] = _child_idx

            self.aHeap[_child_idx] , self.aHeap[_parent_idx] = self.aHeap[_parent_idx] , self.aHeap[_child_idx]

            _child_idx = _parent_idx
            _parent_idx = (_child_idx-1)//2

    def heapify(self,index):

        largest = index
        left = 2*index + 1
        right = 2*index + 2

        if(left <= self.aHeapsize and self.aHeap[left] > self.aHeap[largest]):
            largest = left

        if(right <= self.aHeapsize and self.aHeap[right] > self.aHeap[largest]):
            largest = right

        if(largest != index):
            self.pos[self.aHeap[index]] = largest
            self.pos[self.aHeap[largest]] = index
            self.aHeap[index] , self.aHeap[largest] = self.aHeap[largest] , self.aHeap[index]


            self.heapify(largest)

    def deleteMax(self):
        if self.aHeapsize > 0:

            del self.pos[self.aHeap[0]]
            self.pos[self.aHeap[self.aHeapsize]] = 0

            self.aHeap[0],self.aHeap[self.aHeapsize] =  self.aHeap[self.aHeapsize],self.aHeap[0]



            self.aHeapsize -= 1
            self.heapify(0)

aHeap = CustomHeap()


aHeap.insert(10)
aHeap.insert(25)
aHeap.insert(1)
aHeap.insert(2)

print(aHeap.aHeap)


aHeap.deleteMax()


print(aHeap.aHeap)

print(aHeap.pos)
