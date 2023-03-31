
from flask import Flask,jsonify,request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify(products)
   # return jsonify(products)

@app.route('/products',methods=['GET'])
def getProducts():
    return jsonify({"products":products,"cantidad":products.__len__()})
    

@app.route('/products/<string:nombre>',methods=['GET'])
def getProduct(nombre):
    productFound= [product for product in products if product['nombre']== nombre]
    if (len(productFound) > 0):
        return jsonify(productFound)
    return jsonify({"error":"no se encontro el producto"})

@app.route('/products',methods=['POST'])
def addProduct():
    new_producto={
        "nombre":request.json['nombre'],
        "cantidad":request.json['cantidad'],
        "precio":request.json['precio'],
        "categoria":request.json['categoria'],
    }
    products.append(new_producto)
    return jsonify({'message':'producto agregado al stock '+ request.json['nombre']})

@app.route('/products/<string:nombre>',methods=['PUT'])
def editProduct(nombre):
    productFound= [product for product in products if product['nombre']== nombre]
    if (len(productFound) > 0):
        productFound[0]["nombre"]= request.json['nombre']
        productFound[0]["precio"]= request.json['precio']
        productFound[0]["categoria"]= request.json['categoria']
        productFound[0]["cantidad"]= request.json['cantidad']
        return jsonify({"message":"Producto actualizado","product":productFound[0]})
    return jsonify({"error":"no se encontro el producto"})

@app.route('/products/<string:nombre>',methods=['DELETE'])
def deleteProduct(nombre):
    productFound= [product for product in products if product['nombre']== nombre]
    if (len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({"message":"Producto eliminado","product":productFound[0]})
    return jsonify({"error":"no se encontro el producto "})
        
    
    
if __name__ == '__main__':
    app.run(debug=True,port=4000)