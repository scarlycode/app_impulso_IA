from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

llm = ChatOpenAI(model="gpt-5.6-luna")


def generar_mensaje_motivacional(resumen: dict) -> str:
    """Genera un mensaje corto y motivador según la racha del hábito."""
    estado = "Hoy ya lo cumplió." if resumen["cumplido_hoy"] else "Hoy todavía no lo marca."
    prompt = (
        f"Escribe un mensaje breve (máximo 20 palabras), motivador y en español, "
        f"para alguien que lleva {resumen['racha']} días seguidos cumpliendo "
        f"el hábito '{resumen['nombre']}'. {estado}"
    )
    try:
        return llm.invoke(prompt).content
    except Exception as e:
        print(f"Error IA: {e}")
        return "No pude generar el mensaje ahora, pero tu constancia sigue contando. 💪"
