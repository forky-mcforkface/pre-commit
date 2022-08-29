from __future__ import annotations

from typing import Callable
from typing import Protocol
from typing import Sequence

from pre_commit.hook import Hook
from pre_commit.languages import conda
from pre_commit.languages import coursier
from pre_commit.languages import dart
from pre_commit.languages import docker
from pre_commit.languages import docker_image
from pre_commit.languages import dotnet
from pre_commit.languages import fail
from pre_commit.languages import golang
from pre_commit.languages import lua
from pre_commit.languages import node
from pre_commit.languages import perl
from pre_commit.languages import pygrep
from pre_commit.languages import python
from pre_commit.languages import r
from pre_commit.languages import ruby
from pre_commit.languages import rust
from pre_commit.languages import script
from pre_commit.languages import swift
from pre_commit.languages import system
from pre_commit.prefix import Prefix


class Language(Protocol):
    # Use `None` for no installation / environment
    ENVIRONMENT_DIR: str | None
    # return a value to replace `'default` for `language_version`
    get_default_version: Callable[[], str]
    # return whether the environment is healthy (or should be rebuilt)
    health_check: Callable[[Prefix, str], str | None]
    # install a repository for the given language and language_version
    install_environment: Callable[[Prefix, str, Sequence[str]], None]
    # execute a hook and return the exit code and output
    run_hook: Callable[[Hook, Sequence[str], bool], tuple[int, bytes]]


languages: dict[str, Language] = {
    'conda': conda,
    'coursier': coursier,
    'dart': dart,
    'docker': docker,
    'docker_image': docker_image,
    'dotnet': dotnet,
    'fail': fail,
    'golang': golang,
    'lua': lua,
    'node': node,
    'perl': perl,
    'pygrep': pygrep,
    'python': python,
    'r': r,
    'ruby': ruby,
    'rust': rust,
    'script': script,
    'swift': swift,
    'system': system,
    # TODO: fully deprecate `python_venv`
    'python_venv': python,
}
all_languages = sorted(languages)
