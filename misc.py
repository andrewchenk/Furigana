import os

import aqt

SUPPORT_DIR = os.path.join(os.path.dirname(__file__), "support")
ANKI21_VERSION = int(aqt.appVersion.split('.')[-1])
config = aqt.mw.addonManager.getConfig(__name__)
