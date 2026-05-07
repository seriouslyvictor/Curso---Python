frutas = ["banana", "maçã", "pêra"]

livro1 = {"titulo": "1984", "autor": "George Orwell"}
livro2 = {"titulo": "Bom demais para ser ignorado", "autor": "Cal Newport"}
livro3 = {"titulo": "48 Laws of power", "autor": "Robert Greene"}
livro4 = {"titulo": "AI engineering"}
livro5 = {"titulo": "AI engineering", "autor": "Chip Huyen"}

livros = [livro1, livro2, livro3, livro4, livro5]

frutas_berradas = [fruta.upper()  for fruta in frutas]
print(frutas_berradas)

frutas_mapeadas = {fruta: fruta.upper()  for fruta in frutas}
print(frutas_mapeadas)

frutas_grandes = [fruta.capitalize() for fruta in frutas if len(fruta) >=5]
print(frutas_grandes)

frutas_com_p = [fruta for fruta in frutas if fruta.startswith("p")]
print(frutas_com_p)

titulos_livros = [livro.get("titulo")  for livro in livros]
print(titulos_livros)

autores_livros = [livro.get('autor') for livro in livros if livro.get('autor') != None]
print(autores_livros)

#Remove duplicados.
titulos_livros_set = {livro.get('titulo') for livro in livros if livro.get('titulo')}
print(titulos_livros_set)