from subprocess import run
import shutil
import os


def build_course(base_dir, jupyter_db_path, build_dir, lite_dir, contents_dir):
    os.chdir(base_dir)

    jupyter_db_path.unlink(missing_ok=True)

    if build_dir.exists():
        shutil.rmtree(build_dir)

    cmd = [
        "uv",
        "run",
        "jupyter",
        "lite",
        "build",
        "--lite-dir",
        str(lite_dir),
        "--contents",
        str(contents_dir),
        "--output-dir",
        str(build_dir),
    ]
    run(cmd, check=True)

    source_jupyterlite_json = lite_dir / "jupyter-lite.json"
    build_lite_dir = build_dir / "lite_dir"
    build_lite_dir.mkdir()
    shutil.copy(source_jupyterlite_json, build_lite_dir / "jupyter-lite.json")
