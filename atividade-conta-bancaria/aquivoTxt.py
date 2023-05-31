with open("comprovanteBancario.txt", "r", encoding="utf-8") as arquivoBancario:
    email = arquivoBancario.readlines()
    print(email)