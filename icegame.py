import tkinter as tk
import time


root = tk.Tk()
root.title("As grandes aventuras de Duke")

def print(danaçãoeterna):
    caixaconsole.insert(tk.END, danaçãoeterna + "\n")
    caixaconsole.see(tk.END)
    caixaconsole.config(font=("Cambria", 16))
 
 
caixaconsole = tk.Text(root, height=20, width=100, wrap="word")
caixaconsole.config(state="normal")
caixaconsole.pack()
#jogo liga das legendas
#introdução
print("Duke era conhecido como um grande nadador e extremamente interessado por biologia marinha pelos seus colegas de classe. Com apenas 14 anos, Duke parte em uma expedição em alto-mar a caminho da antártida. No trajeto, sua embarcação acaba tendo uma falha elétrica que deixou o barco sem nenhum sistema de comunicação ou elétrico sequer. Em seguida, foi possível ouvir o que poderia ser o maremoto causado pelas geleiras. O rápido aumento do nível do mar acabou virando a embarcação, naufragando-o de vez. Duke, em um último ato de egoísmo, acabou roubando o bote de sobrevivência, junto com suplementos para si só. A causa do derretimento das geleiras foi completamente inexplicável, mas a rapidez que isso ocorreu acabou decimando grandes cidades. A taxa de casualidades inicial foi gigantesca mas eventos subsequentes extinguiram a humanidade de vez.")

print("Após semanas remando ou deixando o mar levar, Duke encontra um antigo pergaminho em uma das poucas ilhas que ainda restavam. Duke lê sobre o grande e antigo guardião do mar, portador de grandes e temidos poderes. O guardião tinha a capacidade de congelar tudo o que quisesse e quando ele quisesse. Com esse poder, seria possível recongelar as geleiras, recomeçando o mundo. Para isso, ele precisaria se aventurar nas profundezas do mar em esperança de se encontrar com o guardião e remover a gema de sua testa, matando-o e retirando os seus poderes.")
print("Passado alguns dias, Duke consegue enxergar uma espécie de bote brilhante. Duke se aproxima e consegue enxergar a silhueta de um pescador.")

print("Pescador: Um sobrevivente! Até que enfim... Qual o seu nome?")
print("Duke: ...")
print("Ah, você não tem uma boca!")
print("*Duke apontaria para o bote do pescador*")
print("Pescador: Ah, meu bote? Eu tive muita sorte dele não despedaçar quando o mar subiu tão subitamente. Eu investi um dinheirão nele antes disso tudo acontecer.")
print("*Duke observa o bote um pouquinho mais de perto, e realmente, o bote parecia extremamente caro. Tinha tecnologia de ponta, âncoras, bússolas, GPS e até um motor.*")
print("*Duke sinaliza para o pescador que deseja embarcar junto em troca de comida, já que o bote de emergência já estava se despedaçando.*")
print("Pescador: Se bem que eu estava precisando de comida. Muito obrigado!")
print("*Duke pede para o pescador ancorar o barco, pois ele ia nadar*")
print("Pescador: Nadar? Você só pode estar louco...")
print("*O pescador abre o baú de seu bote, revelando uma roupa térmica de mergulho, reguladores de oxigênio, um compressor e um tanque de ar.")
print("*Duke faz um gesto e o pescador fica imóvel*")
print("Pescador: Eu sei disso.")
print("Pescador: O que posso fazer é lhe desejar boa sorte. Você diz que não vais demorar muito, mas não boto fé. Qualquer coisa, retorne a superfície.")
print("Pescador: Tome esta corda comicamente longa, amarre-a na cintura e vá.\n")

print("---Você pode ignorar a história se você já a viu.---")

print("---GAME START---")

Vida1 = 10
peixe_espadavida= 6
Dano = 2
piranha = 4
reaper = 50
branco = 25
guardião = 700


print("Você entra no mar...")
print("Logo de cara, você se depara com um peixe espada, Você deseja lutar?")

