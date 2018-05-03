
class NetPrimes:

    def __init__(self, n):
        self.n = n
        self.createNewNet(n)

    def createNewNet(self, n):
        newNet = ['x'] * 2 + [0] * (n-1)
        newPrimeList = []
        for i in range(2, n+1):
            if newNet[i] == 0:
                newPrimeList.append(i)
                self.removeFromNet(i, newNet, n)
        self.primeList = newPrimeList
        self.net = newNet

    def removeFromNet(self, nr, net, n):
        for j in list(filter(lambda x: x % nr == 0, range(n + 1))):
            net[j] = 'x'

    def IncreaseNetSize(self, new_n):
        newNet = self.net + [0] * (new_n + 1 - self.n)
        newPrimeList = self.primeList
        for i in newPrimeList:
            self.removeFromNet(i, newNet, new_n)
        for j in range(self.n + 1, new_n + 1):
            if newNet[j] == 0:
                newPrimeList.append(j)
                self.removeFromNet(j, newNet, new_n)
        self.primeList = newPrimeList
        self.n = new_n
        self.net = newNet
