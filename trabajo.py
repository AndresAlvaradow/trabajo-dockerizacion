from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
    "Universidad": "UTPL",
    "Curso": "Procesos de Ingeniería de Software",
    "Alumno": "Andres Wladimir Alvarado Chillogallo",
    "Período": "Abr/Ago 2021",
    "Lenguaje de programación preferido": "Java",
    "Aspiración PostGraduación": "Me llama la atención lo que es IA en la parte de automatización, y un poco lo que es minería de datos por eso aspiro encontrar un trabajo en cualquiera de estas áreas"
}
