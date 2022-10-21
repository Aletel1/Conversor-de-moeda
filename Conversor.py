from flask import Flask
from flask import jsonify
from flask import request

app = Flask(_name_)

conv_Din = [
 {
#valores de quando eu escrevi esse codigo
 'real':'1',
 'dolar':'0,19',
 'euro':'0,20'
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

if _name_ == "_main_":
    app.run()
