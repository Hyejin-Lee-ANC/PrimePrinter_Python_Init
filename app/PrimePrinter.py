
class PrimePrinter:

    @staticmethod
    def main(self):
        self._M = 1000
        self._RR = 50
        self._CC = 4
        self._ORDMAX = 30
        self._P = [0 ] *(self._M +1)
        self._PAGENUMBER = 0
        self._PAGEOFFSET = 0
        self._ROWOFFSET = 0
        self._C = 0
        self._N = 0
        self._MULT = [0 ] *(self._ORDMAX +1)

        self._J =1
        self._K =1
        self._P[1] = 2
        self._ORD = 2
        self._SQUARE = 9

        while self._K < self._M:

            self._JPRIME = False
            while not self._JPRIME:
                self._J += 2
                if self._J == self._SQUARE:
                    self._ORD += 1
                    self._SQUARE = self._P[self._ORD ] *self._P[self._ORD]
                    self._MULT[self._ORD -1 ] =self._J
                
                self._N =2
                self._JPRIME =True
                while self._N < self._ORD and self._JPRIME:
                    while self._MULT[self._N ] <self._J:
                        self._MULT[self._N] += self._P[self._N] + self._P[self._N]
                    if self._MULT[self._N] == self._J:
                        self._JPRIME = False
                    self._N += 1


            self._K += 1
            self._P[self._K ] =self._J


        self._PAGENUMBER = 1
        self._PAGEOFFSET = 1
        while self._PAGEOFFSET <= self._M:
            print("The First %d Prime Numbers === Page %d"%(self._M, self._PAGENUMBER))
            print()

            for self._ROWOFFSET in range(self._PAGEOFFSET, self._PAGEOFFSET + self._RR):
                for self._C in range(self._CC):
                    if self._ROWOFFSET + self._C * self._RR <= self._M:
                        print("%10d"%(self._P[self._ROWOFFSET + self._C * self._RR]), end='')
                print()
            
            print("\f")
            self._PAGENUMBER += 1
            self._PAGEOFFSET += self._RR * self._CC
