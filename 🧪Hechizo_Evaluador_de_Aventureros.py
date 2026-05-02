# 🧠 Hechizo: Evaluador de Aventureros

aventureros = [
    {"nombre": "German", "nivel": 5},
    {"nombre": "Lena", "nivel": 12},
    {"nombre": "Kai", "nivel": 20},
    {"nombre": "Mira", "nivel": 2}
]

# 🧪 Lambda para clasificar nivel
clasificar = lambda nivel: "Alto" if nivel >= 15 else "Medio" if nivel >= 5 else "Bajo"

# 🧪 Lambda para detectar élite
es_elite = lambda nivel: nivel >= 15

#Nueva Mazmorra Élite
mazmorra_elite = lambda nivel: "Experto" if nivel > 10 else "Aprendiz" if nivel >= 3 and nivel <= 10 else "Novato"

# ⚙️ Procesamiento
for aventurero in aventureros:
    nombre = aventurero["nombre"]
    nivel = aventurero["nivel"]
    
    rango = clasificar(nivel)
    elite = es_elite(nivel)
    puede = mazmorra_elite(nivel)
    
    print(f"{nombre} | Nivel: {nivel} | Rango: {rango} | Elite: {elite} | Mazmorra Élite: {puede}")