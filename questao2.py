'''
2) Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos
minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor
09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta
quantos minutos já se passaram desde às 00:00h deste dia
'''

horas = int(input("informe o valor das horas do horário atual: "))
minutos = int(input("informe o valor dos minutos do horario atual: "))

minutos_totais =  (horas * 60) + minutos

print(f"Desde 00:00h até {hora_atual:02d}:{minutos_atual:02d} se passaram {minutos_passados} minutos.")