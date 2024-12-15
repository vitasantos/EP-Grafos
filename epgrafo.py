#Feito por Vitória Cordeiro dos Santos RA:11202130706

import math
inf = math.inf
def Matrizes(M,n): #recebe a matriz M com as entradas, e n, que é o número de vértices do digrafo
  T = [[inf for _ in range(n)]  for _ in range(n)] #inicializa uma matriz de infinitos T
  for i in range(len(M)):
      T[M[i][0]-1][M[i][1]-1] = M[i][3] #Preenche a matriz T com o tempo entre v1 e v2 para todo v do digrafo existente em M

  KM = [[inf for _ in range(n)]  for _ in range(n)] #inicializa uma matriz de infinitos KM
  for i in range(len(M)):
      KM[M[i][0]-1][M[i][1]-1] = M[i][2] #Preenche a matriz KM com a distancia entre v1 e v2 para todo v do digrafo existente em M

  return T, KM
  
def BellmanFord(T,KM,s,n,max): #função recebe a matriz T, a matriz KM, o vértice de partida s , número de vértices n e o tempo máximo permitido max
 time = [inf for _ in range(n)] #inicializa a lista vazia de tempo entre s e os outros vértices
 time[s] = 0 #define o tempo de s até s como 0
 km = [inf for _ in range(n)] #inicializa a lista vazia de tempo entre s e os outros vértices
 km[s] = 0 #define a distância de s até s como 0

 for _ in range(1,n-1):
    for u in range(n):
      for v in range(n):
        if time[v] > time[u] + T[u][v]: #verifica se o tempo atual entre s e v é maior do que o tempo entre s a u mais u a v ( min{time[v],time[u]+T(u,v)})
         time[v] = time[u] + T[u][v] #atualiza o time[v]
         km[v] = km[u] + KM[u][v] #atualiza o km[v]

 for _ in range(1,n-1):
    for u in range(n):
       for v in range(n):
         if km[v] > km[u] + KM[u][v] and time[u] + T[u][v]<= max: #agora verifica se há outro caminho entre s e v com uma distância menor porém com o tempo dentro do limite máximo.
             time[v] = time[u] + T[u][v] #atualiza o time[v]
             km[v] = km[u] + KM[u][v] #atualiza o km[v]

 return time, km #retorna as listas time e km

n,m = map(int, input().split()) #recebe as entradas n e m
i = 1
while n!=0:
  M = [list(map(int, input().split())) for i in range(m)] #Matriz com os dados das entradas (v1,v2,disntacia,tempo)

  T,KM = Matrizes(M,n) #Função retorna 2 matrizes: a matriz T que contem o tempo entre cada vértice do digrafo, e a matriz KM que contem a distancia entre cada vértice

  k = int(input())

  E = [list(map(int, input().split())) for i in range(k)] #recebe as entradas v1,v2 e tempo máximo entre eles (v1,v2,max)
  
  
  print("Instancia ",i)
  for linha in E:
    time,km = BellmanFord(T,KM,linha[0]-1,n,linha[2]) #chama a função BellmanFord, partindo do ponto v1=linha[0]-1 (pois os indices da matriz começam do 0 invés do 1) e com o limite maximo de tempo = linha[2] 

    if time[linha[1]-1] <= linha[2]: #verifica se o tempo até v2=linha[1]-1 é menor ou igual ao tempo maximo=linha[2]
      print("Possivel -", km[linha[1]-1], "km,",time[linha[1]-1],"min" ) #imprime a quilometragem e o tempo do percurso
    else:
      print("Impossivel")
  print()
  i+=1
  n,m = map(int, input().split())

#tempo: O(n³)