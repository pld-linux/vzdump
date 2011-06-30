#

%define 	vzdumpdate	2011-06-17
Summary:	OpenVZ backup scripts
Summary(pl.UTF-8):	Skrypty do backupu kontenerów OpenVZ
######		Unknown group!
Name:		vzdump
Version:	1.2_13
Release:	0.1
License:	GPL
Group:		Utilities
Source0:	http://download.proxmox.com/sources/%{name}_%{vzdumpdate}.tar.gz
# Source0-md5:	610c70c2fc49f48979cd8e5af2764d15
URL:		http://www.proxmox.com/
Requires:	cstream
Requires:	perl
Requires:	perl(LockFile::Simple)
Requires:	rsync
#Requires:	smtpdaemon
Requires:	vzctl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the vzdump script to backup and restore openvz
images.

%description -l pl.UTF-8
Pakiet zawiera skrypt vzdump do tworzenia i odtwarzania (vzrestore)
kopii zapasowych kontenerów openvz.

%prep
%setup -q -n %{name}_%{%{name}date}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT/%{perl_vendorlib}
mv $RPM_BUILD_ROOT%{_datadir}/perl5/PVE $RPM_BUILD_ROOT/%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/vzdump
%attr(755,root,root) %{_sbindir}/vzrestore
%{_mandir}/man1/vzdump.1.*
%{_mandir}/man1/vzrestore.1.*
%dir %{perl_vendorlib}/PVE
%dir %{perl_vendorlib}/PVE/VZDump
%{perl_vendorlib}/PVE/VZDump.pm
%{perl_vendorlib}/PVE/VZDump/Plugin.pm
%{perl_vendorlib}/PVE/VZDump/OpenVZ.pm

%defattr(644,root,root,755)
%doc hook-script.pl ChangeLog changelog.Debian copyright
