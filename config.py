# config.py
TOKEN = ""

# ID del servidor de Discord (guild ID) donde estará el bot
GUILD_ID = 123456789012345678  # Reemplaza con el ID de tu servidor

# Configuración de API para comunicarse con el servidor de FiveM
FIVEM_SERVER_URL = "http://ip_del_servidor:30120"  # IP y puerto del servidor FiveM
FIVEM_API_TOKEN = "API_TOKEN_FIVEM"  # Token de la API del servidor FiveM si es necesario

# Roles de Discord
ROLES = {
    "admin": 987654321098765432,  # ID del rol de administrador en Discord
    "mod": 876543210987654321,    # ID del rol de moderador en Discord
    "trusted_player": 765432109876543210,  # Rol de jugador de confianza
}

# Configuración de comandos y permisos
COMMANDS_PERMISSIONS = {
    "estado_servidor": ["admin", "mod", "trusted_player"],  # Roles que pueden usar el comando /estado_servidor
    "jugadores": ["admin", "mod"],                          # Roles que pueden ver la lista de jugadores conectados
    "kick": ["admin", "mod"],                               # Roles que pueden usar el comando /kick
    "ban": ["admin"],                                       # Solo administradores pueden usar /ban
    "broadcast": ["admin"],                                 # Solo administradores pueden enviar mensajes al servidor
}

# Configuración de canales de log-*-
LOG_CHANNELS = {
    "general_log": 123456789012345678,    # Canal donde se enviarán los logs generales del bot -*-
    "admin_log": 234567890123456789,      # Canal donde se enviarán logs solo para administradores-*-
    "moderation_log": 345678901234567890, # Canal donde se registrarán las acciones de moderación
}

# Configuración de mensaje de bienvenida
WELCOME_MESSAGE = {
    "enabled": True,
    "channel_id": 456789012345678901,     # ID del canal de bienvenida
    "message": "Bienvenido al servidor, {user}! Asegúrate de leer las reglas en #reglas."
}

# Configuración avanzada de monitoreo de servidores y alertas
SERVER_MONITORING = {
    "enabled": True,                  # Activa o desactiva el monitoreo automático
    "check_interval_seconds": 300,    # Intervalo en segundos para verificar el estado del servidor
    "alert_channel_id": 567890123456789012, # Canal para enviar alertas si el servidor está caído
    "alert_roles": ["admin", "mod"],  # Roles a mencionar en caso de alerta
}

# Historial de jugadores (configuración de base de datos o archivo)
PLAYER_HISTORY = {
    "enabled": True,
    "storage_type": "database",  # Opciones: "database" o "file"
    "database_url": "sqlite:///fivem_player_history.db",  # Ruta a la base de datos
    "file_path": "./player_history.json",  # Ruta si se usa almacenamiento en archivo
}

# Configuración de idioma y mensajes personalizados
LANGUAGE = "es"  # Opciones: "es" (español), "en" (inglés), etc.
MESSAGES = {
    "server_online": "El servidor está en línea y funcionando correctamente.",
    "server_offline": "El servidor parece estar desconectado.",
    "kick_success": "El jugador ha sido expulsado exitosamente.",
    "ban_success": "El jugador ha sido baneado exitosamente.",
    "no_permission": "No tienes permiso para usar este comando.",
}

# Configuración de otros servicios externos
EXTERNAL_SERVICES = {
    "weather_api_key": "TU_API_KEY_DEL_CLIMA",  # Si se desea mostrar el clima en el servidor, por ejemplo
    "news_api_key": "TU_API_KEY_DE_NOTICIAS",   # API de noticias para obtener información relevante
}

# Configuración de desarrollo
DEBUG_MODE = True  # Activa el modo de depuración para mensajes adicionales en el log
