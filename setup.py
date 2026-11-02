"""Include the CLI's adjacent runtime assets in built distributions."""
from pathlib import Path

from setuptools import setup
from setuptools.command.build_py import build_py


class BuildWithAssets(build_py):
    def run(self):
        super().run()
        root = Path(__file__).parent
        for source in [root / "config.json", *sorted((root / "prompts").glob("*.txt"))]:
            target = Path(self.build_lib) / source.relative_to(root)
            target.parent.mkdir(parents=True, exist_ok=True)
            self.copy_file(str(source), str(target))


setup(cmdclass={"build_py": BuildWithAssets})
