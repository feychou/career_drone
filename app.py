from dotenv import load_dotenv

from config import ASSETS_DIR
from ui import create_demo


def main():
    load_dotenv(override=True)
    create_demo().launch(allowed_paths=[str(ASSETS_DIR)])


if __name__ == "__main__":
    main()
