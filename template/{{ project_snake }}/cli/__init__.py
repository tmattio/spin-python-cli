"""Console script for {{ project_slug }}."""

import click

from . import cmd


@click.group()
def main():
    """{{ project_name }}'s web scraper"""


main.add_command(cmd.main)
