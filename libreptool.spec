#
Summary:	Library for reporting
Name:		libreptool
Version:	0.0.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/reptool/%{name}-%{version}.tar.gz
# Source0-md5:	b12314049c3094a8d1833cdfe45fb7fd
URL:		http://sourceforge.net/projects/reptool/
BuildRequires:	gtk-doc
BuildRequires:	libgda-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reptool is a reporting/printing tool. libreptool, which manage source
files that are the report's definition, and it produces the
report/print; and greptool, which visually creates source files. It is
based on glib, libxml, Gtk+, cairo, pango, libgda.

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
%attr(755,root,root) %{_libdir}/*.so.*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libreptool

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
