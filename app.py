from flask import Flask, jsonify, request, make_response
import psutil
import platform

app = Flask(__name__)

# endpoint para acessar os dados em tempo real
@app.get('/realtime-status')
def get_cpu_usage():

    autenticacao = request.headers.get('Authorization')
    
    if not autenticacao:
        resposta = {
            "mensagem": "Erro de autenticação",
            "detalhe" : "Não foi encontrada informações de autenticação"
        }
        return make_response(resposta, 401)
    
    if not autenticacao == ("sua chave aqui"):
        resposta = {
            "mensagem": "Erro de autenticação",
            "detalhe": "Erro ao validar o token"
        }
        return make_response(resposta, 401)

    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return make_response(jsonify({
        "cpu_usage": f"{cpu_percent}%",
        "memory_usage": f"{memory.percent}%",
        "disk_usage": f"{disk.percent}%"
    }),200)


# endpoint para acessar os dados estáticos
@app.get('/static-infos')
def system_status():

    autenticacao = request.headers.get('Authorization')
    
    if not autenticacao:
        resposta = {
            "mensagem": "Erro de autenticação",
            "detalhe" : "Não foi encontrada informações de autenticação"
        }
        return make_response(resposta, 401)
    
    if not autenticacao == ("sua chave aqui"):
        resposta = {
            "mensagem": "Erro de autenticação",
            "detalhe": "Erro ao validar o token"
        }
        return make_response(resposta, 401)

    os_info = {
        "system": platform.system(),
        "platform": platform.platform(),
        "version": platform.version(),
        "release": platform.release(),
        "architecture": platform.architecture()[0],
        "architecture2": platform.architecture()[1]
    }
    return make_response(jsonify({
        "os_info": os_info
    }),200)
