# o programa deve tocar uma música
from pygame import mixer
mixer.init()
mixer.music.load('C:\\Users\\luis.jesus\\Desktop\\Projetos - Python\\Desafios do Curso em Vídeo\\Materiais\\021.mp3')
mixer.music.play()
x = input('Aperte Enter para parar...')
