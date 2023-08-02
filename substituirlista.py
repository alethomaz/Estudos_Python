sucos = ["caju", "morango", "pecego", "banana","pecego"]

indice = sucos.index("pecego")

while "pecego" in sucos:
    indice = sucos.index("pecego")
    sucos[indice] = "pessego"


print(sucos)


