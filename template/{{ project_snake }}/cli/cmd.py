"""Console script for {{ project_snake }}."""

import sys
import click


@click.command()
def main():
    """Console script for {{ project_snake }}."""
    click.echo(
        "Replace this message by putting your code into " "{{ project_snake }}.cli.main"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
