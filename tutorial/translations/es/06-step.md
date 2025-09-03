# Paso 6: Añadiendo Validación de Formulario

> **Resumen:**
> En este paso, utilizarás el modo Agent de GitHub Copilot para implementar la validación del formulario de Parámetros del Plan, asegurando que los usuarios completen todos los campos necesarios antes del envío.

La validación de formularios es esencial para aplicaciones web que recopilan datos de usuario. Asegura que los usuarios proporcionen la información requerida en el formato correcto, da retroalimentación inmediata sobre errores y evita que el backend reciba datos inválidos o incompletos. 

Actualmente, nuestro formulario de plan de estudios permite a los usuarios enviar sin completar todos los campos, lo que puede causar errores o planes incompletos.

## ⌨️ Actividad: Implementar Validación de Formulario con el Agente Copilot

Usemos el modo Agent de GitHub Copilot para añadir validación a nuestro formulario:

1. Abre el panel **Copilot Chat** y cambia al modo **Agent**.

2. Proporciona las siguientes instrucciones al agente:

    > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
    >
    > ```prompt
    > Modifica el código JavaScript en el archivo index.html para añadir validación al formulario de Parámetros del Plan.
    > 
    > Implementa validación JavaScript para el formulario de Parámetros del Plan en index.html con estos requisitos:
    > - Marca visualmente los campos obligatorios para guiar al usuario
    > - Impide el envío del formulario si cualquier campo obligatorio (área, nivel, tiempo semanal, duración y objetivos específicos) está vacío
    > - Muestra mensajes de error específicos para campos faltantes
    > - Resalta campos inválidos con un borde rojo
    > - Elimina el resaltado cuando un campo se corrige
    > ```

### 🧪 Prueba la Validación del Formulario

Después de implementar la validación, pruébala para asegurar que funciona como se espera:

1. Ejecuta la aplicación si no está ya en ejecución
2. Intenta hacer clic en el botón "Generar Plan de Estudios" sin rellenar ningún campo
3. Verifica que aparezcan mensajes de error para todos los campos obligatorios
4. Rellena algunos campos e intenta de nuevo para verificar que los mensajes de error persisten solo en los campos vacíos
5. Rellena todos los campos obligatorios y verifica que el formulario se envía correctamente

### 📝 Consideraciones de Implementación

Al usar el Agente GitHub Copilot para esta tarea, observa cómo:

1. Analiza la estructura HTML y JavaScript existente
2. Mantiene consistencia con el código existente
3. Implementa una solución que se integra perfectamente con el flujo existente
4. Añade retroalimentación visual para mejorar la experiencia del usuario

La validación de formularios es una excelente oportunidad para usar el modo Agent de GitHub Copilot, ya que implica entender la estructura de código existente, añadir lógica de validación y mejorar la experiencia del usuario—tareas que el Agente Copilot puede lograr eficientemente con una única instrucción clara.

---

| [← Elaboración de Prompts para IA](05-step.md) | [Siguiente: Creando Modos de Chat Personalizados para Pruebas de Accesibilidad →](07-step.md) |
|:-----------------------------------|------------------------------------------:|
