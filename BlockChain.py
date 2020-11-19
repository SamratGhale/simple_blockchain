from hashlib import sha256
import json

class Block:
    def __init__(self,messege,nonce,prev):
        self.messege = messege 
        self.nonce = nonce
        self.prev = prev

class BlockChain:
    def __init__(self):
        self.chain = []
        self.jsonChain = []
        self.diff = 4

    def genesisBlock(self):
        self.chain.append(Block("This is this genesis block so it's hash and previous hash has no proof of work",0,"0"))
        self.jsonChain.append(Block("This is this genesis block so it's hash and previous hash has no proof of work",0,"0").__dict__)

    def getHash(self,messege,nonce,prev):
        return sha256(str(messege + str(nonce) + prev).encode()).hexdigest()

    def printBlocks(self):
        for i in self.chain:
            print("prev hash:", i.prev)
            print("messege:" , i.messege)
            print("Nonce:" , i.nonce)
            print("\n\n")

    def proofOfWork(self,messege, prev):
        nonce = 0
        while(self.getHash(messege,nonce,prev)[:self.diff] != "0"*self.diff):
            nonce +=1
        return nonce

    def addBlock(self,messege):
        pBlock = self.chain[-1]
        h = self.getHash(pBlock.messege,pBlock.nonce,pBlock.prev)
        nonce = self.proofOfWork(messege,h)
        print("block added:",h)
        self.chain.append(Block(messege,nonce,h))
        self.jsonChain.append(Block(messege,nonce,h).__dict__)

    def validate(self):
        valid = []
        for i in self.chain:
            h = self.getHash(i.messege,i.nonce,i.prev)
            valid.append(h[:self.diff] == "0"*self.diff)
        valid = valid[1:]
        return all(valid)

if __name__ == "__main__":
    a = BlockChain()
    a.genesisBlock()
    a.addBlock("this is the first block")
    a.addBlock("this is the second block")
    a.addBlock("this is the third block")
    #a.chain[1].messege= "apple"
    a.printBlocks()
    print(a.jsonChain[0])
    print(a.validate())
