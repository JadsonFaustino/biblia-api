import json

JSON_PATH = 'biblia/ave-maria.json'
BOOKS_ABBREVIATIONS = {
    # Pentateuco
    "Gênesis": "Gn",
    "Êxodo": "Ex",
    "Levítico": "Lv",
    "Números": "Nm",
    "Deuteronômio": "Dt",

    # Históricos
    "Josué": "Js",
    "Juízes": "Jz",
    "Rute": "Rt",
    "1 Samuel": "1Sm",
    "2 Samuel": "2Sm",
    "1 Reis": "1Rs",
    "2 Reis": "2Rs",
    "1 Crônicas": "1Cr",
    "2 Crônicas": "2Cr",
    "Esdras": "Ed",
    "Neemias": "Ne",
    "Tobias": "Tb",
    "Judite": "Jt",
    "Ester": "Et",
    "1 Macabeus": "1Mc",
    "2 Macabeus": "2Mc",

    # Sapienciais
    "Jó": "Jó",
    "Salmos": "Sl",
    "Provérbios": "Pv",
    "Eclesiastes": "Ec",
    "Cântico dos Cânticos": "Ct",
    "Sabedoria": "Sb",
    "Eclesiástico": "Eclo",

    # Proféticos
    "Isaías": "Is",
    "Jeremias": "Jr",
    "Lamentações": "Lm",
    "Baruc": "Br",
    "Ezequiel": "Ez",
    "Daniel": "Dn",
    "Oséias": "Os",
    "Joel": "Jl",
    "Amós": "Am",
    "Abdias": "Ab",
    "Jonas": "Jn",
    "Miquéias": "Mq",
    "Naum": "Na",
    "Habacuc": "Hab",
    "Sofonias": "Sf",
    "Ageu": "Ag",
    "Zacarias": "Zc",
    "Malaquias": "Ml",

    # Novo Testamento
    "Mateus": "Mt",
    "Marcos": "Mc",
    "Lucas": "Lc",
    "João": "Jo",
    "Atos dos Apóstolos": "At",
    "Romanos": "Rm",
    "1 Coríntios": "1Co",
    "2 Coríntios": "2Co",
    "Gálatas": "Gl",
    "Efésios": "Ef",
    "Filipenses": "Fp",
    "Colossenses": "Cl",
    "1 Tessalonicenses": "1Ts",
    "2 Tessalonicenses": "2Ts",
    "1 Timóteo": "1Tm",
    "2 Timóteo": "2Tm",
    "Tito": "Tt",
    "Filêmon": "Fm",
    "Hebreus": "Hb",
    "Tiago": "Tg",
    "1 Pedro": "1Pe",
    "2 Pedro": "2Pe",
    "1 João": "1Jo",
    "2 João": "2Jo",
    "3 João": "3Jo",
    "Judas": "Jd",
    "Apocalipse": "Ap"
}

def load_json(file_path):
    return json.load(open(file_path, 'r', encoding='utf-8'))

if __name__ == "__main__":
    bible_json = load_json(JSON_PATH)
    new_bible_json = {}

    for testament in ['antigo', 'novo']:
        for book in bible_json[f'{testament}Testamento']:
            book_name = book['nome']
            book_chapters = [{**chap, 'quantidade_versiculos': len(chap['versiculos'])} for chap in book['capitulos']]
            book_obj = {
                'nome': book_name,
                'abreviacao': BOOKS_ABBREVIATIONS[book_name],
                'quantidade_capitulos': len(book_chapters),
                'capitulos': book_chapters,
                'testamento': testament
            }
            new_bible_json[BOOKS_ABBREVIATIONS[book_name]] = book_obj
    
    # Save new json
    with open('biblia/ave-maria-refactor.json', 'w', encoding='utf-8') as f:
        json.dump(new_bible_json, f, ensure_ascii=False, indent=2)