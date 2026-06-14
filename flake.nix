{
  description = "mount-image-guestmount: Disk image mounting via guestmount / libguestfs (Linux)";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    mount-image-sudo.url = "github:MBanucu/mount-image-sudo";
  };

  outputs =
    { self
    , nixpkgs
    , flake-utils
    , mount-image-sudo
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [
            mount-image-sudo.overlays.default
            self.overlays.default
          ];
        };
      in
      {
        packages.default = pkgs.python3.pkgs.mount-image-guestmount;

        devShells.default = pkgs.mkShell {
          inputsFrom = [ pkgs.python3.pkgs.mount-image-guestmount ];
          packages = [ pkgs.python3 ];
          shellHook = ''
            echo "mount-image-guestmount dev shell. Run tests:"
            echo "  python -m unittest discover -s tests -v"
          '';
        };
      }
    )
    // {
      overlays.default = final: prev: {
        mount-image-guestmount = final.python3.pkgs.callPackage ./default.nix {
          src = final.lib.cleanSource ./.;
        };
        python3 = prev.python3.override {
          packageOverrides = _: _: {
            inherit (final) mount-image-guestmount;
          };
        };
      };
    };
}
