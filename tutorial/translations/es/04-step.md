# Paso 4: Modelos de Datos y Endpoint de API

> **Resumen:**
> En este paso, crearás los modelos de datos para estructurar solicitudes y respuestas, e implementarás el endpoint de API que conecta la interfaz de usuario con la integración de IA.

## Modelos de Datos y API REST

Para completar nuestra aplicación StudyPlan AI, necesitamos crear:

1. **Modelos de Datos**: Clases que definen la estructura de solicitudes y respuestas, asegurando consistencia y facilitando la validación.

2. **Endpoint de API**: Una ruta Flask que recibe solicitudes de usuario, procesa los datos, interactúa con el cliente de Modelos de GitHub y devuelve el plan de estudio generado.

Este paso es crucial para conectar la interfaz de usuario con la inteligencia artificial, completando el flujo de la aplicación.

## ⌨️ Actividad: Crear Modelos de Datos

Antes de implementar el endpoint de API, necesitamos crear los modelos de datos que estructurarán nuestras solicitudes y respuestas. Estos modelos asegurarán formatos de datos consistentes y facilitarán la validación.

1. Crea un nuevo archivo `app/models/study_plan.py` para definir nuestros modelos de datos.

2. Usa el siguiente prompt con Copilot para implementar los modelos:

    > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
    >
    > ```prompt
    > Crea dos modelos de datos para nuestra aplicación de plan de estudios:
    > 
    > 1. StudyPlanRequest con:
    >    - Campos para area, level, weekly_hours, duration_months, specific_objectives
    >
    > 2. StudyPlanResponse con:
    >    - Campos para structured_plan, success, metadata, error
    > ```

## ⌨️ Actividad: Implementar el Endpoint de API

Con nuestro cliente de Modelos de GitHub y modelos de datos listos, es hora de crear el endpoint de API que impulsa nuestra aplicación. Este endpoint sirve como puente entre el frontend y la IA, manejando solicitudes y devolviendo planes de estudio personalizados.

El endpoint recibe y valida solicitudes de planes de estudio desde el frontend, procesa las preferencias del usuario incluyendo área, nivel y compromiso de tiempo, se comunica con el servicio de IA de Modelos de GitHub, y devuelve contenido educativo estructurado. Al implementar este endpoint, completamos la infraestructura de backend para nuestro generador inteligente de planes de estudio.

1. **Navega al archivo de API** abriendo `app/api/api.py` en el panel Explorer. Este archivo contiene las rutas Flask que definen todos nuestros endpoints de API.

2. **Actualiza las importaciones** para usar los modelos:

```python
from app.models.study_plan import StudyPlanRequest, StudyPlanResponse
```

3. **Abre el panel Copilot Chat** y selecciona el modo **Edit** para ayudar a implementar la funcionalidad faltante. Usa el siguiente prompt:

    > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
    >
    > ```prompt
    > Actualiza la función `generate_study_plan` en la API Flask para usar el cliente de Modelos de GitHub:
    > 
    > - Añade validación para verificar si github_client.token está configurado
    > - Añade una estructura try/except para manejo detallado de errores
    > - Usa `build_study_plan_prompt()` con los parámetros correctos de StudyPlanRequest
    > - Llama a `github_client.chat_completion()` asincrónicamente con los mensajes
    > - Para caso de éxito: devuelve StudyPlanResponse con el plan generado por IA
    > - Para caso de error: devuelve respuesta con success=False y mensaje de error detallado
    > ```

> [!CONSEJO]
> El parámetro de temperatura (establecido en 0.7 en el ejemplo) controla la aleatoriedad de la respuesta de la IA. Valores más bajos (cercanos a 0) hacen que las respuestas sean más deterministas y enfocadas, mientras que valores más altos (cercanos a 1) las hacen más creativas y variadas. Puedes experimentar con este valor para encontrar el equilibrio adecuado para contenido educativo.

---

| [← Backend e Integración con IA](03-step.md) | [Siguiente: Elaboración de Prompts para IA →](05-step.md) |
|:-----------------------------------|------------------------------------------:|
