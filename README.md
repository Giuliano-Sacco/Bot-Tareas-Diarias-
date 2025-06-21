# 🤖 Bot-Tareas-Diarias

Un bot en Python que automatiza tareas comunes del día a día, como revisar correos, guardar adjuntos y notificarte sobre acciones importantes.

---

## 🛠️ ¿Qué hace este bot?

- ✅ Se conecta automáticamente a tu cuenta de Gmail
- ✅ Revisa los correos nuevos no leídos
- ✅ Descarga y guarda archivos adjuntos organizados por fecha
- ✅ Crea carpetas automáticamente según el día
- 🕐 (Próximamente) Envía notificaciones a Telegram o WhatsApp cuando se guardan archivos
- 🕐 (Próximamente) Se ejecuta todos los días automáticamente (cron job o script programado)

---

## 📦 Tecnologías usadas

- Python 3
- IMAP (para acceder al correo)
- Módulo `email` de Python
- `os` y `datetime` para manejo de archivos y carpetas
- (Futuro) Telegram Bot API o Selenium para notificación

---

## 🧠 ¿Para qué sirve?

Ideal para:

- Profesionales que reciben muchos archivos por mail
- Automatizar tareas repetitivas
- Autónomos que quieren mantener organizado su escritorio
- Mostrar un ejemplo de automatización real con Python

---

## ⚙️ Cómo usarlo

1. Cloná este repositorio:
   ```bash
   git clone https://github.com/Giuliano-Sacco/Bot-Tareas-Diarias-.git

    Activá el acceso IMAP en tu cuenta de Gmail

    Creá una contraseña de aplicación en tu cuenta de Google

    Configurá tu correo y contraseña en bot.py

    Ejecutá el script:

    python bot.py

🚀 Próximas mejoras (Roadmap)

Notificación por Telegram

Interfaz web (Flask)

Ejecución automática diaria (cron o tarea programada)

    Versión dockerizada

👨‍💻 Autor

Giuliano Sacco
Estudiante de Ingeniería en Computación y Economía | Backend Developer
📄 Licencia

MIT License – Libre para usar, modificar y compartir.
