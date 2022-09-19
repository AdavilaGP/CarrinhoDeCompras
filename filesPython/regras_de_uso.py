#Regras do negócio da API
from email_validator import validate_email, EmailNotValidError
import db


OK = "OK"
FALHA = "FALHA"


def regras_usuario_cadastrar(usuario):
    print(db.db_usuarios)
    if usuario["id"] in db.db_usuarios:
        return FALHA

    eh_nova_conta = True # False for login pages
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

# Se não existir usuário com o id_usuario ou id_produto retornar falha, 
# se não existir um carrinho vinculado ao usuário, crie o carrinho
# e retornar OK
# senão adiciona produto ao carrinho e retornar OK
def regras_cria_carrinho(carrinho):
    print(carrinho)
    id_usuario = carrinho["id_usuario"]
    id_produtos_geral = carrinho["id_produtos"]
    id_produto = id_produtos_geral[0]
    preco_total = carrinho["preco_total"]
    quantidade_de_produtos = carrinho["quantidade_de_produtos"]

    print(id_produto)
    if id_usuario not in db.db_usuarios and id_produto not in db.db_produtos:

        return FALHA
    if id_usuario not in db.db_usuarios:
        carrinho = db.persistencia_cria_carrinho(carrinho)
        return OK
    else:
        carrinho = db.persistencia_adiciona_ao_carrinho(id_produto)
        return OK