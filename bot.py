# By @TroJanzHEX
from pyrogram import Client
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config  # pylint:disable=import-error


if __name__ == "__main__":
    plugins = dict(root="plugins")

    app = Client(
        "TroJanz",
        bot_token=Config.1950090715:AAH3rJEVIgiil00pZjvRKwXhuRTj_QoLmAE,
        api_id=Config.7744764,
        api_hash=Config.09fb2bd3ee46019e911149d4970bfc47,
        plugins=plugins,
        workers=300,
    )
    app.run()