def Cenario5():
    global Vida1
    print("Um portal se abre...")
    print("Duke entra neste caminho e se depara com uma sala totalmente branca...")
    print("'Isto não estava escrito no pergaminho!' Duke pensa para si mesmo.")
    print("Duke enxerga na distância uma silhueta branca de um humanóide. Sua testa brilhava vermelho. Estava sentada numa pedra, era o único objeto naquela 'sala'.")
    print("Duke,sem dúvidas, sabia que aquele era o guardião.")

    print("Duke corre para cima dele sem pensar!")

    print("Duke percebe uma barragem de pedras chegando por cima!")
    print("Duke conseguiu se esquivar por muito pouco!")
    print("O guardião se levanta. Sem o guardião falar sequer uma palavra, Duke conseguiu entender suas intenções.")
    print("Ele desejava um duelo com um guerreiro digno de conseguir seus poderes, e Duke foi o primeiro a derrotar o Leviatã..")

    print("O grande duelo começa... Você se sente rejuvenescido! (HP = 200)")
    Vida1 = 200

    def AtacarGA():
        global guardião, Vida1, Dano
        guardião -= Dano
        print(f"O Guardião perde {Dano} de vida")
        print("O Guardião te ataca novamente")
        Vida1 -= 15
        print("-7HP")
        print(f"Você tem {Vida1} de vida.")
        if guardião < 0:
            print("Você enfia a sua espada no peito do guardião e ele se desmancha em pó...")
            print("Apenas a gema sobrou...")
            print("Duke coloca a gema em sua testa...")
            print("...")
            print("Duke é teleportado para a superfície...")
            print("Ele conseguiu!")
            print("Ele conseguiu mudar o destino da humanidade!")
            print("Duke recongela as geleiras, rapidamente retirando a água que alagava tudo...")
            print("Duke decidiu não se proclamar o herói e começou a viver uma vida normal na sociedade.")

            botaocurar.destroy()
            botaoatacar.destroy()

        if Vida1 < 0:
            print("Você é apedrejado e morto...")
            exit()
        if Vida1 <= 10:
            print("Você precisa se curar imediatamente!!!")

    def CurarGA():
        global Dano, Vida1
        if Vida1 < 100:
            print("Você se cura, ganhando 35 de vida.")
            Vida1 += 25
        if Vida1 >= 100:
            print("Você não faz nada, pois não há nada para curar...")
        print("A criatura te ataca novamente")
        print("-15HP")
        Vida1 -= 15
        print(f"Você tem {Vida1} de vida...")
        if Vida1 < 0:
            print("Você é espedaçado...")
            exit()      

    botaocurar = tk.Button(root, text="Curar!",command = CurarGA)
    botaoatacar = tk.Button(root, text="Atacar!", command=AtacarGA)
    botaocurar.pack(side="left")
    botaoatacar.pack(side="left")


def Cenario4():
    print("A leveza logo passou no momento que você se depara com uma grande criatura...")
    print("Duke já leu sobre esta criatura, mas não imaginava encontrá-la...")
    print("O que Duke enxergou nada mais é que um Leviatã Ceifador.")
    print("O caminho atrás de você se fecha! Boa sorte <3")



    def AtacarLE():
        global reaper, Vida1, Dano
        reaper -= Dano
        print(f"Reaper perde {Dano} de vida")
        print("Reaper te ataca novamente")
        Vida1 -= 7
        print("-7HP")
        print(f"Você tem {Vida1} de vida.")
        if reaper < 0:
            print("Você corre sua espada contra a barriga da criatura e a mata!")
            print("O Leviatã regurgita centenas de armaduras e espadas de um tempo antigo...")
            print("Você escolhe as mais brilhosas!")
            Vida1 += 165
            Dano += 60
            print(f"Dano = {Dano}")
            print(f"Vida total = {Vida1}")
            botaocurar.destroy()
            botaoatacar.destroy()
            Cenario5()
        if Vida1 < 0:
            print("Você é comido vivo...")
            exit()
        if Vida1 <= 3:
            print("Você precisa se curar imediatamente!!!")
    
    def CurarLE():
        global Dano, Vida1
        if Vida1 < 20:
            print("Você se cura, ganhando 3 de vida.")
            Vida1 += 10
        if Vida1 >= 20:
            print("Você não faz nada, pois não há nada para curar...")
        print("A criatura te ataca novamente")
        print("-7HP")
        Vida1 -= 7
        print(f"Você tem {Vida1} de vida...")
        if Vida1 < 0:
            print("Você é comido vivo...")
            exit()      

        return

    botaocurar = tk.Button(root, text="Curar!",command = CurarLE)
    botaoatacar = tk.Button(root, text="Atacar!", command=AtacarLE)
    botaocurar.pack(side="left")
    botaoatacar.pack(side="left")

