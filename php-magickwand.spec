%define     _pkgname MagickWandForPHP
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	ImageMagick MagickWand API bindings for PHP
Name:		php-magickwand
Version:	1.0.4
Release:	0.1
License:	Apache-like
Group:		Development/Languages/PHP
Source0:	http://www.magickwand.org/download/php/%{_pkgname}-%{version}.tar.bz2
# Source0-md5:	f033b200ba135fec4bb017b07707c689
URL:		http://www.magickwand.org/
BuildRequires: php-devel
BuildRequires: ImageMagick-devel >= 6.3.1
Requires:	php(curl)
Requires:	php-common >= 4:5.0.0
Requires:	ImageMagick >= 6.3.1
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
install -d $RPM_BUILD_ROOT%{extensionsdir}
install modules/magickwand.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE ChangeLog AUTHOR
%attr(755,root,root) %{extensionsdir}/magickwand.so
