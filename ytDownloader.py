# Caso houver erros após instalar o pytube.
# Se tiver instalado usando "pip install pytube"
# Desinstalar o pytube com o comando "pip uninstall pytube"
# E reinstalar usando o seguinte comando:
# pip install git+https://github.com/nficano/pytube

from pytube import YouTube

# Pega o link do vídeo a ser baixado
print("Youtube Vídeo Downloader")
link = input("Link do vídeo: ")
yt = YouTube(link)

# Pega a melhor resolução disponível 
yd = yt.streams.get_highest_resolution()

# Exibe o titulo do vídeo
print(f"Baixando: {yt.streams[0].title} - Aguarde")

# Local onde o vídeo vai ser salvo
# No exemplo abaixo salva os vídeos na área de trabalho
yd.download('C:/Users/SEU-USUARIO/Desktop')

# Exibe no console ao concluir o download.
print("Download Concluído.")
