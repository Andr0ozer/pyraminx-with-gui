class asnode:
    def __init__(self, parent, arrenagement, distance, heuristic):
        self.parent = parent
        self.arrangement = arrenagement
        self.d = distance
        self.h = heuristic
        self.f = distance+heuristic


class minheap:
    def __init__(self):
        self.queue =[]

    def heapify(self):
        iterator = len(self.queue) - 1
        temp = self.queue[iterator]
        while (iterator > 0 and temp.f < self.queue[iterator-1].f):
            self.queue[iterator] = self.queue[iterator-1]
            iterator = iterator -1

        self.queue[iterator] = temp

    def addn(self,addition):
        self.queue.append(addition)
        self.heapify