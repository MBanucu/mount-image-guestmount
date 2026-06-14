# mount-image-guestmount

Disk image mounting via guestmount / libguestfs (Linux).

[![PyPI version](https://img.shields.io/pypi/v/mount-image-guestmount)](https://pypi.org/project/mount-image-guestmount/)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://www.python.org/)
[![License](https://img.shields.io/github/license/MBanucu/mount-image-guestmount)](LICENSE)
[![OS](https://img.shields.io/badge/OS-Linux-blue)](https://github.com/MBanucu/mount-image-guestmount)

[![CI](https://img.shields.io/github/actions/workflow/status/MBanucu/mount-image-guestmount/test.yml?branch=main)](https://github.com/MBanucu/mount-image-guestmount/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/MBanucu/mount-image-guestmount/branch/main/graph/badge.svg)](https://codecov.io/gh/MBanucu/mount-image-guestmount)

## Quick start

```python
from mount_image_guestmount import mount_image, umount_image

device, mount_point = mount_image('/path/to/disk.img')
print(f'Mounted at {mount_point}')
umount_image(device, mount_point)
```

## API

- `mount_image(path, fstype='exfat', options=None)` → `(mount_point, mount_point)`
- `umount_image(mount_point, mount_point=None)`
- `attach_image(path)` → `device` (delegates to mount-image-sudo)
- `detach_image(device)` (delegates to mount-image-sudo)

## License

GPL-3.0-only
