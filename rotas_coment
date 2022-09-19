def regras_dados_usuario(dado):
    def apply(x):
        x["nome"] = dado 
        return x
    mapa = map(apply, db.db_usuarios)
    return print(list(mapa))

def regras_dados_usuario(dado):
    dado_procurado = None

    def apply(x):
        if x["id"] == dado:
            dado_procurado = x
            return dado_procurado
        else:
            pass
            return

    mapa = map(apply, db.db_usuarios)
    return print(list(mapa))

import db

'''def regras_nome_usuario(dado_nome):
    for i in db.db_usuarios:
        print(db.db_usuarios[i]["nome"])
        print(dado_nome)
        if db.db_usuarios[i]["nome"] == "nome":
            pesquisa_nome = db.persistencia_usuario_pesquisar_nome(db.db_usuarios[i])
            return pesquisa_nome

    return 'FALHA' '''

def regras_nome_usuario(dado_nome):
    for i in db.db_usuarios:
        if db.db_usuarios[i]["nome"] == "nome":
            pesquisa_nome = db.persistencia_usuario_pesquisar_nome(db.db_usuarios[i])
            return pesquisa_nome

        #return "FALHA"

regras_nome_usuario("nome")

def regras_id_usuario(dado_id):
    print(db.db_usuarios)
    print(dado_id)
    for i in db.db_usuarios:
        if dado_id in db.db_usuarios:
            print("oi")   
            return pesquisa_id

    return "FALHA"

dict = {123[{"rua": "rua x", "cep": "03245", "cidade": "Sao Paulo", "estado": "SP"}, {"rua": "rua y", "cep": "12345", "cidade": "Santo André", "estado": "SP"}]}
import json
w = json.dumps(dict)
print(w)