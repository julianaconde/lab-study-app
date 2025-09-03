# Paso 7: Creando Modos de Chat Personalizados para Pruebas de Accesibilidad

> **Resumen:**
> En este paso, aprenderás cómo crear modos de chat especializados de GitHub Copilot para pruebas de accesibilidad. Implementarás un asistente personalizado que identifica problemas de accesibilidad en aplicaciones web, sugiere mejoras basadas en los estándares WCAG y ayuda a integrar verificaciones de accesibilidad en tu flujo de desarrollo. [Explora opciones avanzadas de personalización para el chat de GitHub Copilot](https://code.visualstudio.com/docs/copilot/customization/overview).

## Entendiendo los Modos de Chat Personalizados

Los modos de chat personalizados en GitHub Copilot te permiten adaptar el asistente para tareas de desarrollo especializadas. Al crear un modo dedicado a las pruebas de accesibilidad, aseguras que Copilot se enfoque exclusivamente en identificar y resolver problemas de accesibilidad en tu código.

Para construir este modo, utilizaremos el repositorio **Awesome GitHub Copilot Customizations**—una colección curada de prompts, instrucciones y modos de chat que extienden Copilot a través de lenguajes, dominios y flujos de trabajo.

Este repositorio proporciona tres recursos principales que puedes usar al definir tu modo de chat personalizado:

* **[![Awesome Prompts](https://img.shields.io/badge/Awesome-Prompts-blue?logo=githubcopilot)](https://github.com/github/awesome-copilot/blob/main/README.prompts.md)** – Prompts específicos para tareas de generación de código, documentación o resolución de problemas específicos.
* **[![Awesome Instructions](https://img.shields.io/badge/Awesome-Instructions-blue?logo=githubcopilot)](https://github.com/github/awesome-copilot/blob/main/README.instructions.md)** – Estándares de codificación y mejores prácticas para proyectos completos o archivos específicos.
* **[![Awesome Chat Modes](https://img.shields.io/badge/Awesome-Chat_Modes-blue?logo=githubcopilot)](https://github.com/github/awesome-copilot/blob/main/README.chatmodes.md)** – Personas y modos de conversación listos para usar adaptados para diferentes roles de desarrollador y contextos.

## ⌨️ Actividad: Crear un Modo de Chat de Accesibilidad Personalizado

Implementaremos el modo asistente de accesibilidad usando el [modo de Accesibilidad](https://github.com/github/awesome-copilot/blob/main/chatmodes/accesibility.chatmode.md) del repositorio GitHub.

1. **Abre Copilot Chat** haciendo clic en el icono de Copilot en la barra lateral de VS Code.

2. En el panel de Copilot Chat, selecciona **⚙️ Configure Chat** > **Modes** > **Create new custom chat mode file**. Por defecto, los archivos de modo de chat se ubican en la carpeta `.github/chatmodes`.

   <details>
      <summary>📸 Mostrar captura de pantalla</summary>
       <img src="../images/6-configure-chat-instructions.png" alt="Captura de pantalla mostrando la vista de Chat y el menú Configure Chat, resaltando el botón Configure Chat" />
   </details>

3. Nombra el modo de chat como `accessibility`. Aparecerá en la lista desplegable de modos de chat.
   
4. Una vez que el archivo `accessibility.chatmode.md` esté creado, copia su contenido del [repositorio del modo de Accesibilidad](https://github.com/github/awesome-copilot/blob/main/chatmodes/accesibility.chatmode.md) usando la opción "Copy raw file".

   <details>
      <summary>📸 Mostrar captura de pantalla</summary>
       <img src="../../images/6-copy-raw.png" alt="Captura de pantalla mostrando cómo copiar el contenido del archivo en bruto" />
   </details>

5. Abre el panel de Copilot Chat y selecciona `accessibility` en la lista desplegable de modos de chat.

   <details>
      <summary>📸 Mostrar captura de pantalla</summary>
       <img src="../../images/6-chat-mode-dropdown.png" alt="Captura de pantalla mostrando la vista de Chat, resaltando la lista desplegable de modos de chat" />
   </details>

6. Pide a Copilot que verifique tu archivo `index.html`.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
   >
   > ```prompt
   > Verifica la accesibilidad en index.html
   > ```

7. Revisa las sugerencias del asistente de chat de Accesibilidad. Usa el **modo Agent** para actualizar tu archivo `index.html` y corregir cualquier problema de accesibilidad identificado.

---

| [← Añadiendo Validación de Formulario](06-step.md) | [Siguiente: Commit y Revisión de Código con GitHub Copilot →](08-step.md) |
|:-----------------------------------|------------------------------------------:|
