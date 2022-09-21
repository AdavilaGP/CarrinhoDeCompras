#Regras do negócio da API
from email_validator import validate_email, EmailNotValidError
import db


OK = "OK"
FALHA = "FALHA"


def regras_usuario_cadastrar(usuario):
    print(db.db_usuarios)
    if usuario["id"] in db.db_usuarios:
        return FALHA

    eh_nova_conta = True
    try:
        validation = validate_email(usuario["email"], check_deliverability=eh_nova_conta)
        usuario["email"] = validation.email

    except EmailNotValidError as e:
        print(str(e))

    tamanho_permitido = 3
    if tamanho_permitido > len(usuario["senha"]):
        print("senha não é válida. Tamanho menor que o esperado")

    else:
        usuario = db.persistencia_usuario_salvar(usuario)

    print(db.db_usuarios)

    return OK
 #TODO ou deixar tudo try/except, ou if/else


def regras_id_usuario(dado_id):
    if dado_id in db.db_usuarios:
        pesquisa_id = db.persistencia_usuario_pesquisar_id(dado_id)   
        return pesquisa_id

    return FALHA


def regras_nome_usuario(dado_nome):
    pesquisa_nome_recebido = []
    dado_nome = dado_nome.strip(' " " ')

    for i in db.db_usuarios:
        if db.db_usuarios[i]["nome"] == dado_nome:
            #pesquisa_nome = db.persistencia_usuario_pesquisar_nome(db.db_usuarios[i])
            pesquisa_nome_recebido.append(db.db_usuarios[i])

    if pesquisa_nome_recebido == []:
        return FALHA
    else:
        return pesquisa_nome_recebido


def regras_id_usuario_delete(dado_id):
    if dado_id in db.db_usuarios:
        pesquisa_id = db.persistencia_usuario_excluir_id(dado_id)   
        return OK

    return FALHA


def regras_endereco_usuario(dado_id):
    lista_endereços_id = []
    if dado_id in db.db_usuarios:
        lista_endereços_id = db.persistencia_lista_enderecos_id_user(dado_id)
        return lista_endereços_id

    if lista_endereços_id == []:
        return FALHA
    else:
        return lista_endereços_id


def regras_email_database(dominio):
    lista_email_mesmo_dominio = []

    lista_email_mesmo_dominio = db.persistencia_lista_email_database(dominio)
    if lista_email_mesmo_dominio ==[]:
        
        return FALHA
    else:
        return lista_email_mesmo_dominio


def regras_cria_endereco_usuario(endereco, id_usuario):
    if id_usuario not in db.db_usuarios:
        return FALHA

    cria_endereco = db.persistencia_cria_endereco_id_user(endereco, id_usuario)

    return OK


def regras_id_endereco_delete(dado_endereco):
    if dado_endereco in db.db_enderecos:
        pesquisa_end = db.persistencia_endereco_excluir_id(dado_endereco)   
        return OK

    return FALHA


def regras_cria_produto(produto):
    if produto["id"] in db.db_produtos:

        return FALHA
    else:
        produto = db.persistencia_cria_produto(produto)
    
        return OK


def regras_produto_apaga(dado_produto):
    if dado_produto in db.db_produtos:
        pesquisa_produto = db.persistencia_produto_excluir_id(dado_produto)   
        return OK

    return FALHA


def retornar_produto_cadastrado(id_produto):
    if id_produto in db.db_produtos:

        return db.db_produtos[id_produto]
    else:

        return FALHA


def regras_cria_carrinho(id_usuario, id_produto, carrinho):
    produto = retornar_produto_cadastrado(id_produto)
    print(carrinho)
    print(produto)
    if id_usuario not in db.db_usuarios or id_produto not in db.db_produtos:

        return FALHA
    elif id_usuario not in db.db_carrinhos:
        carrinho = db.persistencia_cria_carrinho(id_usuario, id_produto, carrinho)

        return OK
    else:
        carrinho = db.persistencia_adiciona_ao_carrinho(produto, id_usuario, id_produto)
        
        return OK


def regras_retornar_carrinho(dado_usuario):
    if dado_usuario in db.db_carrinhos:
        carrinho_usuario = db.persistencia_busca_carrinho(dado_usuario)
        print("carrinho_user", carrinho_usuario)
        return carrinho_usuario
    else:

        return FALHA


def regras_itens_valor_total(dado_id):
    if dado_id in db. db_carrinhos:
        lista_item_valor_total = db.persistencia_item_valor(dado_id)
        
        return lista_item_valor_total
    else:
        return FALHA


def regras_deleta_carrinho(id_usuario):
    if id_usuario in db.db_carrinhos:
        deleta_carrinho = db.persistencia_deleta_carrinho(id_usuario)
        
        return OK
    else:
        
        return FALHA