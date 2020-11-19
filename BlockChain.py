from hashlib import sha256
class Block:
    def __init__(self,prev,messege,nonce):
        self.prev = prev
        self.messege = messege
        self.nonce = nonce

class BlockChain:
    def __init__(self):
        self.chain = []
    def getHash(self,messege,nonce,prev):
        return sha256(str(messege + str(nonce) +str(prev)).encode()).hexdigest()
    def proofOfWork(self,messege):
        nonce = 0
        #prev = self.chain[-1].prev
        prev = self.getPrevHash()
        h = self.getHash(messege,nonce,prev)
        while(h[:4] !="0000"):
            h = self.getHash(messege,nonce,prev)
            nonce +=1
        return nonce
    def getPrevHash(self):
        m = self.chain[-1].messege
        n = self.chain[-1].nonce
        p = self.chain[-1].prev
        return self.getHash(m,n,p)
    def addBlock(self,messege):
        nonce = self.proofOfWork(messege)
        self.chain.append(Block(self.getPrevHash(),messege,nonce))
    def genesisBlock(self):
        self.chain.append(Block(0,"0",0))
    def printChain(self):
        for i in self.chain:
            print("messege:",i.messege)
            print("previous hash:",i.prev)
            print("nonce:",i.nonce)

    def validate(self):
        """
        for i in self.chain:
            h = self.getHash(i.messege,i.nonce,i.prev)
            valid.append(h[:4] == "0000")
            print(h)
        valid = valid[1:]
        return all(valid)
        """
        print(self.getPrevHash())

if __name__ == "__main__":
    a = BlockChain()
    a.genesisBlock()
    a.addBlock("samrat")
    a.printChain()
    a.validate()
