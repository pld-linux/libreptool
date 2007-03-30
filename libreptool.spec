Summary:	Library for reporting
Summary(pl.UTF-8):	Biblioteka do raportowania
Name:		libreptool
Version:	0.0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/reptool/%{name}-%{version}.tar.gz
# Source0-md5:	b12314049c3094a8d1833cdfe45fb7fd
URL:		http://sourceforge.net/projects/reptool/
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gtk-doc
BuildRequires:	libgda-devel >= 1.2.3
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	pango-devel >= 1.12
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reptool is a reporting/printing tool based on libreptool, which manage
source files that are the report's definition, and it produces the
report/print.

%description -l pl.UTF-8
reptool to narzędzie do raportowania/drukowania oparte na bibliotece
libreptool, zarządzającej plikami źródłowymi będącymi definicją
raportu i tworzącej raport/wydruk.

%package apidocs
Summary:	libreptool API documentation
Summary(pl.UTF-8):	Dokumentacja API libreptool
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libreptool API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libreptool.

%package devel
Summary:	Header files for libreptool library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libreptool
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.0.0
Requires:	glib2-devel >= 1:2.6.0
Requires:	libgda-devel >= 1.2.3
Requires:	libxml2-devel >= 1:2.6.0
Requires:	pango-devel >= 1.12

%description devel
Header files for libreptool library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libreptool.

%package static
Summary:	Static libreptool library
Summary(pl.UTF-8):	Statyczna biblioteka libreptool
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libreptool library.

%description static -l pl.UTF-8
Statyczna biblioteka libreptool.

%prep
%setup -q

%build
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libreptool

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
