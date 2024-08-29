from pathlib import Path
from subprocess import run
import os

from build_site import build_course


def serve_course(base_dir, build_dir, lite_dir):
    os.chdir(base_dir)
    cmd = [
        "uv",
        "run",
        "jupyter",
        "lite",
        "serve",
        "--lite_dir",
        lite_dir,
        "--output-dir",
        str(build_dir),
    ]
    run(cmd, check=True)


def serve_course_with_python(build_dir):
    cmd = ["uv", "run", "python3", "-m", "http.server", "-d", str(build_dir)]
    run(cmd, check=True)


BASE_DIR = Path(__file__).parent.parent
JUPYTER_DB_PATH = BASE_DIR / ".jupyterlite.doit.db"
BUILD_DIR = BASE_DIR / "build"
LITE_DIR = BASE_DIR / "lite_dir"
CONTENTS_DIR = BASE_DIR / "contents"

build_course(BASE_DIR, JUPYTER_DB_PATH, BUILD_DIR, LITE_DIR, CONTENTS_DIR)
# serve_course(BASE_DIR, BUILD_DIR, LITE_DIR)
serve_course_with_python(BUILD_DIR)
