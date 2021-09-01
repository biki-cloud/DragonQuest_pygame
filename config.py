import json
import os


def get_config_json() -> dict:
    with open("config.json", 'r') as fp:
        return json.loads(fp.read())


def get_img_path(img_name) -> str:
    return os.path.abspath(os.path.join(get_config_json()["img_dir"], img_name))


CONFIG: dict = get_config_json()
SCREEN_W, SCREEN_H = CONFIG["screen"]["width"], CONFIG["screen"]["height"]
