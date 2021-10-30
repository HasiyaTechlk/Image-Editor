# By @TroJanzHEX


import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("1950090715:AAH3rJEVIgiil00pZjvRKwXhuRTj_QoLmAE", "")

    APP_ID = int(os.environ.get("7744764", 12345))

    API_HASH = os.environ.get("09fb2bd3ee46019e911149d4970bfc47", "")

    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("5LEW2zTFPxDbLws22GeCii4F", "")
