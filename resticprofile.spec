%global debug_package %{nil}

%ifarch x86_64
%global deb_arch amd64
%elifarch aarch64
%global deb_arch arm64
%endif

Name: resticprofile
Version: 0.32.0
Release: 0%{?dist}
License: GPLv3
Summary: Configuration profiles manager and scheduler for restic backup
Url: https://creativeprojects.github.io/%{name}/
Source0: %{url}/releases/download/v%{version}/resticprofile_no_self_update_%{version}_linux_%{deb_arch}.tar.gz
ExclusiveArch: x86_64 aarch64

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
