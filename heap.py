class heap(object):
    def __init__(self):
        self.list = []

    def percup(self,i):
        while (i+1)/2 >0 :
            if self.list[i][1] < self.list[(i-1)/2][1]:
                self.list[i],self.list[(i-1)/2] = self.list[(i-1)/2],self.list[i]
            i = (i-1)/2

    def insert(self,item):
        self.list.append(item)
        self.percup(len(self.list)-1)

    def minchild(self,i):
        if (2 * i)+2 > len(self.list)-1:
            return (2 * i) + 1
        if self.list[(2 * i)+1][1] > self.list[(2 * i)+2][1]:
            return (2 * i) + 2
        return (2 * i) + 1

    def percdown(self,i):
        while (2 * i) < len(self.list)-1:
            minchild = self.minchild(i)
            #print minchild, i, self.list
            if self.list[minchild][1] < self.list[i][1]:
                self.list[minchild],self.list[i] = self.list[i],self.list[minchild]
            i = minchild

    def extractmin(self):
        min = self.list[0]
        self.list[0] = self.list[len(self.list)-1]
        del self.list[-1]
        self.percdown(0)
        return min
        
if __name__ == "__main__":
    letters = heap()
    letters.insert(["z",26])
    letters.insert(["c",3])
    letters.insert(["m",13])
    letters.insert(["f",6])
    letters.insert(["v",22])
    letters.insert(["p",16])
    letters.insert(["a",1])
    while len(letters.list)>0:
        print letters.list
        print letters.extractmin()
