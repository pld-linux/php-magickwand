%define     _pkgname MagickWandForPHP
%define     _modname magickwand
Summary:	ImageMagick MagickWand API bindings for PHP
Name:		php-%{_modname}
Version:	1.0.4
Release:	0.3
License:	Apache-like
Group:		Development/Languages/PHP
Source0:	http://www.magickwand.org/download/php/%{_pkgname}-%{version}.tar.bz2
# Source0-md5:	f033b200ba135fec4bb017b07707c689
URL:		http://www.magickwand.org/
BuildRequires:	ImageMagick-devel >= 6.3.1
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
Requires:	ImageMagick >= 6.3.1
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module enables PHP access to the ImageMagick MagickWand API.

%prep
%setup -q -n %{_pkgname}-%{version}

%build
phpize
%configure \
	--with-magickwand
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_extensiondir},%{php_sysconfdir}/conf.d}
install modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}

cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc README LICENSE ChangeLog AUTHOR
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/magickwand.ini
%attr(755,root,root) %{php_extensiondir}/magickwand.so
