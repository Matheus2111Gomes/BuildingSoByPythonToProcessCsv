from csv_operations import processCsvFile

if __name__ == "__main__":
    nome_arquivo = 'dataTeste.csv'  # nome do arquivo CSV
    selected_columns = "idade,cidade"  # colunas selecionadas (pode ter maiúsculas e minúsculas misturadas)
    rowFilterDefinitions = "Idade>30\ncidade==Belo horizonte"  # filtro a ser aplicado

    processCsvFile(nome_arquivo, selected_columns, rowFilterDefinitions)