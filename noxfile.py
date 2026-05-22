from pathlib import Path

import nox
from nox import Session


nox.needs_version = ">=2025.5.1"  # No upper bound to keep compliance with future versions
nox.options.reuse_existing_virtualenvs = True
nox.options.error_on_missing_interpreters = True
nox.options.default_venv_backend = "uv"  # Use uv backend by default for all virtual environments

# Specify which sessions will be run (in this order) at command invocation `nox`.
# If you want to run another specific session, explicitly invoke it ; for example `nox -s dev`.
nox.options.sessions = ["dev"]

PYTHON_VERSIONS = ["3.13"]
PROJECT_ROOT = Path(__file__).parent
DATA_FOLDER = PROJECT_ROOT / "data"
TRAIN_TS_FILE = DATA_FOLDER / "DSPub237.parquet"
TRAIN_META_FILE = DATA_FOLDER / "DSPub237Metadata.parquet"
TEST_TS_FILE = DATA_FOLDER / "DSPub237_test.parquet"
TEST_META_FILE = DATA_FOLDER / "DSPub237Metadata_test.parquet"
DATASET_URL = "https://zenodo.org/records/19855612"


@nox.session(venv_backend="none")  # Use the default uv venv
def dev(session: Session) -> None:
    """Set up an environment for a developer, which can be used by an IDE.

    The virtual environment will be created under `.venv`.
    The script also checks for existence of the 4 data files.

    Usage
    -----
    > nox -s dev
    """
    # Synchronize virtual environment
    session.run("uv", "sync", "--all-extras", "--all-groups", f"--python={PYTHON_VERSIONS[-1]}", external=True)

    # Check presence of data
    DATA_FOLDER.mkdir(parents=True, exist_ok=True)
    for f in (TRAIN_TS_FILE, TRAIN_META_FILE, TEST_TS_FILE, TEST_META_FILE):
        if not f.exists():
            session.error(f"Data File not found: '{f.as_posix()}'. Please download it from {DATASET_URL}")

    # Run notebook
    # session.run("jupyter", "notebook")
