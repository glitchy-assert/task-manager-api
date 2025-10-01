import subprocess


class RuffFormatter:
    command = "ruff"

    @staticmethod
    def format(path: str) -> None:
        try:
            subprocess.run(
                [RuffFormatter.command, "format", path],
                check=True,
                capture_output=True,
                text=True,
            )
            print("✓ Code formatted successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Formatting failed:\n{e.stderr}")
            return False

    @staticmethod
    def check(path: str) -> None:
        try:
            subprocess.run(
                [RuffFormatter.command, "check", path],
                check=True,
                capture_output=True,
                text=True,
            )
            print("✓ No linting issues found")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Linting issues:\n{e.stdout}")
            return False
