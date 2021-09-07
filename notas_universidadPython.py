x=2
print(type(x))

title=input("Tell me the title of the book: ")

author=input("Tell me the author of the book: ")

print(title, "was write for ", author)
print(f"{title} was write for {author}") # --> idem que ${} en JS

alto=int(input("Dime el alto del rectángulo...:"))
ancho=int(input("Dime el ancho del rectángulo...:"))
area=alto*ancho
perimetro=(alto+ancho)*2
print(f"el area del rectángulo es de {area} y su perimetro es de {perimetro}")


# -- operador ternario (NO ES RECOMENDABLE)
numero=int(input("Dime un número: "))
print("Mayor a 5") if numero>5 else print("Menor o igual a 5")
