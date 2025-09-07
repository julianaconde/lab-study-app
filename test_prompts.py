from app.services.prompts import build_study_plan_prompt

if __name__ == "__main__":
    # Parâmetros do teste
    area = "backend"
    nivel = "iniciante"
    tempo = 10
    duracao = 3
    objetivos = "Quero construir APIs REST com Node.js"

    prompt = build_study_plan_prompt(area, nivel, tempo, duracao, objetivos)
    for msg in prompt:
        print(f"Role: {msg['role']}")
        print(msg['content'])
        print("-"*40)
