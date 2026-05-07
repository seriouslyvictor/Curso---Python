frutas = ["banana", "maçã", "pêra"]

livro1 = {"titulo": "1984", "autor": "George Orwell"}
livro2 = {"titulo": "Bom demais para ser ignorado", "autor": "Cal Newport"}
livro3 = {"titulo": "48 Laws of power", "autor": "Robert Greene"}
livro4 = {"titulo": "AI engineering"}
livro5 = {"titulo": "AI engineering", "autor": "Chip Huyen"}

livros = [livro1, livro2, livro3, livro4, livro5]
import time

def come_up_with_fruit_names():
    for fruta in frutas:
        time.sleep(1) # thinking of a fruit
        yield fruta

#Não dá para simplesmente printar os elementos, precisamos pegar os "pedaços", também conhecido como Chunks
for chunk in come_up_with_fruit_names():
    print(chunk)

def gerador_autores():
    yield from [livro.get("autor") for livro in livros if livro.get("autor")]


for chunk in gerador_autores():
    print(chunk)