import xlwt
from bs4 import BeautifulSoup
from random import choice
import requests

desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

def random_headers():
    return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

pagina = 0
estado = 0
q = 0
linha_questao = 1 # começa com 1 porque é a segunda linha da planilha
linha_alternativa = 1
cor_linha = 0

# criar um arquivo em branco
w = xlwt.Workbook()
# criar uma planilha no arquivo
ws = w.add_sheet('Prova')

# adicionar uma nova cor com os parâmetros RGB
xlwt.add_palette_colour("custom_colour", 0x21)
w.set_colour_RGB(0x21, 251, 228, 228)

headline = xlwt.easyxf('pattern: pattern solid, fore_colour gray25; border: bottom thick, top thick, right thick; font: bold on; align: wrap on, vert centre, horiz left')
style1 = xlwt.easyxf('pattern: pattern solid, fore_colour pale_blue; align: wrap on, vert centre, horiz left; border: bottom thick, left thick, right thick, top thick')
style2 = xlwt.easyxf('pattern: pattern solid, fore_colour gray25; align: wrap on, vert centre, horiz left; border: bottom thick, left thick, right thick, top thick')

# escrever em uma célula
ws.write(0,0,'prova_ano',style=headline)
ws.write(0,1,'prova_esfera',style=headline)
ws.write(0,2,'prova_banca',style=headline)
ws.write(0,3,'prova_tipo',style=headline)
ws.write(0,4,'prova_escolaridade',style=headline)
ws.write(0,5,'prova_area',style=headline)
ws.write(0,6,'prova_instituto',style=headline)
ws.write(0,7,'prova_instituto_uf',style=headline)
ws.write(0,8,'prova_instituto_municipio',style=headline)
ws.write(0,9,'prova_supercargo',style=headline)
ws.write(0,10,'prova_cargo',style=headline)
ws.write(0,11,'prova_ninscritos_tot',style=headline)
ws.write(0,12,'prova_ninscritos_amplo',style=headline)
ws.write(0,13,'prova_ninscritos_negro',style=headline)
ws.write(0,14,'prova_ninscritos_def',style=headline)
ws.write(0,15,'prova_nota_max_amplo',style=headline)
ws.write(0,16,'prova_nota_max_negro',style=headline)
ws.write(0,17,'prova_prova_nota_max_def',style=headline)
ws.write(0,18,'prova_corte_amplo',style=headline)
ws.write(0,19,'prova_corte_negro',style=headline)
ws.write(0,20,'prova_corte_def',style=headline)
ws.write(0,21,'quest_materia',style=headline)
ws.write(0,22,'quest_anulada',style=headline)
ws.write(0,23,'quest_obs',style=headline)
ws.write(0,24,'quest_txt_ass',style=headline)
ws.write(0,25,'quest_no',style=headline)
ws.write(0,26,'quest_corpo',style=headline)
ws.write(0,27,'assert_letra',style=headline)
ws.write(0,28,'assert_corpo',style=headline)
ws.write(0,29,'assert_correta',style=headline)
ws.write(0,30,'assert_jurisprudencia',style=headline)
ws.write(0,31,'assert_doutrina',style=headline)
ws.write(0,32,'assert_obs',style=headline)
ws.write(0,33,'lei_municipio',style=headline)
ws.write(0,34,'lei_uf',style=headline)
ws.write(0,35,'lei_esfera',style=headline)
ws.write(0,36,'lei_tipo',style=headline)
ws.write(0,37,'lei_diploma',style=headline)
ws.write(0,38,'lei_ano',style=headline)
ws.write(0,39,'lei_artigo',style=headline)
ws.write(0,40,'lei_paragrafo',style=headline)
ws.write(0,41,'lei_inciso',style=headline)
ws.write(0,42,'lei_alinea',style=headline)
ws.write(0,43,'prova_alt_art_tipo',style=headline)
ws.write(0,44,'lei_alt_art_diploma',style=headline)
ws.write(0,45,'lei_alt_art_ano',style=headline)
ws.write(0,46,'lei_alt_paragrafo_tipo',style=headline)
ws.write(0,47,'lei_alt_paragrafo_diploma',style=headline)
ws.write(0,48,'lei_alt_paragrafo_ano',style=headline)
ws.write(0,49,'lei_alt_inciso_tipo',style=headline)
ws.write(0,50,'lei_alt_inciso_diploma',style=headline)
ws.write(0,51,'lei_alt_inciso_ano',style=headline)
ws.write(0,52,'lei_alt_alinea_tipo',style=headline)
ws.write(0,53,'lei_alt_alinea_diploma',style=headline)
ws.write(0,54,'lei_alt_alinea_ano',style=headline)
ws.write(0,55,'sumula_entidade',style=headline)
ws.write(0,56,'sumula_numero',style=headline)
ws.write(0,57,'sumula_vinculante',style=headline)
ws.write(0,58,'oj_entidade',style=headline)
ws.write(0,59,'oj_numero',style=headline)
ws.write(0,60,'enun_entidade',style=headline)
ws.write(0,61,'enun_numero',style=headline)

while estado is not None:
    pagina+=1
    source = requests.get(f'https://www.qconcursos.com/questoes-de-concursos/provas/cespe-2018-pgm-joao-pessoa-pb-procurador-do-municipio/questoes?page={pagina}', headers = random_headers()).text
    soup = BeautifulSoup(source, 'lxml')
    estado = soup.find('div', class_='q-question-body')

    for questao in soup.find_all('div', class_='q-question-body'):
        a = 0
        # desatualizado = questao.find('div', class_='q-caption')
        # print(desatualizado)
        print('')
        enunciado = questao.find('div', class_='q-question-enunciation').text
        q+=1
        print(f'{q}) ', end='')
        print(enunciado)
        if cor_linha%2 == 0:
            style = style1
        else:
            style = style2
        ws.write(linha_questao, 24, q, style=style)
        ws.write(linha_questao, 25, enunciado, style=style)
        for alternativa in questao.find_all('div', class_='q-item-enum js-alternative-content'):
            a+=1
            print(f'{q}.{a}', end=' ')
            if a == 1:
                ws.write(linha_alternativa, 26, 'A', style=style)
                alternativa = alternativa.text
                ws.write(linha_alternativa, 27, alternativa, style=style)
                print(alternativa)
                print('')
                linha_alternativa +=1
            elif a == 2:
                ws.write(linha_alternativa, 26, 'B', style=style)
                alternativa = alternativa.text
                ws.write(linha_alternativa, 27, alternativa, style=style)
                print(alternativa)
                print('')
                linha_alternativa +=1
            elif a == 3:
                ws.write(linha_alternativa, 26, 'C', style=style)
                alternativa = alternativa.text
                ws.write(linha_alternativa, 27, alternativa, style=style)
                print(alternativa)
                print('')
                linha_alternativa +=1
            elif a == 4:
                ws.write(linha_alternativa, 26, 'D', style=style)
                alternativa = alternativa.text
                ws.write(linha_alternativa, 27, alternativa, style=style)
                print(alternativa)
                print('')
                linha_alternativa +=1
            elif a == 5:
                ws.write(linha_alternativa, 26, 'E', style=style)
                alternativa = alternativa.text
                ws.write(linha_alternativa, 27, alternativa, style=style)
                print(alternativa)
                print('')
                linha_alternativa +=1
        linha_questao+=5
        cor_linha+=1

# salvar o arquivo
w.save('CESPE - 2018 - PGM - João Pessoa - PB - Procurador do Município.xls')

