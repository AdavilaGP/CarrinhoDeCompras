from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import regras_de_uso


app = FastAPI()


@app.get("/")
async def bem_vinda():
    site = "Seja bem vinda"
    return site.replace('\n', '')

###################################################################################
# Classes
# Classe representando os dados do usuário
class Usuario(BaseModel): 
    #def __init__(self, id, nome, email, senha):
    id: int
    nome: str
    email: str
    senha: str 

# Classe representando os dados do cliente
class Endereco(BaseModel):
    rua: str
    cep: str
    cidade: str
    estado: str

# Classe representando a lista de endereços de um cliente (Não usei ainda..)
class ListaDeEnderecosDoUsuario(BaseModel):
    usuario: Usuario
    enderecos: List[Endereco] = []

# Classe representando os dados do produto
class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float

# Classe representando o carrinho de compras de um cliente com uma lista de produtos
class CarrinhoDeCompras(BaseModel):
    id_usuario: int
    id_produtos: List[Produto] = ()
    preco_total: float
    quantidade_de_produtos: int

###################################################################################
#ok Criar um usuário,
#ok se tiver outro usuário com o mesmo ID retornar falha, 
#ok se o email não tiver o @ retornar falha, 
#ok senha tem que ser maior ou igual a 3 caracteres, 
#ok senão retornar OK
@app.post("/usuario/")
async def criar_usuario(usuario: Usuario):
    print(usuario.dict())
    novo_user = regras_de_uso.regras_usuario_cadastrar(usuario.dict())

    return novo_user

###################################################################################
# Se o id do usuário existir, retornar os dados do usuário
# senão retornar falha
@app.get("/usuario/{id}")
async def retornar_usuario(id: int):
    dados_usuario = regras_de_uso.regras_id_usuario(id)
        
    return dados_usuario

##################################################################################
# Se existir um usuário com exatamente o mesmo nome, retornar os dados do usuário
# senão retornar falha
@app.get("/usuario/nome/{nome}")
async def retornar_usuario_com_nome(nome: str):
    print(nome)
    mesmo_usuario = regras_de_uso.regras_nome_usuario(nome)
    print(mesmo_usuario)

    return mesmo_usuario

#################################################################################
# Se o id do usuário existir, deletar o usuário e retornar OK
# senão retornar falha
# ao deletar o usuário, deletar também endereços e carrinhos vinculados a ele
@app.delete("/usuario/{id}")
async def deletar_usuario(id: int):
    dados_usuario_apaga = regras_de_uso.regras_id_usuario_delete(id)
        
    return dados_usuario_apaga

#################################################################################
# Se não existir usuário com o id_usuario retornar falha, 
# senão retornar uma lista de todos os endereços vinculados ao usuário
# caso o usuário não possua nenhum endereço vinculado a ele, retornar 
# uma lista vazia
### Estudar sobre Path Params (https://fastapi.tiangolo.com/tutorial/path-params/)
@app.get("/usuario/{id_usuario}/endereços/")
async def retornar_enderecos_do_usuario(id_usuario: int):
    endereço_usuario = regras_de_uso.regras_endereco_usuario(id_usuario)

    return endereço_usuario

#################################################################################
# Retornar todos os emails que possuem o mesmo domínio
# (domínio do email é tudo que vêm depois do @)
# senão retornar falha
@app.get("/usuarios/emails/{dominio}")
async def retornar_emails(dominio: str):
    email_database = regras_de_uso.regras_email_database(dominio)

    return email_database

##################################################################################
# Se não existir usuário com o id_usuario retornar falha, 
# senão cria um endereço, vincula ao usuário e retornar OK
@app.post("/endereco/{id_usuario}")
async def criar_endereco(endereco: Endereco, id_usuario: int):
    cria_endereco_id_usuario = \
        regras_de_uso.regras_cria_endereco_usuario(endereco.dict(), id_usuario)

    return cria_endereco_id_usuario

##################################################################################
# Se não existir endereço com o id_endereco retornar falha, 
# senão deleta endereço correspondente ao id_endereco e retornar OK
# (lembrar de desvincular o endereço ao usuário)
@app.delete("/endereco/{id_endereco}")
async def deletar_endereco(id_endereco: int):
    dados_endereco_apaga = regras_de_uso.regras_id_endereco_delete(id_endereco)

    return dados_endereco_apaga

#################################################################################
# Se tiver outro produto com o mesmo ID retornar falha, 
# senão cria um produto e retornar OK
@app.post("/produto/")
async def criar_produto(produto: Produto):
    cria_produto = regras_de_uso.regras_cria_produto(produto.dict())
    return cria_produto

#################################################################################
# Se não existir produto com o id_produto retornar falha, 
# senão deleta produto correspondente ao id_produto e retornar OK
# (lembrar de desvincular o produto dos carrinhos do usuário) TODO entender vinculação
@app.delete("/produto/{id_produto}/")
async def deletar_produto(id_produto: int):
    dados_produto_apaga = regras_de_uso.regras_produto_apaga(id_produto)

    return dados_produto_apaga

#################################################################################
# Se não existir usuário com o id_usuario ou id_produto retornar falha, 
# se não existir um carrinho vinculado ao usuário, crie o carrinho
# e retornar OK
# senão adiciona produto ao carrinho e retornar OK
@app.post("/carrinho/{id_usuario}/{id_produto}/")
async def adicionar_carrinho(carrinho: CarrinhoDeCompras, id_usuario: int, id_produto: int):
    criar_carrinho = regras_de_uso.regras_cria_carrinho(id_usuario, id_produto, carrinho.dict())
    return criar_carrinho

#################################################################################
# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o carrinho de compras.
@app.get("/carrinho/{id_user}")
async def retornar_carrinho(id_user: int):
    dados_carrinho = regras_de_uso.regras_retornar_carrinho(id_user)
    return dados_carrinho

#################################################################################
# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o o número de itens e o valor total do carrinho de compras.
@app.get("/carrinho/{id_usuario}/checkout")
async def retornar_total_carrinho(id_usuario: int):
    informação_carrinho = regras_de_uso.regras_itens_valor_total(id_usuario)
    if informação_carrinho is list:
        numero_itens = informação_carrinho[0]
        valor_total = informação_carrinho[1]

        return numero_itens, valor_total
    else:
        return informação_carrinho

##################################################################################
# Se não existir usuário(?? Não seria carrinho?) com o id_usuario retornar falha, 
# senão deleta o carrinho correspondente ao id_usuario e retornar OK
@app.delete("/carrinho/{id_usuario}/")
async def deletar_carrinho(id_usuario: int):
    deleta_carrinho_user = regras_de_uso.regras_deleta_carrinho(id_usuario)

    return deleta_carrinho_user