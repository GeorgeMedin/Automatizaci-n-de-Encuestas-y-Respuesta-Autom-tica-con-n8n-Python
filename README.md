# 📊 Automatización de Encuestas y Respuesta Automática con n8n & Python  

Este proyecto implementa un flujo en **n8n** para gestionar encuestas y responder automáticamente a clientes insatisfechos mediante un **script en Python**.  

## 🛠 Tecnologías utilizadas  
- ✅ **n8n** → Para la automatización del flujo.  
- ✅ **Python** → Para procesar respuestas y generar correos automáticos.  
- ✅ **Excel/SQL** → Para almacenar las respuestas de la encuesta.  
- ✅ **Gmail API** → Para el envío de correos de disculpa.  

## 🚀 ¿Cómo funciona?  
1. **Recepción de respuestas**: Los clientes completan una encuesta.  
2. **Almacenamiento de datos**: Las respuestas se guardan en **Excel** (con opción a SQL).  
3. **Análisis de satisfacción**: Si una respuesta indica insatisfacción, se activa un **script en Python**.  
4. **Envío de disculpas**: Se genera y envía automáticamente un correo de disculpa al cliente.  

## 📂 Contenido del repositorio  
📜 `n8n_flow.json` → Configuración del flujo en n8n.  
🐍 `process_responses.py` → Script en Python que analiza respuestas y envía correos.  
📊 `html_menssage.html` → Mensaje en html que se muestra en el correo electronico de respuesta.  

## 🔧 Configuración  
1. Instalar **n8n** y configurar el flujo con el archivo `n8n_flow.json`.  
2. Configurar las credenciales para el envío de correos en Python.  
3. Asegurar la conexión con **Excel** o **SQL** para almacenar datos.  

## 📩 Contacto  
Si tienes dudas o sugerencias, ¡contáctame o contribuye al proyecto! 🚀 https://www.linkedin.com/in/jorge-medina-rincon-5b7507237/  
