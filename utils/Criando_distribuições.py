impor numpy as np

def amostra_bernoulli(prob_sucesso, tam):
    '''
    Código que gera uma amostra de bernoullis
        prob_sucesso - probabilidade de sucesso da bernoulli
        tam - tamanho desejado da amostra
     ''' 
    lista = []
    for _ in range(n)
        U = np.random.uniform()
        if U > prob_sucesso:
            lista.append(0)
        else:
            lista.append(1)
    return lista

def amostra_bionimal(n, p, N):
    '''
    Código que gera uma amostra de binomiais
        n - número de lançamentos de cada binomial
        p - probabilidade de sucesso das binomiais
        N - tamanho da amostra de binomiais
    '''
    lista = []
    for i in range(N):
        U = np.random.uniform(size=n)
        binomial = np.sum(U<p)
        lista.append(binomial)
    return lista

def amostra_geometrica(p, N):
    '''
    Código que gera uma amostra de geométricas
        p - probabilidade de sucesso das geométricas
        N - tamanho da amostra de geométricas
    '''
    lista = []
    for i in range(N):
        u = np.random.uniform
        x = np.floor(np.log(u)/np.log(1-p)) + 1
        lista.append(x)
    return lista

def amostra_poisson(lbd, N):
    '''
    Código que gera uma amostra de poisson
    lbd - parâmetro do número médio de ocorrências
    N - tamanho da amostra
    '''
    lista = []
    for _ in range(N):
        u = np.random.uniform()
        i = 0
        p = np.exp(-lbd)
        F = p
        while u > F:
            i += 1
            p *= lbd/i
            F += p
        lista.append(i)
    return lista


def normalizar_amostra(amostra, n, mi, sigma2):
    '''
    Código que normaliza as amostras e as deixa com distribuição N(0,1)
        amostra - lista da amostra que se deseja normalizar
        n - tamanho da amostra
        mi - média (teórica) da distribuição amostrada
        sigma2 - variância (teórica) da distribuição amostrada
    '''
    normal = np.sqrt(n)*(np.mean(amostra,axis=1)-mi)/np.sqrt(sigma2)
    return normal


def amostra_binomial_negativa(r, p, N):
    '''
    Código que gera uma amostra de binomiais negativas
        r - número de sucessos desejados
        p - probabilidade do sucesso
        N - tamanho da amostra desejada
    '''
    lista = []
    for _ in range(N)
    geometricas = []
    soma = 0
    for _ in range(r):
        U = np.random.uniform()
        x = np.floor(np.log(1-U)/np.log(1-p)) + 1
        geometricas.append(x)
        soma = sum(geometricas)
    lista.append(soma)