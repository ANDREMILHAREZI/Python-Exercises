# Lendo a hora de início do evento
hora_inicio = int(input("Digite a hora de início do evento: "))
minuto_inicio = int(input("Digite o minuto de início do evento: "))
segundo_inicio = int(input("Digite o segundo de início do evento: "))

# Lendo a duração do evento em segundos
duracao_segundos = int(input("Digite a duração do evento em segundos: "))

# Convertendo a hora de início para segundos
segundos_inicio = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio

# Calculando o horário de término do evento
segundos_fim = segundos_inicio + duracao_segundos
hora_fim = segundos_fim // 3600
minuto_fim = (segundos_fim % 3600) // 60
segundo_fim = segundos_fim % 60

# Exibindo o horário de término do evento
print("Horário de término do evento:", hora_fim, ":", minuto_fim, ":", segundo_fim)


