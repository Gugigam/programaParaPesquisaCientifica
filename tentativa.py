def vetorUnicoArquivo(arquivo):
	ref_arquivo = open(arquivo,"r")
	arquivoInteiro = []
	arquivoVetorUnico = []
	for linha in ref_arquivo:
		valores = linha.split()
		arquivoInteiro.append(valores)
	
	for i in range(0,len(arquivoInteiro)):
		for j in range(0,len(arquivoInteiro[i])):
			arquivoVetorUnico.append(arquivoInteiro[i][j])
	ref_arquivo.close()
	return (arquivoVetorUnico)


def encontra_Heap_Summary(arquivo_Lista):
  tamanho = len(arquivo_Lista)
  for i in range(0,len(arquivo_Lista)):
    if arquivo_Lista[0] != "HEAP" and arquivo_Lista[0] != "Summary:" :
      del arquivo_Lista[0]
    else :
      return arquivo_Lista

def encontra_exit_allocsUse_alçocsFree_totaloAllocated(saida_Lista):
  tamanho = len(saida_Lista)
  exitt = "nada"
  usage = "nada"
  free = "nada"
  allocated = "nada"
  for index, valor in enumerate(saida_Lista):
    if saida_Lista[index] == "exit:":
      exitt = saida_Lista[index+1]
    if saida_Lista[index] == "usage:":
      usage = saida_Lista[index+1]
    if saida_Lista[index] == "frees,":
      free = saida_Lista[index-1]
    if saida_Lista[index] == "allocated":
      allocated = saida_Lista[index-2]
  if exitt != "nada" and usage != "nada" and free != "nada" and allocated != "nada":
    #dadosHeapSummary = dHS
    dHS = []
    dHS.append(exitt)
    dHS.append(usage)
    dHS.append(free)
    dHS.append(allocated)
    return dHS
    
def validar_leak(saida_Lista):
	for index, valor in enumerate(saida_Lista):
		if saida_Lista[index] == "LEAK" and saida_Lista[index+1] == "SUMMARY:":
			return True			
	return False
	

def numeros_do_leak(dados_do_dHS, existencia_leak):
	if existencia_leak == True:
		definitely = "nada"
		indirectly = "nada"
		possibly = "nada"
		reachable = "nada"
		nulo = 0
		for index, valor in enumerate(saida_Lista):
			if saida_Lista[index] == "definitely":
				definitely = saida_Lista[index+2]
			if saida_Lista[index] == "indirectly":
				indirectly = saida_Lista[index+2]
			if saida_Lista[index] == "possibly":
				possibly = saida_Lista[index+2]
			if saida_Lista[index] == "reachable:":
				reachable = saida_Lista[index+1]
			if definitely != "nada" and indirectly != "nada" and possibly != "nada" and reachable != "nada":
				dados_do_dHS.append(definitely)
				dados_do_dHS.append(indirectly)
				dados_do_dHS.append(possibly)
				dados_do_dHS.append(reachable)
				return dados_do_dHS
			
	else:
		for i in range(0,4):
			dados_do_dHS.append(nulo)
			return dados_do_dHS


x = "saida.txt"
arquivo_Lista = vetorUnicoArquivo(x)
saida_Lista = encontra_Heap_Summary(arquivo_Lista)
dados_do_dHS = encontra_exit_allocsUse_alçocsFree_totaloAllocated(saida_Lista)
existencia_leak = validar_leak(saida_Lista)
dados_gerais = numeros_do_leak(dados_do_dHS, existencia_leak)
print(dados_gerais)

