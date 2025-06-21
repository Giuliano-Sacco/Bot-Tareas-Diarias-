import imaplib
import email
from email.header import decode_header
import os
import datetime

# ⚙️ CONFIGURACIÓN
USUARIO = "tucorreo@gmail.com"
CONTRASENA = "tu_contraseña_app"  # Generada en Google -> Seguridad -> Contraseñas de aplicaciones
IMAP_SERVER = "imap.gmail.com"
CARPETA_DESTINO = "descargas_adjuntos"

# 📁 Crear carpeta principal si no existe
if not os.path.exists(CARPETA_DESTINO):
    os.makedirs(CARPETA_DESTINO)

# 📬 Conectar a Gmail vía IMAP
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(USUARIO, CONTRASENA)
mail.select("inbox")

# 🔎 Buscar correos no leídos
status, mensajes = mail.search(None, 'UNSEEN')
mensajes = mensajes[0].split()

print(f"🔍 Correos no leídos encontrados: {len(mensajes)}")

# 📥 Procesar cada correo
for num in mensajes:
    _, data = mail.fetch(num, "(RFC822)")
    for response_part in data:
        if isinstance(response_part, tuple):
            # Obtener el mensaje
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")
            from_ = msg.get("From")

            # Obtener fecha del correo
            fecha_raw = msg.get("Date")
            try:
                fecha = email.utils.parsedate_to_datetime(fecha_raw)
            except:
                fecha = datetime.datetime.now()
            fecha_str = fecha.strftime("%Y-%m-%d")

            print(f"\n📨 Asunto: {subject}")
            print(f"📅 Fecha: {fecha_str}")
            print(f"👤 De: {from_}")

            # Crear carpeta por fecha
            carpeta_dia = os.path.join(CARPETA_DESTINO, fecha_str)
            if not os.path.exists(carpeta_dia):
                os.makedirs(carpeta_dia)

            # 🗂️ Descargar adjuntos
            for part in msg.walk():
                content_disposition = str(part.get("Content-Disposition"))
                if part.get_content_maintype() == "multipart":
                    continue
                if "attachment" in content_disposition:
                    nombre_archivo = part.get_filename()
                    if nombre_archivo:
                        nombre_archivo, enc = decode_header(nombre_archivo)[0]
                        if isinstance(nombre_archivo, bytes):
                            nombre_archivo = nombre_archivo.decode(enc if enc else "utf-8")
                        ruta = os.path.join(carpeta_dia, nombre_archivo)
                        with open(ruta, "wb") as f:
                            f.write(part.get_payload(decode=True))
                        print(f"✅ Archivo guardado: {ruta}")

# 🔒 Cerrar sesión
mail.logout()
print("\n🏁 Fin del proceso.")

