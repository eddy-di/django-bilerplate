from pathlib import Path

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create a structured subapp inside a Django app."

    def add_arguments(self, parser):
        parser.add_argument(
            "name",
            type=str,
            help="Name of the subapp to create.",
        )
        parser.add_argument(
            "inside",
            type=str,
            help="Name of the app where sub app has to be created.",
        )

    def handle(self, *args, **options):
        name = options["name"]
        inside = options['inside']

        ROOT = Path.cwd()
        APPS = ROOT / "apps"

        if not name.isidentifier():
            raise CommandError(
                f"Invalid subapp name: {name!r}. "
                "Use a valid Python identifier."
            )

        def list_folders(base: Path) -> list[str]:
            """Return sorted names of the immediate subfolders of `base`."""
            return sorted(p.name for p in base.iterdir() if p.is_dir())

        def get_app_path(name: str) -> Path:
            """Return the path to `apps/<name>`, or raise if it does not exist."""
            target = APPS / name
            target.mkdir(parents=True, exist_ok=True)
            return target

        def get_or_create_subapp_folder(parent_folder: str, sub_app: str) -> Path:
            target = parent_folder / sub_app
            if target.exists():
                available = ", ".join(list_folders(parent_folder))
                raise CommandError(
                    f"'{sub_app}' not found. Available: {available}")
            return target

        app_path = get_app_path(inside)

        sub_app_path = get_or_create_subapp_folder(app_path, name)

        directories = [
            sub_app_path,
            sub_app_path / "services",
            sub_app_path / "repositories",
            sub_app_path / "tests",
        ]

        files = [
            sub_app_path / "__init__.py",
            sub_app_path / "admin.py",
            sub_app_path / "models.py",
            sub_app_path / "serializers.py",
            sub_app_path / "urls.py",
            sub_app_path / "views.py",

            sub_app_path / "services" / "__init__.py",
            sub_app_path / "repositories" / "__init__.py",
            sub_app_path / "tests" / "__init__.py",
        ]

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)

        for file_path in files:
            file_path.touch()

        self.stdout.write(
            self.style.SUCCESS(
                f"Subapp '{name}' created successfully at {app_path}"
            )
        )
