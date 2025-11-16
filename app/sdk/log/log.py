import json
import os
import socket
from datetime import datetime
from app.sdk.base import base


class Logger:
    def __init__(self, service_name=""):
        print("Logger Initial")

        base.load_env()

        self.env = os.getenv("ENV", "").lower()
        self.service = service_name
        self.host = socket.gethostname()

        self.mode, self.dest = self._detect_mode_dest()
        self.log_level = self._detect_level()

        print("Logger Initial Success")

    def _detect_mode_dest(self):
        env = self.env

        if env == "" or env == "local":
            return 2, 0
        if env == "prd":
            return 0, 0
        if env == "dev":
            return 3, 0
        return 1, 0

    def _detect_level(self):
        lv = os.getenv("LOG_LEVEL", "INFO").upper()
        if lv == "ERROR":
            return 1
        if lv == "WARNING":
            return 2
        return 3

    def _build(self, msg, key="", data=""):
        return {
            "time": datetime.utcnow().isoformat(),
            "env": self.env,
            "service": self.service,
            "host": self.host,
            "key": key,
            "message": msg,
            "data": data,
        }

    def _output(self, record):
        if self.mode in [2, 3]:
            print(record)
        else:
            print(json.dumps(record))

    def info(self, msg, key="", data=None):
        if self.log_level < 3:
            return
        record = self._build(msg, key, json.dumps(data) if data else "")
        self._output(record)

    def warn(self, msg, key="", data=None):
        if self.log_level < 2:
            return
        record = self._build(msg, key, json.dumps(data) if data else "")
        self._output(record)

    def error(self, msg, key="", data=None):
        record = self._build(msg, key, json.dumps(data) if data else "")
        self._output(record)

    def errorf(self, msg, key="", data=None):
        self.error(msg, key, data)
        raise Exception(msg)
