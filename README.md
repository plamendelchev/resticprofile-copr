# resticprofile-copr

RPM spec file and packaging configuration for [resticprofile](https://creativeprojects.github.io/resticprofile/), published via [Fedora COPR](https://copr.fedorainfracloud.org/).

## About

resticprofile is a configuration profiles manager and scheduler for [restic](https://restic.net/) backup. This
repository contains the RPM packaging files needed to build and publish resticprofile for Fedora and RHEL-compatible
distributions through the COPR build service.

## Contents

- `resticprofile.spec` - RPM spec file for building the package
- `.tito/` - Tito release management configuration

## Supported Architectures

- x86_64
- aarch64

## Building

This package is managed with [Tito](https://github.com/rpm-software-management/tito). To tag a new release:

```
tito tag
```

To build locally:

```
tito build --rpm
```

## License

GPLv3. See [LICENSE](LICENSE) for details.
