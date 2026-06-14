# mount-image-guestmount — AGENTS.md

## Project

Disk image mounting via guestmount / libguestfs (Linux).

- **Package**: `mount-image-guestmount` (PyPI), `mount_image_guestmount` (import)
- **Repo**: `https://github.com/MBanucu/mount-image-guestmount`
- **Python**: `>=3.10`
- **License**: GPL-3.0-only
- **Depends on**: `mount-image-sudo` (for attach/detach)

## Commands

```bash
pip install -e .
python -m unittest discover -s tests -v
pip install coverage
python -m coverage run -m unittest discover -s tests -v
python -m coverage report --fail-under=70 --skip-covered
```

## Module structure

```
mount_image_guestmount/
  __init__.py    — public API (mount via guestmount, attach via sudo)
tests/
  test_mount_image_guestmount.py
```
