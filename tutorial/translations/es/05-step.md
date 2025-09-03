# Paso 5: Elaboración de Prompts para IA

> **Resumen:**
> En este paso, aprenderás cómo elaborar prompts para la generación de contenido por IA a través de solicitudes de API. Implementarás un sistema de prompts estructurado para StudyPlan AI, lo probarás en diferentes escenarios y lo refinarás iterativamente para producir planes de estudio de alta calidad.

La calidad de los planes de estudio generados por IA depende en gran medida de cómo se escriben los prompts. Los prompts claros y bien estructurados ayudan a la IA a entender el contexto, incluir todos los componentes requeridos y devolver respuestas en el formato correcto. Un sistema de prompts robusto generalmente incluye dos partes:

* **Prompt del Sistema** – Define el rol, tono y directrices de comportamiento de la IA. Por ejemplo, puedes instruir a la IA para que actúe como un mentor educativo o para que siempre proporcione respuestas concisas y estructuradas.
* **Prompt del Usuario** – Contiene la solicitud específica y datos de entrada, generalmente formateados con una plantilla para guiar la salida de la IA.

## ⌨️ Actividad: Implementar la Función de Construcción de Prompt para Plan de Estudios

La función `build_study_plan_prompt` crea prompts personalizados que guían a la IA en la generación de planes de estudio relevantes. Vamos a implementarla con GitHub Copilot.

1. **Abre el archivo de prompts** en `app/services/prompts.py`. Encontrarás ejemplos de prompts y un marcador de posición para la función.

2. Vamos a completar la función `build_study_plan_prompt` usando el modo Agent. Abre el panel **Copilot Chat**, cambia al modo **Agent** y proporciona las siguientes instrucciones:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
   >
   > ```prompt
   > Completa la función `build_study_plan_prompt` para que devuelva una lista de mensajes:
   >
   > **El prompt del sistema debe incluir:**
   > - Eres un especialista en educación con más de 10 años de experiencia
   > - Siempre responde en el idioma preferido del usuario
   > - Crea planes prácticos, estructurados y realistas
   > - Incluye proyectos prácticos y recursos específicos
   >
   > **El prompt del usuario debe incluir:**
   > - Plantilla con variables: área, nivel, tiempo, duración, objetivos
   > - Solicitud para cronograma semanal detallado
   > - Solicitud para recursos específicos (cursos, libros, herramientas)
   > - Solicitud para proyectos prácticos progresivos
   > - Solicitud para hitos de evaluación mensuales
   > ```

3. Guarda los cambios y prueba con entradas de ejemplo. Por ejemplo:

   | Área          | Nivel        | Tiempo Semanal | Duración | Objetivo Específico                                |
   | ------------- | ------------ | -------------- | -------- | -------------------------------------------------- |
   | backend       | principiante | 10             | 3        | "Quiero construir APIs REST con Node.js"           |
   | frontend      | intermedio   | 15             | 4        | "Necesito dominar React y aprender Next.js"        |
   | data\_science | avanzado     | 20             | 6        | "Quiero implementar modelos de ML en producción"   |
   | fullstack     | principiante | 12             | 6        | "Quiero crear una aplicación web completa"         |
   | ai\_ml        | intermedio   | 18             | 5        | "Necesito entender deep learning para NLP"         |

Estos ejemplos prueban diferentes áreas, niveles de habilidad y objetivos, dándote una imagen clara de cómo tu sistema de prompts se adapta a varios escenarios.

---

| [← Modelos de Datos y Endpoint de API](04-step.md) | [Siguiente: Añadiendo Validación de Formulario →](06-step.md) |
|:-----------------------------------|------------------------------------------:|
