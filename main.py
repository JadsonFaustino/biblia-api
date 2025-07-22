from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json
import os
import uvicorn
from loguru import logger
import traceback

app = FastAPI()

BIBLE_PATH = './biblia/ave-maria-refactor.json'

def handle_error(e):
    logger.error(f"{e} (line {traceback.extract_stack()[-2].lineno})")
    raise HTTPException(
        status_code=e.status_code if hasattr(e, 'status_code') else 500,
        detail=str(e.detail if hasattr(e, 'detail') else str(e))
    )


@app.get('/health')
def health_check():
    """
    Health check endpoint to verify if the service is running.
    """
    return JSONResponse(
        content={
            "mensagem": "Serviço rodando"
        },
        status_code=200
    )


@app.get('/livros')
def list_books(
):
    """
    Endpoint to list all books in the Bible.
    """
    try:
        with open(BIBLE_PATH, 'r') as file:
            bible_json = json.load(file)
        return JSONResponse(
            content={
                "livros": [
                    {
                        'nome': book['nome'], 
                        'abrev': book['abreviacao'],
                        'qtd_capitulos': book['quantidade_capitulos'],
                        'testamento': book['testamento']
                    } 
                    for book in bible_json.values()
                ],
                "qtd_livros": len([b for b in bible_json.values()]),
            },
            status_code=200
        )
    except Exception as e:
        handle_error(e)


@app.get('/livro/{book}')
def get_book(book: str | int):
    """
    Endpoint to get details of a specific book in the Bible and its verses.
    """
    try:
        index_mode = book.isdigit()
        abbr_mode = not index_mode and len(book) <= 3
        response = None
        with open(BIBLE_PATH, 'r') as file:
            bible_json = json.load(file)

        if (abbr_mode):
            partial_response = [b for b in bible_json.values() if b['abreviacao'].lower() == book.lower()]
            if len(partial_response) > 0:
                response = partial_response[0]
        
        if (index_mode and int(book) > 0 and int(book) <= len(bible_json.keys())):
            response = [b for b in bible_json.values()][int(book) - 1]

        if (not abbr_mode and not index_mode):
            partial_response = [i for i in filter(lambda b: b['nome'].lower() == book.lower(), bible_json.values())]
            if len(partial_response) > 0:
                response = partial_response[0]

        if response:
            return JSONResponse(
                content=response,
                status_code=200
            )
        else:
            raise HTTPException(
                status_code=404,
                detail='Livro não encontrado'
            )

    except Exception as e:
        handle_error(e)


@app.get('/livro/{book}/capitulo/{chapter}')
def get_chapter(book: str | int, chapter: str | int):
    """
    Endpoint to get a specific chapter of a book in the Bible and its details.
    """
    try:
        if not chapter.isdigit() or int(chapter) < 1:
            raise HTTPException(
                status_code=400,
                detail='Capítulo inválido'
            )

        index_mode = book.isdigit()
        abbr_mode = not index_mode and len(book) <= 3
        book_response = None
        with open(BIBLE_PATH, 'r') as file:
            bible_json = json.load(file)

        if (abbr_mode):
            partial_book_response = [b for b in bible_json.values() if b['abreviacao'].lower() == book.lower()]
            if len(partial_book_response) > 0:
                book_response = partial_book_response[0]
        
        if (index_mode and int(book) > 0 and int(book) <= len(bible_json.keys())):
            book_response = [b for b in bible_json.values()][int(book) - 1]

        if (not abbr_mode and not index_mode):
            partial_book_response = [i for i in filter(lambda b: b['nome'].lower() == book.lower(), bible_json.values())]
            if len(partial_book_response) > 0:
                book_response = partial_book_response[0]

        if not book_response:
            raise HTTPException(
                status_code=404,
                detail='Livro não encontrado'
            )
        
        if int(chapter) > len(book_response['capitulos']):
            raise HTTPException(
                status_code=404,
                detail='Capítulo não encontrado'
            )
        chapter_response = book_response['capitulos'][int(chapter) - 1]
        return JSONResponse(
            content=chapter_response,
            status_code=200
        )

    except Exception as e:
        handle_error(e)


@app.get('/livro/{book}/capitulo/{chapter}/versiculo/{verse}')
def get_verse(book: str | int, chapter: str | int, verse: str | int):
    """
    Endpoint to get a specific verse of a book in the Bible and its details.
    """
    try:
        if not chapter.isdigit() or int(chapter) < 1:
            raise HTTPException(
                status_code=400,
                detail='Capítulo inválido'
            )
        
        if not verse.isdigit() or int(verse) < 1:
            raise HTTPException(
                status_code=400,
                detail='Versículo inválido'
            )

        index_mode = book.isdigit()
        abbr_mode = not index_mode and len(book) <= 3
        book_response = None
        with open(BIBLE_PATH, 'r') as file:
            bible_json = json.load(file)

        if (abbr_mode):
            partial_book_response = [b for b in bible_json.values() if b['abreviacao'].lower() == book.lower()]
            if len(partial_book_response) > 0:
                book_response = partial_book_response[0]
        
        if (index_mode and int(book) > 0 and int(book) <= len(bible_json.keys())):
            book_response = [b for b in bible_json.values()][int(book) - 1]

        if (not abbr_mode and not index_mode):
            partial_book_response = [i for i in filter(lambda b: b['nome'].lower() == book.lower(), bible_json.values())]
            if len(partial_book_response) > 0:
                book_response = partial_book_response[0]

        if not book_response:
            raise HTTPException(
                status_code=404,
                detail='Livro não encontrado'
            )
        
        if int(chapter) > len(book_response['capitulos']):
            raise HTTPException(
                status_code=404,
                detail='Capítulo não encontrado'
            )
        chapter_response = book_response['capitulos'][int(chapter) - 1]

        if int(verse) > len(chapter_response['versiculos']):
            raise HTTPException(
                status_code=404,
                detail='Versículo não encontrado'
            )
        verse_response = chapter_response['versiculos'][int(verse) - 1]

        return JSONResponse(
            content=verse_response,
            status_code=200
        )

    except Exception as e:
        handle_error(e)


# run app
if __name__ == '__main__':
    if not os.path.exists(BIBLE_PATH):
        print(f"Bible file not found at {BIBLE_PATH}. Please check the path.")
    else:
        uvicorn.run(app, host="localhost", port=8000)
        print("Starting FastAPI server...")