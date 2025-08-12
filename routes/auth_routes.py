from fastapi import APIRouter 

auth_router = APIRouter(prefix="/auth", tags=["autenticacao"]) # Definir caminho de autenticação do roteador de um determinado endpoint/prefixos - Definição da tag (título na documentação do FastAPI)

@auth_router.get("/") # Definição do caminho e requisição
async def autenticacao():
    """
    Rota padrão de autenticação do sistema. 
    """
    # Inserção da lógica da função
    return {"mensagem": "você acessou a rota de autenticacao", "autenticacao": False}