def Cenario3():
    print("Você sai da caverna e se depara com um maldito tubarão branco. Ele está partindo pra cima. Você não tem como fugir.")

    def AtacarTU():
        global branco, Vida1, Dano
        branco -= Dano
        print(f"O tubarão perde {Dano} de vida")
        print("O tubarão te ataca novamente")
        Vida1 -= 7
        print("-7HP")
        print(f"Você tem {Vida1} de vida.")
        if branco < 0:
            print("Você conseguiu esporrar ele até a morte!")
            print("O corpo do tubarão acaba caindo por cima da entrada da caverna, desmoronando-a de vez. Logo depois, um caminho misterioso se abre no fundo do oceano...")
            print("Ao passar pelo caminho, você se sente mais leve... (HP = 35)")
            Vida1 = 35
            Cenario4()
            botaocurar.destroy()
            botaoatacar.destroy()
        if Vida1 < 0:
            print("Você é comido vivo...")
            exit()
    
    def CurarTU():
        global Dano, Vida1
        if Vida1 < 20:
            print("Você se cura, ganhando 3 de vida.")
            Vida1 += 5
        if Vida1 >= 20:
            print("Você não faz nada, pois não há nada para curar...")
        print("A criatura te ataca novamente")
        print("-HP")
        Vida1 -= 7
        print(f"Você tem {Vida1} de vida...")
        print("Acho que se curar não é recomendado.")
        if Vida1 < 0:
            print("Você é comido vivo...")
            exit()      

        return

    botaocurar = tk.Button(root, text="Curar!",command = CurarTU)
    botaoatacar = tk.Button(root, text="Atacar!", command=AtacarTU)
    botaocurar.pack(side="left")
    botaoatacar.pack(side="left") 


