from pathlib import Path
from subprocess import run

BASE_DIR = Path(__file__).parent.parent
QUARTO_DIR = BASE_DIR / "quarto"
BUILD_DIR = BASE_DIR / "build"
QUARTO_BIN = "quarto"


def build_quarto_site(quarto_dir, output_dir):
    cmd = [QUARTO_BIN, "render", str(quarto_dir), "--output-dir", str(output_dir)]
    run(cmd, check=True, cwd=quarto_dir)


def check_quarto_is_installed():
    cmd = [QUARTO_BIN, "-v"]
    process = run(cmd, capture_output=True)
    if process.returncode:
        raise RuntimeError(
            'Do you have quarto (https://quarto.org/) installed? Try to run "quarto -v"'
        )


def install_quarto_live(quarto_dir):
    cmd = [QUARTO_BIN, "add", "--no-prompt", "r-wasm/quarto-live"]
    run(cmd, check=True, cwd=quarto_dir)


check_quarto_is_installed()
install_quarto_live(QUARTO_DIR)
build_quarto_site(QUARTO_DIR, BUILD_DIR)
print("You could serve the built site by running the commands:")
print(f"cd {BUILD_DIR}")
print("python -m http.server 8000 --bind 127.0.0.1")
