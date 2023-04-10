#
# spec file for package Koi
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           Koi
Version:        0.3
Release:        0
Summary:        Theme scheduling for the KDE Plasma Desktop
License:        LGPL-3.0-only
URL:            https://github.com/MartinVonReichenberg/Koi
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libQt5Core-devel
BuildRequires:  fdupes
# Fedora build/make dependencies:#
BuildRequires:  libQt5Core-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
# Requires KDE Plasma installed#
Requires:       patterns-kde-kde_plasma
Requires:       plasma5-desktop
Requires:       plasma5-workspace
Requires:       plasma5-integration-plugin
# Requires:       libKF5Plasma5
Requires:       desktop-file-utils

%description
Koi is a program designed to provide the KDE Plasma Desktop functionality
to automatically switch between light and dark themes. Koi is under active development,
and while it is stable enough to use daily, expect bugs. Koi is designed to be used with Plasma,
and while some features may function under different desktop environments,
they are unlikely to work and untested.

%prep
%setup

%build
cd src
%cmake
%cmake_build

%install
cd src/build
make %{?_smp_mflags}
make DESTDIR=%{buildroot} install
cd ..
%cmake_install INSTALL_ROOT=%{buildroot}
%fdupes -s %{buildroot}

%files
%{_bindir}/koi
%{_datadir}/applications/koi.desktop
%{_datadir}/icons/hicolor/scalable/apps/*
%license LICENSE
%doc README.md

%changelog

* Sun Mar 5 2023 Martin Stibor <martin.von.reichenberg@proton.me> 0.3
  - Added installable packages *(binaries)* for Debian/Ubuntu, Fedora, SUSE & Arch Linux + AppImage [Martin Stibor <martin.von.reichenberg@proton.me>] + [William F. A. Hai (baduhai) <public@baduhai.eu>]
  - Fixed to use new tray icons [William F. A. Hai (baduhai) <public@baduhai.eu>]
  - New tray icons -> **LIGHT/DARK** -> *Icons change after hoovering with mouse cursor over the tray icon* [William F. A. Hai (baduhai) <public@baduhai.eu>]
  - Autostart Koi as hidden (without popping up) [William F. A. Hai (baduhai) <public@baduhai.eu>]
  - Updated ***wm_class*** [William F. A. Hai (baduhai) <public@baduhai.eu>]
  - Fixed build failure [William F. A. Hai (baduhai) <public@baduhai.eu>]
  - Reference to *AppImage* [William F. A. Hai (baduhai) <public@baduhai.eu>]
  - Binary renamed from **Koi** -> **koi** [William F. A. Hai (baduhai) <public@baduhai.eu>]
  - Fixed indentation [Martin Stibor <martin.von.reichenberg@proton.me>]
  - Updated *README* [Martin Stibor <martin.von.reichenberg@proton.me>]
  - Version bump -> ***Decimal/Hundredth** versioning format **x.x/x.xx*** [Martin Stibor <martin.von.reichenberg@proton.me>]

- Other changes in version **0.3**/*0.2.3*:
  - Fix multiple issues when switching mode. (#64) [William F. A. Hai F. A. Hai (baduhai) <public@baduhai.eu>]
  - Add restart of krunner to refresh its theme. [William F. A. Hai (baduhai) <public@baduhai.eu>]
  - Modify the way to change plasma-style using `plasma-apply-desktoptheme`. Now it shoulds be more consistent (especially with plasma 5.26 and later versions) and the modification reduces the
    complexity of the code. [William F. A. Hai (baduhai) <public@baduhai.eu>]
  - Improve the plasma restart code for kvantum. It replaces the usage of kill with kquitapp5 to be able to wait before starting plasmashell. It may improve stability of plasma-shell restart by
    avoiding some failures due to starting plasmashell while the previous process did not finish. [William F. A. Hai (baduhai) <public@baduhai.eu>]
