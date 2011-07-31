# TODO
# - system locale dir
%define		status		stable
%define		pearname	Horde_Rpc
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde RPC API
Name:		php-horde-Horde_Rpc
Version:	1.0.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	1773f8a624a42d4bed937fe5015cc91b
URL:		https://github.com/horde/horde/tree/master/framework/Rpc/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_ActiveSync < 2.0.0
Requires:	php-horde-Horde_Core < 2.0.0
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Lock < 2.0.0
Requires:	php-horde-Horde_Perms < 2.0.0
Requires:	php-horde-Horde_Serialize < 2.0.0
Requires:	php-horde-Horde_Support < 2.0.0
Requires:	php-horde-Horde_SyncMl < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-horde-Horde_Xml_Element < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-horde-Horde_Http
Suggests:	php-pear-PEAR
Suggests:	php-soap
Suggests:	php-xmlrpc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Http.*) pear(PEAR.*)

%description
The Horde_Rpc library provides a common abstracted interface to
various remote methods of accessing Horde functionality.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%doc docs/Horde_Rpc/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Rpc.php
%{php_pear_dir}/Horde/Rpc
%{php_pear_dir}/data/Horde_Rpc
