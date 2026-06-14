"""Unit tests for mount_image_guestmount — mocked subprocess calls."""

import unittest
from unittest.mock import patch, MagicMock


class TestGuestmountMount(unittest.TestCase):
    @patch('mount_image_guestmount.subprocess.run')
    @patch('mount_image_guestmount.tempfile.mkdtemp')
    def test_mount_image_success(self, mock_mkdtemp, mock_run):
        mock_mkdtemp.return_value = '/tmp/mp'
        mock_run.return_value = MagicMock(returncode=0, stdout='', stderr='')
        from mount_image_guestmount import mount_image
        dev, mp = mount_image('/tmp/test.img', 'vfat', None)
        self.assertEqual(dev, '/tmp/mp')
        self.assertEqual(mp, '/tmp/mp')

    @patch('mount_image_guestmount.subprocess.run')
    @patch('mount_image_guestmount.tempfile.mkdtemp')
    def test_mount_image_fails(self, mock_mkdtemp, mock_run):
        mock_mkdtemp.return_value = '/tmp/mp'
        mock_run.return_value = MagicMock(returncode=1, stderr='fail')
        from mount_image_guestmount import mount_image
        with self.assertRaises(RuntimeError) as ctx:
            mount_image('/tmp/test.img', 'vfat', None)
        self.assertIn('guestmount failed', str(ctx.exception))

    @patch('mount_image_guestmount.subprocess.run')
    @patch('mount_image_guestmount.tempfile.mkdtemp')
    def test_mount_image_custom_options(self, mock_mkdtemp, mock_run):
        mock_mkdtemp.return_value = '/tmp/mp'
        mock_run.return_value = MagicMock(returncode=0)
        from mount_image_guestmount import mount_image
        mount_image('/tmp/test.img', 'vfat', ['ro', 'noexec'])
        args = mock_run.call_args[0][0]
        self.assertIn('-o', args)
        self.assertIn('ro', args)

    @patch('mount_image_guestmount.subprocess.run')
    def test_umount_image(self, mock_run):
        from mount_image_guestmount import umount_image
        umount_image('/tmp/mp')

    @patch('mount_image_sudo.attach_image')
    def test_attach_image_delegates(self, mock_sudo_attach):
        mock_sudo_attach.return_value = '/dev/loop0'
        from mount_image_guestmount import attach_image
        dev = attach_image('/tmp/test.img')
        self.assertEqual(dev, '/dev/loop0')
        mock_sudo_attach.assert_called_once_with('/tmp/test.img')

    @patch('mount_image_sudo.detach_image')
    def test_detach_image_delegates(self, mock_sudo_detach):
        from mount_image_guestmount import detach_image
        detach_image('/dev/loop0')
        mock_sudo_detach.assert_called_once_with('/dev/loop0')
