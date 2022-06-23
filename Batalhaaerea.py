import pygame
import random
from funcoesajuda import clean, mimir, registro

acionamento = True
arroba = True

while True:
    clean()
    print()
    print("SEJA BEM VINDO A BATALHA AEREA BETA.01")
    print()
    print("Deixe aqui seu nome e email registrados , para receber as proximas atulizações :")
    print()
    while acionamento == True:
        conteudo = registro()
        nome = input("Nome: ")
        while arroba == True:
            email = input(str("Email: "))
            if "@" in email and ".com" in email:
                conteudo = conteudo + nome + "\n" + "\n" 
                arroba = False
                acionamento = False
                break
            elif "@" not in email or ".com" not in email:
                print ("Digite um Email Valido , PLEASE!")
                arroba = Face

        arquivo = open("Registrotets.txt", "w")
        arquivo.write(conteudo)
        arquivo.close()
        print("Registro Salvo , Valeu aí")
        mimir()
        if arroba == False:
            break
    if arroba == False:
        clean()
        break        

pygame.init()

largura = 900
altura = 400
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Sanin Play")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("assets/saikomene.jpg")
pygameDisplay.set_icon(gameIcon)

bg = pygame.image.load("assets/TorreVing.png")
bg_destroy = pygame.image.load("assets/TorreOver.jpg")

explosaoSound = pygame.mixer.Sound("assets/Gameover.mp3")
explosaoSound.set_volume(0.5)
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
gameEvents = pygame.event

def dead(pontos):
    gameDisplay.blit(bg_destroy, (0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
    texto = fonte.render("Perdeu PlayBoy "+str(pontos) +
                         " pontos!", True, black)
    textoContinue = fonteContinue.render(
        "Press enter to continue...", True, white)
    gameDisplay.blit(textoContinue, (50, 200))
    gameDisplay.blit(texto, (50, 100))
    pygameDisplay.update()

def jogo():
    posicaoX = 0
    posicaoY = random.randrange(0, altura)
    direcao = True
    velocidade = 1
    posicaoXNave = 500
    posicaoYNave = 100
    movimentoXNave = 0
    movimentoYNave = 0
    pontos = 0
    missile = pygame.image.load("assets/D.va.png")
    nave = pygame.image.load("assets/pharah.png")
    missile = pygame.transform.flip(missile, True, False)
    pygame.mixer.music.load("assets/Naruto Theme.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    missileSound = pygame.mixer.Sound("assets/Michael Jackson Hee Hee.mp3")
    missileSound.set_volume(0.8)
    pygame.mixer.Sound.play(missileSound)

    alturaNave = 170
    larguraNave = 170
    alturaMissel = 80
    larguraMissel = 80
    dificuldade = 29
    jogando = True
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jogo()
                if event.key == pygame.K_LEFT:
                    movimentoXNave = - 10
                elif event.key == pygame.K_RIGHT:
                    movimentoXNave = 10
                elif event.key == pygame.K_UP:
                    movimentoYNave = -10
                elif event.key == pygame.K_DOWN:
                    movimentoYNave = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXNave = 0
                    movimentoYNave = 0    
        if jogando == True:
            posicaoXNave = posicaoXNave + movimentoXNave
            posicaoYNave = posicaoYNave + movimentoYNave
            if posicaoXNave < 0:
                posicaoXNave = 0
            elif posicaoXNave >= largura - larguraNave:
                posicaoXNave = largura - larguraNave

            if posicaoYNave < 0:
                posicaoYNave = 0
            elif posicaoYNave >= altura - alturaNave:
                posicaoYNave = altura - alturaNave

            gameDisplay.blit(bg, (0, 0))
            
            if direcao == True:
                if posicaoX < largura-150:
                    posicaoX = posicaoX + velocidade
                else:
                    pygame.mixer.Sound.play(missileSound)
                    direcao = False
                    posicaoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    missile = pygame.transform.flip(missile, True, False)
                    pontos = pontos + 1
                               
            else:
                if posicaoX >= 0:
                    posicaoX = posicaoX - velocidade
                else:
                    pygame.mixer.Sound.play(missileSound)
                    direcao = True
                    posicaoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    missile = pygame.transform.flip(missile, True, False)
                    pontos = pontos + 1
                
            gameDisplay.blit(missile, (posicaoX, posicaoY))
            gameDisplay.blit(nave, (posicaoXNave, posicaoYNave))
            
            fonte = pygame.font.Font("freesansbold.ttf", 30)
            texto = fonte.render("Pontos: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 20))

            pixelsYNave = list(
                range(posicaoYNave, posicaoYNave + alturaNave+1))
            pixelsXNave = list(
                range(posicaoXNave, posicaoXNave + larguraNave+1))

            pixelsYMissel = list(range(posicaoY, posicaoY+alturaMissel+1))
            pixelsXMissel = list(range(posicaoX, posicaoX+larguraMissel+1))

            if len(list(set(pixelsYMissel) & set(pixelsYNave))) > dificuldade:
                if len(list(set(pixelsXMissel) & set(pixelsXNave))) > dificuldade:
                    jogando = False
                    dead(pontos)

        pygameDisplay.update()
        clock.tick(60)


jogo()


