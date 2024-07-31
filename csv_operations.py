import io

def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
        csv_data = [linha.strip().split(',') for linha in linhas]
    return csv_data

def selecionar_colunas(csv_data, selected_columns):
    headers = csv_data[0]
    if selected_columns != "":
        selected_headers = [header.strip().lower() for header in selected_columns.split(',')]
        
        
        lower_headers = [header.lower() for header in headers] #corrigir erros de case-sensitive
        
        selected_indices = [lower_headers.index(header) for header in selected_headers]
        
        selected_data = []
        for linha in csv_data[1:]:
            selected_line = [linha[idx] for idx in selected_indices]
            selected_data.append(selected_line)
        return selected_data
    else: return csv_data

def adicionar_header(headers):
    header = ','.join(headers).replace(' ','')
    return header

def localizar_indice_header(headers, filtro):
    filtro = filtro.strip()
    filtro = filtro.lower()
    indice = headers.index(filtro)
    return indice

def processCsvFile(nome_arquivo, selected_columns=None, rowFilterDefinitions=None):
    csv_data = ler_arquivo_csv(nome_arquivo)
    selected_columns = selected_columns.strip()

    if selected_columns == "" or selected_columns==None:
        selected_columns = ','.join(csv_data[0]).lower()  # Se selected columns estiver vazio, pegaremos o header para localizar todas as colunas

    selected_data = selecionar_colunas(csv_data, selected_columns)
    
    # Adicionar o cabeçalho (sem modificação, assumindo que selected_columns já está em minúsculas)
    headers = selected_columns.split(',')
    print(adicionar_header(headers))
    
    # Aplicar filtros se fornecidos
    if rowFilterDefinitions:
        filtros = rowFilterDefinitions.strip().split('\n')
        for filtro_individual in filtros:
            selected_data = aplicar_filtro(selected_data, filtro_individual.strip(), headers)
    
    # Imprimir as linhas selecionadas após os filtros
    for linha in selected_data:
        print(','.join(linha))

def remover_acentos_e_lower(texto):
    # Dicionário para mapear caracteres acentuados para sem acento
    mapa_acentos = {
        'á': 'a', 'à': 'a', 'â': 'a', 'ä': 'a', 'ã'
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ñ': 'n', 'ç': 'c'
    }
    
    # Remover acentos e converter para minúsculas
    resultado = []
    for c in texto:
        if c in mapa_acentos:
            resultado.append(mapa_acentos[c])
        else:
            resultado.append(c)
    
    return ''.join(resultado).lower()

def aplicar_filtro(data, filtro, headers):
    filtros = filtro.strip().split('\\n')
    filtered_data = data
    
    for filtro_individual in filtros:
        filtro_individual = filtro_individual.strip()
        campo, operador, valor = parse_filtro(filtro_individual)
        indiceHeader = localizar_indice_header(headers, campo)
        
        # Função para comparar ignorando case-sensitive e acentos
        def comparar_sem_acentos(a, b):
            return remover_acentos_e_lower(a.strip()) == remover_acentos_e_lower(b.strip())
        
        # Aplicar o filtro com base no operador, ignorando case-sensitive e acentos
        if operador == '>':
            filtered_data = [linha for linha in filtered_data if int(linha[indiceHeader].strip().lower()) > int(valor)]
        elif operador == '<':
            filtered_data = [linha for linha in filtered_data if int(linha[indiceHeader].strip().lower()) < int(valor)]
        elif operador == '>=':
            filtered_data = [linha for linha in filtered_data if int(linha[indiceHeader].strip().lower()) >= int(valor)]
        elif operador == '<=':
            filtered_data = [linha for linha in filtered_data if int(linha[indiceHeader].strip().lower()) <= int(valor)]
        elif operador == '==':
            filtered_data = [linha for linha in filtered_data if comparar_sem_acentos(linha[indiceHeader], valor)]
        elif operador == '=':
            operador = "=="
            filtered_data = [linha for linha in filtered_data if comparar_sem_acentos(linha[indiceHeader], valor)]
        else:
            raise ValueError(f"Operador '{operador}' não suportado.")

    return filtered_data

def parse_filtro(filtro):
    for operador in ['>=', '<=', '==', '>', '<']:
        if operador in filtro:
            campo, valor = filtro.split(operador)
            return campo.strip(), operador.strip(), valor.strip()
    raise ValueError(f"Filtro '{filtro}' não é válido.")

def processCsv(csv_string, selected_columns=None, rowFilterDefinitions=None):
    # Ler os dados CSV da string
    csv_data = [linha.split(',') for linha in csv_string.strip().split('\n')]
    
    selected_columns = selected_columns.strip()

    if selected_columns == "" or selected_columns is None:
        selected_columns = ','.join(csv_data[0]).lower()  # Se selected columns estiver vazio, pegaremos o header para localizar todas as colunas

    selected_data = selecionar_colunas(csv_data, selected_columns)
    
    # Adicionar o cabeçalho (sem modificação, assumindo que selected_columns já está em minúsculas)
    headers = selected_columns.split(',')
    print(adicionar_header(headers))
    
    # Aplicar filtros se fornecidos
    if rowFilterDefinitions:
        filtros = rowFilterDefinitions.strip().split('\n')
        for filtro_individual in filtros:
            selected_data = aplicar_filtro(selected_data, filtro_individual.strip(), headers)
    
    # Imprimir as linhas selecionadas após os filtros
    for linha in selected_data:
        print(','.join(linha))

