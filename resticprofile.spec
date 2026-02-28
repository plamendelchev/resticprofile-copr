%global debug_package %{nil}

Name: resticprofile
Version: 0.32.0
Release: 3
License: GPLv3
Summary: Configuration profiles manager and scheduler for restic backup
Url: https://github.com/creativeprojects/%{name}
Source0: %{url}/releases/download/v%{version}/resticprofile_no_self_update_%{version}_linux_amd64.tar.gz
ExclusiveArch: x86_64

%description
Configuration profiles manager for restic backup.
resticprofile is the missing link between a configuration file and restic backup.

%prep
%autosetup -c

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Sat Feb 28 2026 Plamen Delchev <plamen.delchev> 0.32.0-3
- Revert "resticprofile.spec: Fix prep macro" (plamen.delchev@gmail.com)
- Automatic commit of package [resticprofile] minor release [0.32.0-2].
  (plamen.delchev)
- resticprofile.spec: Fix prep macro (plamen.delchev@gmail.com)

* Fri Feb 27 2026 Plamen Delchev <plamen.delchev> 0.32.0-1
- resticprofile.spec: Fix ULR (plamen.delchev@gmail.com)
- README.md: Create file (plamen.delchev@gmail.com)
- Remove tarball (plamen.delchev@gmail.com)

* Fri Feb 27 2026 Plamen Delchev <plamen.delchev> 0.32.0-0
- new package built with tito

