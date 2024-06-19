from csv import reader
from collections import defaultdict

class CalculaGanador:

    # Se seteo el nombre por determidado del csv
    def leer_datos(self, filename = '0204.csv'):
        data = []
        with open(filename, 'r') as csvfile:
            lector = reader(csvfile)
            next(lector)
            for fila in lector:
                data.append(fila)
        return data

    # Extrayendo el conteo de votos de calcularganador a un nuevo metodo
    def contar_votos(self, data):
        votos_por_candidato = defaultdict(int) 
        for fila in data:
            candidato = fila[4]                             # Renombrando fila[4] a candidato_id              
            if fila[5] == '1' and len(fila[3]) == 8:        # Condicional de dni de 8 digitos
                votos_por_candidato[candidato] += 1             # Simplificando el codigo con +=
        return votos_por_candidato

    # Calculando si es que hay segunda vuelta o no
    def segunda_vuelta(self, candidatos_ordenados):
        totalvotos = 0
        for fila in candidatos_ordenados:
            totalvotos += fila[1]
        umbral = totalvotos/2
        primero = candidatos_ordenados[0]
        if primero[1] >= umbral:
            return True
        return False

    def calcular_ganador(self, data):
        votos_por_candidato = self.contarvotos(data)                # Renombrando a votos_por_candidato
        for candidato, votos in votos_por_candidato.items():
            print(f'candidato: {candidato} votos validos: {votos}')
        candidatos_ordenados = sorted(votos_por_candidato.items(), key=lambda item:item[1], reverse=True)    # Renombrando a candidatos_ordenados
        resultado = []
        if(self.segundaVuelta(candidatos_ordenados)) == False:
            resultado = candidatos_ordenados[0]                   # Si no hay segunda vuelta, se guarda el primero de los candidatos
        else:
            resultado = [candidatos_ordenados[0], candidatos_ordenados[1]]    # Caso contrario, se guardan los dos primeros de los candidatos
        return resultado
    
c = CalculaGanador()

datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
]
print(c.calcularganador(datatest))