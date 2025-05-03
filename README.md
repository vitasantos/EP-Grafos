**EP1 – Algoritmos em Grafos 2024.3 – UFABC**

✨ **Descrição**

Este projeto implementa uma solução para o Exercício Programa 1 (EP1) da disciplina Algoritmos em Grafos (prof. Aritanan Gruber – 2024.3), na Universidade Federal do ABC. O problema modela um cenário logístico onde produtos perecíveis precisam ser entregues de um ponto a outro dentro de um tempo limite, percorrendo o menor caminho em distância possível, respeitando as restrições de tempo e a natureza direcional das estradas.

🧩 **Objetivo**

Dado um grafo direcionado onde as arestas representam estradas com pesos de distância e tempo, e múltiplas entregas a serem analisadas, o algoritmo determina:

- Se é possível entregar a mercadoria dentro do tempo limite imposto.

- Se for possível, retorna o menor caminho em quilômetros e o tempo total gasto.

- Se não, imprime "Impossivel".

🛠️ **Implementação**

A solução utiliza programação dinâmica inspirada no algoritmo de Bellman-Ford, adaptado para otimizar a distância com uma restrição de tempo.

Técnicas utilizadas:
-Representação de grafos com listas de adjacência.

- Programação dinâmica com estado [v][t], onde v é o vértice e t o tempo acumulado.

- Priorização de caminhos com menor distância e, em caso de empate, menor tempo.

- Análise de complexidade incluída nos comentários do código.
