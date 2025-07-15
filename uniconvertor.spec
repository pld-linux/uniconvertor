Summary:	Vector graphics translator
Summary(pl.UTF-8):	Konwerter grafiki wektorowej
Name:		uniconvertor
Version:	1.1.5
Release:	1
License:	LGPL v2+, some plugins GPL v2+ (CCX, CDR)
Group:		Applications/Graphics
#Source0Download: http://code.google.com/p/uniconvertor/downloads/list
Source0:	http://uniconvertor.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	d1272315a58304ece2ff588834e23f72
Patch0:		%{name}-install.patch
URL:		http://sk1project.org/modules.php?name=Products&product=uniconvertor
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	python-sk1libs >= 0.9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UniConvertor is a universal vector graphics translator utilizing sK1
engine.

Supported input formats:
- CorelDRAW version 7-X3,X4 (CDR/CDT/CCX/CDRX/CMX)
- Adobe Illustrator up to version 9 (AI postscript based)
- Postscript (PS)
- Encapsulated Postscript (EPS)
- Computer Graphics Metafile (CGM)
- Windows Metafile (WMF)
- XFIG
- Scalable Vector Graphics (SVG)
- Skencil/Sketch/sK1 (SK and SK1)
- Acorn Draw (AFF)
- HPGL for cutting plotter files (PLT)
- Autocad Drawing Exchange Format (DXF)
- Design format (Tajima) (DST)
- Embroidery file format (Brother) (PES)
- Embroidery file format (Melco) (EXP)
- Design format (Pfaff home) (PCS)

Supported output formats are: AI, SVG, SK, SK1, CGM, WMF, PDF, PS and
PLT.

%description -l pl.UTF-8
UniConvertor jest uniwersalnym konwerterem grafiki wektorowej
wykorzystującym silnik sK1.

Obsługiwane formaty wejściowe:
- CorelDRAW w wersji 7-X3,X4 (CDR/CDT/CCX/CDRX/CMX)
- Adobe Illustrator do wersji 9 (AI oparte na Postscripcie)
- Postscript (PS)
- Encapsulated Postscript (EPS)
- Computer Graphics Metafile (CGM)
- Windows Metafile (WMF)
- XFIG
- Scalable Vector Graphics (SVG)
- Skencil/Sketch/sK1 (SK i SK1)
- Acorn Draw (AFF)
- HPGL dla ploterów tnących (PLT)
- Autocad Drawing Exchange Format (DXF)
- Design format (Tajima) (DST)
- Embroidery (Brother) (PES)
- Embroidery (Melco) (EXP)
- Design (Pfaff home) (PCS)

Obsługiwane formaty wyjściowe to: AI, SVG, SK, SK1, CGM, WMF, PDF, PS
oraz PLT.

%prep
%setup -q
%patch -P0 -p1

%build
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README src/COPYRIGHTS
%attr(755,root,root) %{_bindir}/uniconvertor
%dir %{py_sitedir}/uniconvertor
%{py_sitedir}/uniconvertor/__init__.py[co]
%dir %{py_sitedir}/uniconvertor/app
%{py_sitedir}/uniconvertor/app/Graphics
%{py_sitedir}/uniconvertor/app/Lib
%{py_sitedir}/uniconvertor/app/Scripting
%{py_sitedir}/uniconvertor/app/conf
%{py_sitedir}/uniconvertor/app/events
%{py_sitedir}/uniconvertor/app/io
%{py_sitedir}/uniconvertor/app/managers
%dir %{py_sitedir}/uniconvertor/app/modules
%attr(755,root,root) %{py_sitedir}/uniconvertor/app/modules/*.so
%{py_sitedir}/uniconvertor/app/scripts
%{py_sitedir}/uniconvertor/app/utils
%{py_sitedir}/uniconvertor/app/VERSION
%{py_sitedir}/uniconvertor/app/__init__.py[co]
%{py_sitedir}/uniconvertor/share
%{py_sitedir}/uniconvertor-*.egg-info
