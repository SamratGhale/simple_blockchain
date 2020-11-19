from flask import Flask , jsonify, render_template, request
from BlockChain import  BlockChain
import json

app = Flask(__name__)

blockS = BlockChain()
blockS.genesisBlock()
blockS.addBlock("samrat ghale")

@app.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/get_chain',methods=['GET','POST'])
def get_chain():
    if request.method == 'POST':
        messege = request.form.get('messege')
        blockS.addBlock(messege)
    return jsonify(blockS.jsonChain)

if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)
