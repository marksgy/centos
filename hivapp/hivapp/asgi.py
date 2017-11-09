import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hivapp.settings")
channel_layer = channels.asgi.get_channel_layer()