{
  lib
, buildPythonPackage
, setuptools
, mount-image-sudo
, src
}:
buildPythonPackage rec {
  pname = "mount-image-guestmount";
  version = "0.1.0";
  pyproject = true;

  inherit src;

  nativeBuildInputs = [ setuptools ];
  propagatedBuildInputs = [ mount-image-sudo ];

  doCheck = false;
  pythonImportsCheck = [ "mount_image_guestmount" ];

  meta = with lib; {
    description = "Disk image mounting via guestmount / libguestfs (Linux)";
    homepage = "https://github.com/MBanucu/mount-image-guestmount";
    license = licenses.gpl3Only;
    maintainers = with maintainers; [ ];
  };
}
