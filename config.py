import base64
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
CSS_PATH = BASE_DIR / "styles.css"
FONT_PATH = ASSETS_DIR / "ElectroShackle.woff"


def load_css():
    font_data = base64.b64encode(FONT_PATH.read_bytes()).decode("ascii")
    return CSS_PATH.read_text(encoding="utf-8").replace(
        "/file=assets/ElectroShackle.woff",
        f"data:font/woff;base64,{font_data}",
    )
