from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from models import Princesa
from typing import Optional, Any
from time import sleep

app = FastAPI(title="Princesas")

def banco_princesas():
    try: 
        print("Abrindo Banco de dados")
        sleep(1)
    finally:
        print("Fechando Banco de dados")
        sleep(1)

princesas = {
    1: {
        'nome': 'Branca de Neve',
        'idade': 14,
        'filme': 'Branca de Neve e os Sete Anões'
    },
    2: {
        'nome': 'Cinderela',
        'idade': 19,
        'filme': 'Cinderela'
    },
    3: {
        'nome': 'Aurora',
        'idade': 16,
        'filme': 'A Bela Adormecida'
    },
    4: {
        'nome': 'Ariel',
        'idade': 16,
        'filme': 'A Pequena Sereia'
    },
    5: {
        'nome': 'Bela',
        'idade': 17,
        'filme': 'A Bela e a Fera'
    },
    6: {
        'nome': 'Jasmine',
        'idade': 16,
        'filme': 'Aladdin'
    },
    7: {
        'nome': 'Pocahontas',
        'idade': 18,
        'filme': 'Pocahontas'
    },
    8: {
        'nome': 'Fa Mulan',
        'idade': 16,
        'filme': 'Mulan'
    },
    9: {
        'nome': 'Tiana',
        'idade': 19,
        'filme': 'A Princesa e o Sapo'
    },
    10: {
        'nome': 'Rapunzel',
        'idade': 18,
        'filme': 'Enrolados'
    },
    11: {
        'nome': 'Merida',
        'idade': 16,
        'filme': 'Valente'
    },
    12: {
        'nome': 'Moana',
        'idade': 16,
        'filme': 'Moana'
    }
}

#teste inicial
@app.get("/")
async def mensagem():
    return "Todas as Princesas deram certo!"

#lista de princesas
@app.get("/todas_princesas")
async def get_princesas(db: Any = Depends(banco_princesas)):
    return princesas

#buscar princesa pelo ID
@app.get("/princesas/{id_princesa}")
async def princesa(id_princesa: int):
    if id_princesa in princesas:
        return princesas[id_princesa]
    else:
        return {"Erro": "Esse ID não corresponde a nenhuma princesa!"}

#adicionar princesa
@app.post("/princesa")
async def add_princesa(princesa: Optional [Princesa] = None):
    if princesa.id not in princesas:
        next_id = len(princesas) + 1
        princesas[next_id] = princesa
        del princesa.id
        return princesa
    else:
        return {"Erro": "Já existe uma princesa com esse ID!"}
    
#atualizar princesa
@app.put("/princesa/{id_princesa}")
async def put_princesa(id_princesa: int, princesa: Princesa):
    if id_princesa in princesas:
        princesas[id_princesa] = princesa
        princesa.id = id_princesa
        return princesa
    else:
        return {"Erro": "Não existe uma princesa com esse ID!"}

#deletar princesa
@app.delete("/princesa/{id_princesa}")
async def del_princesa(id_princesa: int, princesa: Princesa):
    if id_princesa in princesas:
        del princesas[id_princesa]
        return {"Erro": "Delete a princesa {id_princesa}"}
    else:
        return {"Erro": "Não existe essa princesa!"}
    


#metodo patch

#Fazer com que seus colegas acessem sua API


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)