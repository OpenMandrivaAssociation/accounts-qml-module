Summary:	QML module to manage the user's online accounts
Name:		accounts-qml-module
Version:	0.7
Release:	1
License:	LGPLv2.1+
Group:		System/Libraries
Url:		https://gitlab.com/accounts-sso/accounts-qml-module
# https://gitlab.com/accounts-sso/accounts-qml-module/-/archive/master/accounts-qml-module-master.tar.bz2
Source0:	accounts-qml-module-master.tar.bz2
BuildRequires:	qdoc5
BuildRequires:	qt5-qtdeclarative
BuildRequires:	pkgconfig(accounts-qt5)
BuildRequires:	pkgconfig(libsignon-qt5)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Xml)
Requires:	UbuntuOnlineAccounts-qml = %{EVRD}

%description
This QML module provides an API to manage the user's online accounts and get
their authentication data. It's a tiny wrapper around the Qt-based APIs of
libaccounts-qt and libsignon-qt.

%files
%{_bindir}/tst_plugin

#----------------------------------------------------------------------------

%define qmlubuntuonlineaccounts %mklibname UbuntuOnlineAccounts-qml

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
%dir %{_qt5_prefix}/qml/Ubuntu/OnlineAccounts/
%{_qt5_prefix}/qml/Ubuntu/OnlineAccounts/*

#----------------------------------------------------------------------------

%prep
%autosetup -n %{name}-master

%build
%qmake_qt5
%make_build

%install
%make_install

# Drop docs
rm -rf %{buildroot}%{_datadir}/accounts-qml-module/doc/
