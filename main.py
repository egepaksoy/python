import speak
import listen
import substructure
import info
import program

#! DİKKAT: Ses motorunda gtts çok yavaş oyüzden başka birşey araştır


while True:
    voice = listen.listen()
    print('\n' + voice)
    print(speak.speak(program.program(voice)))
