def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
nome = ['f','l','a','m','e','n','g','o']
letra = 'g'
print(f'letra que esta sendo procurada {letra.upper()}')
print(f'O Elemento encontrado no indice {linearsearch(nome,letra)}')
