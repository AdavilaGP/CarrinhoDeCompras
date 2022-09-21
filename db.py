#Database provisória até a integração com o Banco de Dados acontecer

# Criar a class Database(). Como chamar as funções da classe em Regras_de_uso?
    
db_usuarios = {} #[]
db_produtos = {}
db_enderecos = {}#{123: {"rua": "rua x", "cep": "03245", "cidade": "Sao Paulo", "estado": "SP"},123: {"rua": "rua y", "cep": "13245", "cidade": "Santa Catarina", "estado": "SC"}, 124: {"rua": "rua z", "cep": "23245", "cidade": "Santa Catarina", "estado": "SC"}}  #Não funciona com mais de um endereço..
db_carrinhos = {}

def persistencia_usuario_salvar(novo_user):
    #db_usuarios.append(novo_user)
    db_usuarios[novo_user["id"]] = novo_user

    return

def persistencia_usuario_pesquisar_id(dado_id):
    pesquisa_usuario = db_usuarios[dado_id]
    print("Pesquisa usuario", pesquisa_usuario)

    return pesquisa_usuario

#def persistencia_usuario_pesquisar_nome(dado_nome):
#    pesquisa_usuario = dado_nome
#    print("Pesquisa usuario", pesquisa_usuario)

#    return pesquisa_usuario

def persistencia_usuario_excluir_id(dado_id):
    db_usuarios.pop(dado_id, None)
    db_enderecos.pop(dado_id, None)
    db_carrinhos.pop(dado_id,None)

    return 

def persistencia_lista_enderecos_id_user(dado_id):
    lista_endereço = []
    for w, i in enumerate(db_enderecos):
        print("w", w, "i", i, "dado_id", dado_id, "Types", type(i), type(dado_id))
        if i == dado_id:
            lista_endereço.append(db_enderecos[i]["rua"])
            lista_endereço.append(db_enderecos[i]["cep"])
            lista_endereço.append(db_enderecos[i]["cidade"])
            lista_endereço.append(db_enderecos[i]["estado"]) 

    return lista_endereço
#TODO Arrumar "retornar uma lista de todos os endereços vinculados ao usuário". Uma mesma chave aponta para o mesmo objeto.
#O looping reescreve o valor da variável.

def persistencia_lista_email_database(dominio):
    lista_dominio = []
    for i in db_usuarios:
        for j, w in enumerate(db_usuarios[i]):
            print(db_usuarios[i])
            print(w)
            if w == "email":
                if  dominio in db_usuarios[i][w]:
                    lista_dominio.append(db_usuarios[i][w])
    print(lista_dominio)
    return lista_dominio


def persistencia_cria_endereco_id_user(endereco, id_usuario):
    codigo_novo_endereco = id_usuario
    #endereco["id_end"] = codigo_novo_endereco
    db_enderecos[id_usuario] = endereco
    print(db_enderecos)

    return

def persistencia_endereco_excluir_id(dado_endereco):
    db_enderecos.pop(dado_endereco, None)
    return 

def persistencia_cria_produto(novo_produto):
    db_produtos[novo_produto["id"]] = novo_produto
    print("db produto", db_produtos)

    return

def persistencia_produto_excluir_id(dado_produto):
    db_produtos.pop(dado_produto, None)
    print("db", db_produtos)
    return

def persistencia_cria_carrinho(id_user, produto, novo_carrinho):
    db_carrinhos[novo_carrinho["id_usuario"]] = novo_carrinho
    print("db carrinho", db_carrinhos)
    return 

# senão adiciona produto ao carrinho e retornar OK
def persistencia_adiciona_ao_carrinho(dado_produto, id_user, id_produto):
    print(db_carrinhos)
    db_carrinhos[id_user]["id_produtos"] = dado_produto
    print(db_carrinhos[id_user])
    return 

def persistencia_busca_carrinho(dado_usuario):
    carrinho = db_carrinhos[dado_usuario]
    return carrinho

def persistencia_item_valor(dado_id):
    lista_item = []
    lista_valor = []
    for i in db_carrinhos[dado_id]:
        if i == "preco_total":
            lista_item.append(db_carrinhos[dado_id]["preco_total"])
        if i == "quantidade_de_produtos":
            lista_valor.append(db_carrinhos[dado_id]["quantidade_de_produtos"])
    
    lista_item_valor = [sum(lista_item), sum(lista_valor)]
    return lista_item_valor

def persistencia_deleta_carrinho(id_usuario):
    db_carrinhos.pop(id_usuario, None)
    return