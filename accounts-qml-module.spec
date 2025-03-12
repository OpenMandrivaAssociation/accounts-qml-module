%bcond_without qt5
%bcond_without qt6

%define qmlubuntuonlineaccounts %mklibname UbuntuOnlineAccounts-qml
%define qmlssoaccounts %mklibname SSOAccounts-qml

Summary:	QML module to manage the user's online accounts
Name:		accounts-qml-module
Version:	0.8~20250312
Release:	1
License:	LGPLv2.1+
Group:		System/Libraries
Url:		https://gitlab.com/accounts-sso/accounts-qml-module
Source0:	https://gitlab.com/accounts-sso/accounts-qml-module/-/archive/master/accounts-qml-module-master.tar.bz2
%if %{with qt5}
BuildRequires:	qdoc5
BuildRequires:	qmake5
BuildRequires:	qt5-qtdeclarative
BuildRequires:	pkgconfig(accounts-qt5)
BuildRequires:	pkgconfig(libsignon-qt5)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Xml)
Requires:	%{qmlubuntuonlineaccounts} = %{EVRD}
%endif
%if %{with qt6}
BuildRequires:	qt6-qttools-doc
BuildRequires:	qmake-qt6
BuildRequires:	qt6-qtdeclarative
BuildRequires:	pkgconfig(accounts-qt6)
BuildRequires:	pkgconfig(libsignon-qt6)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Xml)
Requires:	%{qmlssoaccounts} = %{EVRD}
%endif

%description
This QML module provides an API to manage the user's online accounts and get
their authentication data. It's a tiny wrapper around the Qt-based APIs of
libaccounts-qt and libsignon-qt.

%files
%{_bindir}/tst_plugin

#----------------------------------------------------------------------------

%if %{with qt5}
%package -n %{qmlubuntuonlineaccounts}
Summary:	QML module to manage the user's online accounts
Group:		System/Libraries
Provides:	ubuntuonlineaccounts-qml = %{EVRD}
Provides:	UbuntuOnlineAccounts-qml = %{EVRD}

%description -n %{qmlubuntuonlineaccounts}
This QML module provides an API to manage the user's online accounts and get
their authentication data. It's a tiny wrapper around the Qt-based APIs of
libaccounts-qt and libsignon-qt.

%files -n %{qmlubuntuonlineaccounts}
%{_qt5_libdir}/qt5/qml/SSO
%endif

#----------------------------------------------------------------------------

%if %{with qt6}
%package -n %{qmlssoaccounts}
Summary:	QML module to manage the user's online accounts
Group:		System/Libraries

%description -n %{qmlssoaccounts}
This QML module provides an API to manage the user's online accounts and get
their authentication data. It's a tiny wrapper around the Qt-based APIs of
libaccounts-qt and libsignon-qt.

%files -n %{qmlssoaccounts}
%{_qtdir}/qml/SSO
%endif

#----------------------------------------------------------------------------

%prep
%autosetup -n %{name}-master
%if %{with qt5}
mkdir qt5
cp -a $(ls |grep -v qt5) qt5/
%endif

%build
%if %{with qt5}
cd qt5
%qmake_qt5
%make_build
cd ..
%endif

%if %{with qt6}
%{_qtdir}/bin/qmake
%make_build
%endif

%install
%if %{with qt5}
cd qt5
%make_install INSTALL_ROOT=%{buildroot}
cd ..
%endif

%if %{with qt6}
%make_install INSTALL_ROOT=%{buildroot}
%endif

# Drop docs
rm -rf %{buildroot}%{_datadir}/accounts-qml-module/doc/
