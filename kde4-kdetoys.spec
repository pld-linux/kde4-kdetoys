#
%define		_state		stable
%define		orgname		kdetoys
%define		qtver		4.7.1

Summary:	Kdetoys
Summary(pl.UTF-8):	Kdetoys
Name:		kde4-kdetoys
Version:	4.5.5
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	00f5fb6d5c01b55ad63c270a0db150ec
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.84
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE toys.

%description -l pl.UTF-8
Zabawki KDE.

%package amor
Summary:	amor
Group:		X11/Applications

%description amor
On-Screen Creature.

%package kteatime
Summary:	kteatime
Group:		X11/Applications

%description kteatime
Kteatime.

%package ktux
Summary:	ktux
Group:		X11/Applications

%description ktux
Ktux.

%package kweather
Summary:	kweather
Group:		X11/Applications

%description kweather
A weather reporting panel applet.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	.. \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files amor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/amor
%{_desktopdir}/kde4/amor.desktop
%{_datadir}/apps/amor
%{_datadir}/dbus-1/interfaces/org.kde.amor.xml
%{_kdedocdir}/en/amor
%{_iconsdir}/hicolor/*x*/apps/amor.png
%{_mandir}/man6/amor.6*

%files kteatime
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kteatime
%{_desktopdir}/kde4/kteatime.desktop
%{_datadir}/apps/kteatime
%{_kdedocdir}/en/kteatime
%{_iconsdir}/hicolor/*x*/apps/kteatime.png

%files ktux
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktux
%{_datadir}/apps/ktux
%{_iconsdir}/hicolor/*x*/apps/ktux.png
%{_datadir}/kde4/services/ScreenSavers/ktux.desktop

#%files kweather
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kweatherreport
#%attr(755,root,root) %{_bindir}/kweatherservice
#%{_libdir}/kde4/kcm_weather.so
#%{_libdir}/kde4/kcm_weatherservice.so
#%{_libdir}/libkdeinit4_kweatherreport.so
#%{_datadir}/apps/kweather
#%{_datadir}/apps/kweatherservice
#%{_datadir}/dbus-1/interfaces/org.kde.kweather.kweather.xml
#%{_datadir}/dbus-1/interfaces/org.kde.kweather.service.xml
#%{_kdedocdir}/en/kweather
#%{_iconsdir}/hicolor/*x*/apps/kweather.png
#%{_datadir}/kde4/services/kcmweather.desktop
#%{_datadir}/kde4/services/kcmweatherservice.desktop
#%{_datadir}/kde4/services/kweatherservice.desktop
