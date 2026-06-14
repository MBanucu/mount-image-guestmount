"""Disk image mounting via guestmount / libguestfs (Linux)."""

import os
import shutil
import subprocess
import tempfile


def mount_image(image_path: str, fstype: str = 'exfat',
                options: list[str] | None = None) -> tuple[str, str]:
    """Mount *image_path* via guestmount (FUSE).

    Returns ``(mount_point, mount_point)`` — both values are the same
    since guestmount does not create a separate loop device.
    Raises ``RuntimeError`` on failure.
    """
    mount_point = tempfile.mkdtemp(prefix='mount_image_')
    cmd = ['guestmount', '-a', str(image_path), '-m', '/dev/sda']
    if options:
        for opt in options:
            cmd.extend(['-o', opt])
    else:
        cmd.extend(['-o', f'uid={os.getuid()}', '-o', f'gid={os.getgid()}'])
    cmd.append(mount_point)

    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        shutil.rmtree(mount_point, ignore_errors=True)
        raise RuntimeError(f"guestmount failed: {r.stderr.strip()}")

    return mount_point, mount_point


def umount_image(device: str, mount_point: str | None = None):
    """Unmount a FUSE filesystem."""
    mp = mount_point or device
    subprocess.run(['fusermount', '-u', mp], capture_output=True)
    if mp:
        try:
            shutil.rmtree(mp, ignore_errors=True)
        except Exception:
            pass


def attach_image(image_path: str) -> str:
    """Attach *image_path* as a block device via sudo losetup.

    Guestmount does not create loop devices, so this delegates to
    the sudo losetup strategy.
    """
    from mount_image_sudo import attach_image as _sudo_attach
    return _sudo_attach(image_path)


def detach_image(device: str):
    """Detach a block device via sudo losetup."""
    from mount_image_sudo import detach_image as _sudo_detach
    _sudo_detach(device)


def umount_inner(mount_point: str):
    """Unmount FUSE without cleanup. Used by the orchestrator."""
    subprocess.run(['fusermount', '-u', mount_point], capture_output=True)


def detach_inner(device: str):
    """No-op. Guestmount uses FUSE, no loop device to detach."""
    pass