def Cenario2():

    def caminhodireita():
        print("Você nada para a direita.")
        print("Você nada e encontra um baú, porém, dentro dele tinha uma piranha, e ela decide lutar com você.")
        botaoesquerda.destroy()
        botaodireita.destroy()
    
        global piranha, Dano, Vida1
        piranha -= Dano
        print("Você quer atacar ou se tratar?")

        botaoatacar = tk.Button(root, text="Atacar!", command=AtacarPI)
        botaoatacar.pack(side=tk.LEFT)
        botaocurar = tk.Button(root, text="Curar!",command = CurarPI)
        botaocurar.pack(side=tk.LEFT)


    def AtacarPI():
        global piranha, Dano, Vida1
        piranha -= Dano
        print("Você ataca o peixe!!!")
        print(f"{Dano} de dano!")
        print("A criatura te ataca novamente...")
        Vida1 -=1
        print("-1HP")
        print(f"Você tem {Vida1} de vida...")
        if piranha < 0:
            print("Você matou ele! Parabéns.")
            botaoatacar.destroy()
            botaocurar.destroy()
            Cenario3()
        if Vida1 < 1:
            print("Você foi comido!")
            exit()

    def CurarPI():
        global piranha, Dano, Vida1
        if Vida1 < 10:
            print("Você se cura, ganhando 3 de vida.")
            Vida1 += 3
        if Vida1 >= 10:
            print("Você não faz nada, pois não há nada para curar...")
        print("A criatura te ataca novamente")
        print("-HP")
        Vida1 -=1
        print(f"Você tem {Vida1} de vida...")      

    def caminhoesquerda():
        botaoesquerda.destroy()
        botaodireita.destroy()
        global Dano, Vida1
        print("Você nada para a esquerda.")
        print("Você encontra um baú, nesse baú, você encontra uma espada antiga e uma grande armadura.")
        Dano += 8
        Vida1 += 25
        print(f"Dano total = {Dano}")
        print(f"Vida total = {Vida1}")
        Cenario3() 

       
    botaocurar = tk.Button(root, text="Curar!",command = CurarPI)
    botaoatacar = tk.Button(root, text="Atacar!", command=AtacarPI)    
    def caminhodireita():
        print("Você nada para a direita.")
        print("Você nada e encontra um baú, porém, dentro dele tinha uma piranha, e ela decide lutar com você.")
        botaoesquerda.destroy()
        botaodireita.destroy()
        
        global piranha, Dano, Vida1
        piranha -= Dano
        print("Você quer atacar ou se tratar?")

        botaoatacar.pack(side=tk.LEFT)
        botaocurar.pack(side=tk.LEFT)
    
    print("Após nadar por não-sei-quantos minutos, você se depara com uma caverna se dividindo entre esquerda e direita. Qual caminho você escolhe?")

    botaoesquerda = tk.Button(root, text="Avançar para a esquerda!", command=caminhoesquerda)
    botaoesquerda.pack(side="left")

    botaodireita = tk.Button(root, text="Avançar para a direita!", command=caminhodireita)
    botaodireita.pack(side="left")

def batalhaPE():
    def AtacarPE():
        global peixe_espadavida, Dano, Vida1
        peixe_espadavida -= Dano
        print("Você ataca o peixe!!!")
        print(f"{Dano} de dano!")
        print("A criatura te ataca novamente...")
        Vida1 -=1
        print("-1HP")
        print(f"Você tem {Vida1} de vida...")
        if peixe_espadavida < 0:
            print("Você matou ele! Parabéns.")
            Cenario2()
            botaoatacar.destroy()
            botaocurar.destroy()
        if Vida1 < 1:
            print("Você foi perfurado e morto...")
            exit()
    
   

    def CurarPE():
        global peixe_espadavida, Dano, Vida1
        if Vida1 < 10:
            print("Você se cura, ganhando 3 de vida.")
            Vida1 += 3
        if Vida1 >= 10:
            print("Você não faz nada, pois não há nada para curar...")
        print("A criatura te ataca novamente")
        print("-HP")
        Vida1 -=1
        print(f"Você tem {Vida1} de vida...")      
    

    botaosimatacar.destroy()
    botaonaoatacar.destroy()
    print("Você começa a jogar socos no peixe e ele te ataca de volta.")

    print("Você quer atacar ou se tratar?")

    botaoatacar = tk.Button(root, text="Atacar!", command=AtacarPE)
    botaoatacar.pack(side=tk.LEFT)
    botaocurar = tk.Button(root, text="Curar!",command = CurarPE)
    botaocurar.pack(side=tk.LEFT)
def FugirPE():
    print("Você decide fugir do peixe, e ele parece não se importar.")
    botaonaoatacar.destroy()
    botaosimatacar.destroy()
    Cenario2()

botaosimatacar = tk.Button(root, text="Sim, quero espancar-lo.", command=batalhaPE)
botaosimatacar.pack(side=tk.LEFT)

botaonaoatacar = tk.Button(root, text="Não!", command=FugirPE)
botaonaoatacar.pack(side=tk.LEFT)










#fim liga das lendas
tk.mainloop()