import os
import sys
from datetime import datetime

class Logger:
    def __init__(self, service_name=""):
        self.service = service_name
        self.log_level = self._detect_level()

    def _detect_level(self):
        lv = os.getenv("LOG_LEVEL", "INFO").upper()
        if lv == "ERROR":
            return 1
        if lv == "WARNING":
            return 2
        return 3  # INFO

    def _now(self):
        return datetime.now().strftime("%H:%M:%S")

    def _print(self, level, msg):
        print(f"[{level}][{self.service}][{self._now()}] {msg}")

    def info(self, msg, data=None):
        if self.log_level < 3:
            return

        if data is not None:
            msg = f"{msg} | {data}"

        self._print("INFO", msg)

    def warn(self, msg, data=None):
        if self.log_level < 2:
            return

        if data is not None:
            msg = f"{msg} | {data}"

        self._print("WARN", msg)

    def error(self, msg, data=None):
        if data is not None:
            msg = f"{msg} | {data}"

        self._print("ERROR", msg)

    def errorf(self, msg, err=None):
        if err:
            full = f"{msg} | {err}"
            self.error(full)
            sys.exit(1)  # dừng chương trình
        else:
            self.error(msg)
            sys.exit(1)
