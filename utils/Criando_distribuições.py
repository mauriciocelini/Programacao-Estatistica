def gerar_num_01(n_potencias):
    num_bin = np.random.choice(a=(0,1), size=n_potencias)
    binarizacao = (1/2)**np.arrange(1,n_potencias+1)
    vetor_ultimo = num_bin*binarizacao
    soma = np.sum(vetor_ultimo)
    return soma


def amostra_bernoulli(lista, prob_sucesso, tam):
    for i in range(n)        
        U = np.random.uniform()
        if U > prob_sucesso:
            lista.append(0)
        else:
            lista.append(1)
    return lista