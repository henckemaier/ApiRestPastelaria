from flask_restful import Resource
# Criar os endpoints de Funcionario: GET, POST, PUT, DELETE
class Funcionario(Resource):
        def get(self, id):
                return {"msg": "get executado"}, 200
        def post(self, id):
                return {"msg": "post executado"}, 201
        def put(self, id):
                return {"msg": "put executado"}, 201
        def delete(self, id):
                return {"msg": "delete executado"}, 201

from flask import Flask
from flask_restful import Api
# import das classes com os endpoints
from FuncionarioDAO import Funcionario

app = Flask(__name__)
api = Api(app)
# mapeamento dos endpoints
api.add_resource(Funcionario, "/funcionario/<int:id>", endpoint = 'funcionario')

if __name__ == "__main__":
        """ Inicia a API Flask RESTful """
        app.run(host='0.0.0.0', port=5000, debug=True)