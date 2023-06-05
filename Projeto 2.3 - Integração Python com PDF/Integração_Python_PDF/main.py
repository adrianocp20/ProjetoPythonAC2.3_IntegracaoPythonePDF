#Importando Bibliotecas
import tabula
import PyPDF2 as pyf
from pathlib import Path

#Funções pyPDF2
pyf.PdfReader #Ler o PDF
pyf.PdfWriter #Escrever PDF
pyf.PdfMerger #Juntar PDF

#Ler arquivo PDF
#nome_arquivo = "MGLU_ER_3T20_POR.pdf" #Arquivo na mesma pasta do projeto
#arquivo_pdf = pyf.PdfReader(nome_arquivo)

i = 1 #Inicia como identificador da página 1

#Percorrer todas as páginas do arquivo e salvando individualmente cada página percorrida
#for pagina in arquivo_pdf.pages:
    #arquivo_novo = pyf.PdfWriter()
    #arquivo_novo.add_page(pagina)
    #Criar e Salvar Arquivo1, salvando o arquivo.novo dentro arquivo,final
    #with Path(f'paginas/Arquivos{i}.pdf').open(mode='wb') as arquivo_final:
        #arquivo_novo.write(arquivo_final)
        #i += 1 #Incrementa o numero na pagina que vai salvar em cada arquivo

#paginas = [1, 14, 16] #Numeros das paginas que são necessárias juntar

#Criar um novo PDF
#novo_pdf = pyf.PdfWriter()

#for num_pagina in paginas:
    #Pegar o arquivo num_pagina
    #nome_arquivo = f"paginas/Arquivos{num_pagina}.pdf"
    #arquivo_pdf = pyf.PdfReader(nome_arquivo)
    #pagina = arquivo_pdf.pages[0] #Pegar a pagina de indice [0] devido ter apenas uma folha
    #Adicionar no novo PDF
    #novo_pdf.add_page(pagina)

#Salvar o novo pdf
#with Path(f"Consolidado.pdf").open(mode='wb') as arquivo_final:
    #novo_pdf.write(arquivo_final)

#Adionando 2 arquivos de PDF em um só
#pdf_mesclado = pyf.PdfMerger()

#arquivo1 = "MGLU_ER_3T20_POR.pdf"
#arquivo2 = "MGLU_ER_4T20_POR.pdf"

#pdf_mesclado.append(arquivo1)
#pdf_mesclado.append(arquivo2)

#with Path(f'ConsolidadoAppend.pdf').open(mode='wb') as arquivo_final:
    #pdf_mesclado.write(arquivo_final)

#Adionando um arquivo no meio de outro arquivo (merge)
#pdf_mesclado2 = pyf.PdfMerger()

#pdf_mesclado2.append(arquivo1)
#pdf_mesclado2.merge(1, arquivo2)

#with Path(f'ConsolidadoMerge.pdf').open(mode='wb') as arquivo_final:
    #pdf_mesclado2.write(arquivo_final)

#Função para rodar a pagina

#pdf_rodar = pyf.PdfReader(arquivo1)

#pdf_final = pyf.PdfWriter()
#for pagina in pdf_rodar.pages:
    #pagina.rotate(90) #rotate-> Sentido Horario / (90) -> Angulo rotacionado
    #pdf_final.add_page(pagina)

#with Path(f'ArquivoRodado.pdf').open(mode='wb') as arquivo_final:
    #pdf_final.write(arquivo_final)

#Trabalhando com Textos e Informações Dentro do PDF
#Objetivo 01: Pegar texto da página e identificar onde está essa informação
#nome_arquivo = "MGLU_ER_4T20_POR.pdf"
#arquivo = pyf.PdfReader(nome_arquivo)

#numero_paginas = len(arquivo.pages)
#print(numero_paginas)

#infos = arquivo.metadata
#print(infos)

#texto_procurado = """| Despesas com Vendas """

#for pagina in arquivo.pages:
    # Percorrendo todas as paginas
    # Pegar o que está escrito na página
    #texto_pagina = pagina.extract_text()
    # Verificar se no dentro do texto da página tem o [texto_procurado]
    #if texto_procurado in texto_pagina:
    # Se tiver, me diz qual é o numero da página
        #print(f'Está na Página{i}')
        #numero_paginas = i
        #texto_final = texto_pagina
        #print(texto_final)
    #i += 1
    #if i == 10:
        #print(texto_pagina) -> Localizar uma caracteristica no texto para identificar apenas o que está procurando

#posicao = texto_final.find("| Despesas com Vendas") #Encontrar a posição do texto final
#print(posicao)
#posicao_final = texto_final.find("|", posicao + 1) #Encontra a ultima posição do texto final
#print(posicao_final)
#texto_despesa = texto_final[posicao:posicao_final] #Pega o texto da posição inicial ate a final
#print(texto_despesa)

#Objetivo 02: Analisar o DRE (sem ajuste - Página 5)
# Para ler tabelas usar biblioteca 'tabula'

#mglu_3t20 = "MGLU_ER_3T20_POR.pdf"

#df = tabula.table(mglu_3t20)
#tabela = df[0]
