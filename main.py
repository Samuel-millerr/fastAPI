""" Aqui se localiza o arquivo final do FastAPI onde o ocorre sua inicialização e configuração final, os pontos importantes e necessários para esse arquivo são:
- Importações do settings e router já definidos
- Instancia da api atráves da variável app recebendo classe 'FastAPI'
- Opcional: Metódo simples para retornar uma mensagem que a api está funcional
- Definição do origin e do middleware para evitar problemas futuros principalmente com o frontend
- Incluir a rota importada da pasta api
- Lógica simples para permitir o gerenciamento da inicialização da api
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from api.v1.api import api_router

app = FastAPI(title="Escola API com Banco")

@app.get("/", tags=["API"])
async def start_api():
    return {"message": "Bem vindo a api de escola, aqui você encontra disponibilidade de informações relacionadas a aulas, turmas, alunos e professores."}

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5500",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001, log_level="info", reload=True)