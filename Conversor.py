from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

conv_Din = [
 {
#valores de quando eu escrevi esse codigo
 'real':'1',
 'dolar':'5,34',
 'euro':'5,33'
 }
 ]

#A URL deverá ser <http://nome_da_maquina.dominio/convertemoeda/<VALOR>
@app.route('/convertemoeda',methods=['GET'])
def getAllEmp():
    return jsonify({'Valores':conv_Din})

@app.route('/convertemoeda/<VALOR>',methods=['GET'])
def getVal(VALOR):
    conv = [
        {
            'real': VALOR,
            'dolar': (int(VALOR) * 0.19),
            'euro': (int(VALOR) * 0.20)
        }
    ]
    return jsonify({'Valores':conv})

if __name__ == "__main__":
    app.run()
