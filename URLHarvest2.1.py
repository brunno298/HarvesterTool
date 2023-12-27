import re
from colorama import init, Fore, Style
from pyfiglet import Figlet

# Inicializar colorama
init()

class URLHarvest:
    def __init__(self):
        # Seu código para a inicialização do objeto vai aqui
        pass

    def extrair_urls(self, texto):
        # Expressão regular para extrair URLs
        padrao = re.compile(r'https?://\S+')

        # Encontrar todas as URLs no texto
        urls = padrao.findall(texto)

        # Remover duplicatas usando um conjunto (set)
        urls_unicas = list(set(urls))

        return urls_unicas

    def salvar_urls_em_txt(self, arquivo, urls):
        # Salvar URLs em um arquivo de texto
        with open(arquivo, 'w') as arquivo_saida:
            for url in urls:
                arquivo_saida.write(url + '\n')

    def ler_urls_de_txt(self, arquivo, encoding='utf-8'):
        # Ler URLs de um arquivo de texto
        try:
            with open(arquivo, 'r', encoding=encoding) as arquivo_entrada:
                texto = arquivo_entrada.read()
            return texto
        except (OSError, IOError) as e:
            return ''

    def exibir_template(self):
        """Exibe o template do script em Cores."""
        f = Figlet(font='slant')
        banner = f.renderText('URLHarvest')
        
        template = f"""
{Fore.GREEN}{banner}{Style.RESET_ALL}
{Fore.GREEN}Script para extrair e manipular URLs em Textos Brutos{Style.RESET_ALL}
{Fore.RED}Autor:{Style.RESET_ALL} 
{Fore.GREEN}Bruno Azevedo/ The Guardian{Style.RESET_ALL}
{Fore.RED}Instagram:{Style.RESET_ALL} 
{Fore.GREEN}www.instagram.com/guardiao_digitall{Style.RESET_ALL}
{Fore.RED}Data:{Style.RESET_ALL} 
{Fore.GREEN}20 de dezembro de 2023{Style.RESET_ALL}
{Fore.RED}Descrição:{Style.RESET_ALL}
{Fore.GREEN}Este script extrai URLs de um arquivo de texto 
Bruto, adiciona novas URLs e salva de volta no mesmo arquivo, removendo duplicatas.{Style.RESET_ALL}
{Fore.RED}Como usar:{Style.RESET_ALL}
{Fore.GREEN}Pegue Seu Enorme Texto Com as URLs 
Que Precisa Extrair e Salve O Arquivo com a Extensão .TXT
Por Exemplo: Arquivos.txt{Style.RESET_ALL}
"""
        print(template)

    def main(self):
        # Exibir o template
        self.exibir_template()

        # Solicitar ao usuário o nome do arquivo em formato de texto
        nome_arquivo = input(f"{Fore.RED}Por favor, insira o nome do arquivo em formato de texto: {Style.RESET_ALL}")

        # Restante do código permanece inalterado...
        bloco_de_texto = self.ler_urls_de_txt(nome_arquivo)
        urls_encontradas = self.extrair_urls(bloco_de_texto)

        # Adicionar novas URLs e remover duplicatas
        # (adicione esse trecho após o código original)
        novas_urls = [
            'https://novosite1.com',
            'https://novosite2.com',
            # Adicione mais URLs conforme necessário
        ]

        urls_encontradas.extend(novas_urls)
        urls_unicas = list(set(urls_encontradas))

        # Salvar URLs únicas de volta no arquivo
        self.salvar_urls_em_txt(nome_arquivo, urls_unicas)

        for url in urls_unicas:
            print(url)

if __name__ == "__main__":
    url_harvester = URLHarvest()
    url_harvester.main()
