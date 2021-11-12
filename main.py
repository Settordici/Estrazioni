import urllib3

def getList(min, max):
    http = urllib3.PoolManager()
    arguments = f"https://www.random.org/sequences/?min="+str(min)+"&max="+str(max)+"&col=1&format=plain&rnd=new"
    r = http.request('GET', arguments)
    out = r.data.decode()
    out = out.split("\n")
    for x in range(len(out) - 1):
        out[x] = int(out[x])
    return out

def convert_list(lista):
    lista = lista[:len(lista)-1]
    print(lista)
    file = open("lista.txt", "r")
    out = file.readlines()
    for x in lista:
        for i in out:
            i = i.split(".")
            if i[0] != "" and i[0] != "*":
                if int(i[0]) == x:
                    print(i[1], end= "")

lista = getList(1, 23)
convert_list(lista)
