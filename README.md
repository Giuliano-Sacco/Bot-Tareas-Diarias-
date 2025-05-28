# Bot-Tareas-Diarias-
# 🤖 Bot de Tareas Diarias Automatizadas

Este proyecto es un bot hecho en **Python** que automatiza tareas comunes del día a día, como revisar correos, guardar adjuntos y notificarte de acciones importantes.

---

## 🛠️ ¿Qué hace este bot?

✅ Conectarse automáticamente a tu cuenta de Gmail  
✅ Revisar los correos nuevos no leídos  
✅ Descargar y guardar archivos adjuntos organizados por fecha  
✅ Crear carpetas automáticamente según el día  
✅ (Próximamente) Enviar notificación a Telegram o WhatsApp cuando se guarden archivos  
✅ (Próximamente) Ejecutarse todos los días de forma automática (cron job o script programado)

---

## 📦 Tecnologías usadas

- Python 3
- IMAP (para acceder al correo)
- Módulo `email` de Python
- `os` y `datetime` para manejo de archivos y carpetas
- (Más adelante) Telegram Bot API o Selenium para notificación

---

## 🧠 ¿Para qué sirve?

Este bot es útil para:
- Profesionales que reciben muchos archivos por mail
- Automatizar tareas repetitivas
- Independientes que quieren mantener organizado su escritorio
- Ejemplo de automatización real con Python

---


---

## ⚙️ Cómo usarlo

1. Cloná el repositorio  
2. Activá el acceso IMAP en tu cuenta de Gmail  
3. Creá una contraseña de aplicación  
4. Configurá tu correo y contraseña en el archivo `bot.py`  
5. Ejecutá el script:

```bash
python bot.py

🚀 Próximas mejoras (roadmap)

Agregar notificación por Telegram

Versión con interfaz web (Flask)

Automatización con cron job o tarea programada

    Versión dockerizada

👨‍💻 Autor

Desarrollado por Giuliano Sacco
Ingeniería en Computación y Economía | Backend Developer
📄 Licencia

MIT License – libre para usar, modificar y compartir
