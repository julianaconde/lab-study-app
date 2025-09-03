# Paso 3: Backend e Integración con IA

> **Resumen:**
> En este paso, implementarás la funcionalidad principal de StudyPlan AI conectando el backend a los modelos de IA de GitHub y creando el endpoint de API que impulsa la aplicación.

## Descripción General de la Aplicación StudyPlan

StudyPlan AI sigue un flujo de procesamiento claro, comenzando desde la entrada del usuario y terminando con un plan de estudio personalizado:

1. **Entrada del Usuario:** El usuario completa un formulario en la interfaz web con su información de perfil (área de interés, nivel de habilidad actual, tiempo de estudio disponible).

2. **Capa de API (`app/api/api.py`):** Recibe la solicitud, valida los datos y los mapea a los objetos de modelo apropiados.

3. **Servicio de Prompts (`app/services/prompts.py`):** Formatea la información del usuario en instrucciones estructuradas para el modelo de IA, diseñadas para producir resultados óptimos.

4. **Cliente de GitHub (`app/services/github_client.py`):** Envía las instrucciones formateadas a los Modelos de GitHub y espera la respuesta de la IA.

5. **Manejo de Respuesta:** La respuesta generada por la IA es procesada, formateada y devuelta al usuario a través de la interfaz web como un plan de estudio estructurado y personalizado.

## ⌨️ Actividad: Implementar el Cliente de Modelos de GitHub

El cliente de Modelos de GitHub es esencial para comunicarse con los servicios de IA. Maneja la autenticación, el formato de solicitudes y el procesamiento de respuestas, permitiendo que StudyPlan AI genere contenido personalizado. En esta actividad, implementaremos el cliente que se comunica con las capacidades de IA de GitHub.

1. Abre `app/services/github_client.py`. Verás la clase `GitHubModelsClient` con alguna estructura predefinida, incluyendo métodos de inicialización y configuración.

2. En la clase `GitHubModelsClient`, haz clic derecho en el nombre de la clase y selecciona **Explain this** desde el menú contextual de GitHub Copilot para entender su estructura y comportamiento previsto.

3. Abre el panel **Copilot Chat**, cambia al modo **Agent** y pide a Copilot que implemente el cliente usando la biblioteca Azure AI Inference con el siguiente prompt:

    > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
    >
    > ```prompt
    > Implementa el cliente de Modelos de GitHub usando la biblioteca Azure AI Inference:
    >
    > - Primero instala el paquete requerido: pip install azure-ai-inference
    > - Usa ChatCompletionsClient de azure.ai.inference
    > - Usa SystemMessage y UserMessage de azure.ai.inference.models
    > - Conéctate al endpoint https://models.github.ai/inference
    > - Usa el modelo openai/gpt-4o-mini
    > - Implementa una respuesta simulada de respaldo para pruebas
    > - Maneja errores y proporciona mensajes de error detallados
    > ```

> [!IMPORTANTE]
> Cuando envíes este prompt, Copilot Chat puede solicitar permiso para instalar el paquete Azure AI Inference.
> - Haz clic en **Continue** en la ventana de chat para autorizar la instalación
>
> - Haz clic en **Keep** cuando se te solicite guardar los cambios en el archivo de requisitos
>
> Este paquete es esencial para establecer comunicación con la API de Modelos de GitHub y habilitar la generación de planes de estudio impulsados por IA.

<details>
  <summary>🤔 ¿Cómo funciona?</summary><br/>

La implementación de **GitHubModelsClient** se integra con los modelos de IA de GitHub para generar planes de estudio personalizados. Utiliza la **biblioteca Azure AI Inference** para establecer conexiones seguras con el endpoint de la API de Modelos de GitHub, maneja la autenticación a través de **tokens de GitHub** y convierte los mensajes del usuario al formato apropiado para el procesamiento de IA. 

El cliente incluye un **mecanismo de respaldo** que cambia automáticamente a respuestas simuladas cuando la API no está disponible, asegurando que la aplicación permanezca funcional durante el desarrollo y las pruebas.

</details>

---

| [← Verificar tu entorno](02-step.md) | [Siguiente: Modelos de Datos y Endpoint de API →](04-step.md) |
|:-----------------------------------|------------------------------------------:|
