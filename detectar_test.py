def detectar_resultado (tabuleiro):
	#Linhas Verticais
	for marcador in range(0,1,2):
		if tabuleiro[marcador] == tabuleiro[marcador+3]==tabuleiro[marcador+6]:
			return True
	#Linhas Horizontais
	for horizontal in range(0,9,3):
		if tabuleiro[horizontal] == tabuleiro[horizontal+1]==tabuleiro[horizontal+2]:
			return True
	#Linhas Diagonais
	if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
		return True
	if tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
		return True
	return False

print(detectar_resultado("XXOXXXOXO"))
print(detectar_resultado("1XXX23456"))
print(detectar_resultado("XOOOXOOOX"))
print(detectar_resultado("OOXOXOXOO"))
print(detectar_resultado("1X234XX56"))