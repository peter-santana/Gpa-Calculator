#!/usr/bin/env python
# coding: utf-8

# In[33]:


print("Hola gaddiel me dijo que hiciera esto")

creditos = []
notas = []
clases = []
cantidad_de_semestres = int(input("Cuantos semestres has tomado? "))

def gpaCalculator():
    x = 0
    while x < cantidad_de_semestres:
        idk = int(input("Cuantas clases cogistes en " + str(x+1) + " semestre "))
        ok = 0
        while ok < idk:
            clases.append(str(input("Pon el nombre de la clase que cogiste en " + str(x+1) + " semestre ")))
            notas.append(str(input("Que sacaste? ")))
            creditos.append(int(input("Cuantos creditos eran ? ")))
            ok+=1
        
        x += 1
        
    print("Calculando")
    print(clases)
    print(creditos)
    print(notas)
    totalcreditos = []
    j = 0
    for i in creditos:
        if notas[j] == "A" or notas[j] == "a":
            totalcreditos.append(i * 4)
            j+=1
        elif notas[j] == "B" or notas[j] == "b":
            totalcreditos.append(i * 3)
            j+=1
        elif notas[j] == "C" or notas[j] == "c":
            totalcreditos.append(i * 2)
            j+=1
        elif notas[j] == "D" or notas[j] == "d":
            totalcreditos.append(i * 1)
            j+=1
        else:
            totalcreditos.append(0)
            j+=1
            
    print(sum(totalcreditos) / sum(creditos))
gpaCalculator()                      
        
       


# In[ ]:




