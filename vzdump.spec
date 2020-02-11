%define 	reldate	2011-09-13
%define 	subver	15
%define		rel		1
Summary:	OpenVZ backup scripts
Summary(pl.UTF-8):	Skrypty do backupu kontenerów OpenVZ
Name:		vzdump
Version:	1.2
Release:	0.%{subver}.%{rel}
License:	GPL v2
Group:		Applications/System
#Source0:	http://ftp.debian.org/debian/pool/main/v/vzdump/%{name}_%{version}.orig.tar.gz
Source0:	http://download.proxmox.com/sources/%{name}_%{reldate}.tar.gz
# Source0-md5:	efed9fc7b6851cbd4537627bc8c715b0
URL:		http://www.proxmox.com/cms_proxmox/en/virtualization/openvz/vzdump/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	cstream
Requires:	rsync
Requires:	smtpdaemon
Requires:	vzctl
Suggests:	xdelta
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the vzdump script to backup and restore openvz
images.

%description -l pl.UTF-8
Pakiet zawiera skrypt vzdump do tworzenia i odtwarzania (vzrestore)
kopii zapasowych kontenerów openvz.

%prep
%setup -q -n %{name}_%{reldate}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PERLLIBDIR=%{perl_vendorlib}/PVE \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO changelog.Debian
%doc hook-script.pl
%attr(755,root,root) %{_sbindir}/vzdump
%attr(755,root,root) %{_sbindir}/vzrestore
%{_mandir}/man1/vzdump.1*
%{_mandir}/man1/vzrestore.1*
%dir %{perl_vendorlib}/PVE
%{perl_vendorlib}/PVE/VZDump.pm
%dir %{perl_vendorlib}/PVE/VZDump
%{perl_vendorlib}/PVE/VZDump/Plugin.pm
%{perl_vendorlib}/PVE/VZDump/OpenVZ.pm
