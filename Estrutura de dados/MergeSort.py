def merge_lists(left_sublist, right_sublist):
    i, j = 0, 0
    result = []
    # iterate através da sublista esquerda e direita
    while i < len(left_sublist) and j < len(right_sublist):
        # if valor esquerdo é menor do que a direita, em seguida, apê-lo para o resultado
        if left_sublist[i] <= right_sublist[j]:
            result.append(left_sublist[i])
            i += 1
        else:
            # if valor direito é menor do que a esquerda, em seguida, apê-lo para o resultado
            result.append(right_sublist[j])
            j += 1
    # concatenate o resto dos sublistas esquerdo e direito
    result += left_sublist[i:]
    result += right_sublist[j:]
    # return o resultado
    return result


def merge_sort(input_list):
    # if lista contém apenas 1 elemento devolvê-lo
    if len(input_list) <= 1:
        return input_list
    else:
        # split as listas em dois suballists e sublistas recursivamente divididos
        midpoint = int(len(input_list) / 2)
        left_sublist = merge_sort(input_list[:midpoint])
        right_sublist = merge_sort(input_list[midpoint:])
        # return a lista mesclada usando a função merge_list acima
        return merge_lists(left_sublist, right_sublist)


# test corrido
number_list = [3, 1, 5, 3, 2, 5, 8, 2, 9, 6, 12, 53, 75, 22, 83, 123, 12123]
teste = merge_sort(number_list)
print(teste)