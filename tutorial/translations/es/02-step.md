# Paso 2: Verificar tu entorno

> **Resumen:**
> En este paso, verificarás que tu entorno esté configurado correctamente ejecutando un script de prueba. El script verifica la estructura de tu aplicación, valida tu token de GitHub, prueba la conectividad con el servicio de IA y confirma que todas las dependencias estén instaladas.

El script `test_setup.py` es una herramienta de diagnóstico que realiza una serie de comprobaciones para asegurar que tu entorno esté configurado correctamente. Específicamente:

* **Verifica la estructura de la aplicación**: Confirma que todos los archivos necesarios estén presentes (por ejemplo, `app/main.py`, `app/services/github_client.py`).
* **Valida el token de GitHub**: Busca la variable `GITHUB_TOKEN` en tu archivo `.env` y asegura que esté configurada.
* **Prueba la conectividad con el servicio de IA**: Envía una solicitud de prueba al servicio de modelos de IA de GitHub usando tu token para verificar el acceso al servicio y los permisos.
* **Confirma las dependencias**: Verifica que todas las bibliotecas de Python necesarias estén instaladas.

## ⌨️ Actividad: Prueba Tu Configuración

1. Antes de ejecutar la prueba, necesitas implementar la función `check_dependencies` para verificar que todos los paquetes requeridos estén instalados. Abre el archivo `test_setup.py`, luego en el panel **Copilot Chat** y selecciona el modo **Edit**.

   <details>
      <summary>📸 Mostrar captura de pantalla</summary>
      <img src="../../images/2-edit-mode.png" alt="Captura de pantalla de la pestaña Ports" />
   </details>

2. Pide a Copilot que actualice la función:

  > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social\&logo=github%20copilot)
  >
  > ```prompt
  > Actualiza la función check_dependencies para leer los paquetes desde requirements.txt e intentar importar cada uno. Imprime "✅ Dependencias importadas correctamente" en la lista final de resultados cuando todas las dependencias estén instaladas. Si falta alguna, lista los paquetes faltantes.
  > ```

3. Revisa la implementación para asegurar que verifica correctamente todas las dependencias del archivo requirements.txt.

4. Abre tu terminal y verifica tu configuración ejecutando:

```bash
python test_setup.py
```

**Resultado esperado:**

```text
✅ Estructura de la aplicación verificada
✅ GITHUB_TOKEN encontrado
✅ Modelos de GitHub funcionando - Respuesta: OK  
✅ Dependencias importadas correctamente
🎉 ¡Configuración completa! Todo listo para ejecutar la aplicación.
```

<details>
  <summary>🤷 ¿Tienes problemas?</summary>

1. **Problemas con el token de GitHub:**

   * Asegúrate de que está copiado correctamente (sin espacios adicionales)
   * Confirma que el alcance `read:user` está habilitado
   * Usa un token clásico, no de grano fino

2. **Errores de dependencia:**

```bash
# Actualiza pip
python -m pip install --upgrade pip

# Reinstala las dependencias
pip install -r requirements.txt
```

3. **Python no encontrado localmente:**

   * Windows: Instala desde [python.org](https://python.org)
   * Asegúrate de que la versión de Python sea 3.9 o superior

</details>

---

| [← Introducción a la Aplicación StudyPlan y Configuración del Entorno](01-step.md) | [Siguiente: Backend e Integración con IA →](03-step.md) |
|:-----------------------------------|------------------------------------------:|
