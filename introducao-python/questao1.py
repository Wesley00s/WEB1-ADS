# 1. Quantos segundos há em 70 minutos e 42 segundos?

def sec_count(minutes, seconds):
    return minutes * 60 + seconds

result = sec_count(70, 42)
print(f'{result} segundos')