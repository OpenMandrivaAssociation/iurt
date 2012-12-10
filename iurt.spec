############################################
# Warning
#   This package must be handled 
#   via /svn/soft/build_system/iurt/trunk/
############################################

%define name iurt
%define release %mkrel 1

Name: %{name}
Version: 0.6.5
Release: %{release}
License: GPL
Summary: Packages rebuilder
Group: Development/Other
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/build_system/iurt/trunk/
Source: %{name}.tar.xz
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: mkcd
BuildArch: noarch

%description
iurt is a collection of tools to create an automatic rebuild system. It contains
the rebuild script, iurt, as well as the scheduler, ulri, and the upload script, 
emi.

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/emi
%{_bindir}/iurt
%{_bindir}/ulri
%{_sbindir}/iurt_root_command
%{perl_vendorlib}/Iurt



%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.6.5-1mdv2012.0
+ Revision: 749051
- update tarball and spec for version 0.6.5
- update tarball and spec for version 0.6.5
- update tarball and spec for version 0.6.5
- update tarball and spec for version 0.6.5
- update tarball and spec for version 0.6.5
- update tarball and spec for version 0.6.5
- Rework to use make targets to commit and submit package.

* Wed Apr 20 2011 Antoine Ginies <aginies@mandriva.com> 0.6.4-6.r272332.3
+ Revision: 656210
- fix %%setup
- update tarball to latest release
- release r272332
- update tarball and spec for version 0.6.4

* Thu Mar 24 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 0.6.4-6.r272097.2
+ Revision: 648345
- Updated package to r272097

* Sun Jan 09 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.4-6.r271421.2mdv2011.0
+ Revision: 630773
- merge rpm5 branch

* Sun Oct 31 2010 Olivier Blin <blino@mandriva.org> 0.6.4-6.r271258.1mdv2011.0
+ Revision: 591265
- update to svn snapshot r271258

* Sat Mar 06 2010 Pascal Terjan <pterjan@mandriva.org> 0.6.4-6.r265102.1mdv2011.0
+ Revision: 514906
- Update to latest svn

  + Sandro Cazzaniga <kharec@mandriva.org>
    - clean spec file

* Tue Dec 01 2009 Pascal Terjan <pterjan@mandriva.org> 0.6.4-6.r259002.1mdv2010.1
+ Revision: 472297
- Update to current svn

* Sun Oct 04 2009 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-6mdv2010.0
+ Revision: 453520
- fix group
- use newer code than from 2006-12-07 (svn)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild
    - fix description-line-too-long
    - kill re-definition of %%buildroot on Pixel's request

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Thu Dec 07 2006 Warly <warly@mandriva.com> 0.6.4-1mdv2007.0
+ Revision: 91988
- update tarball and spec for version 0.6.4
- update tarball and spec for version 0.6.4

* Wed Dec 06 2006 Warly <warly@mandriva.com> 0.6.3-1mdv2007.1
+ Revision: 91771
- update tarball and spec for version 0.6.3
- update tarball and spec for version 0.6.3
- update tarball and spec for version 0.6.3
- update tarball and spec for version 0.6.3

* Wed Dec 06 2006 Warly <warly@mandriva.com> 0.6.2-1mdv2007.1
+ Revision: 91724
- update tarball and spec for version 0.6.2
- update tarball and spec for version 0.6.2
- Update package SPEC for version 0.6.2
- Remove previously copied spec to replace it for 0.6.2
- Update package SPEC for version 0.6.2
- Create iurt

