Summary:	vector graphics translator
Summary(pl.UTF-8):	Konwerter grafiki wektorowej
Name:		uniconvertor
Version:	1.1.2
Release:	1
License:	LGPL v2+, some plugins GPL v2+ (CCX, CDR)
Group:		Applications/Graphics
Source0:	http://sk1project.org/downloads/uniconvertor/v1.1.2/%{name}-%{version}.tar.gz
# Source0-md5:	ff6a73c1a678286fe119f62307825d1a
Patch0:		%{name}-install.patch
URL:		http://sk1project.org/modules.php?name=Products&product=uniconvertor
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	python-PIL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UniConvertor is a universal vector graphics translator.

%description -l pl.UTF-8
UniConvertor jest uniwersalnym konwerterem grafiki wektorowej.

%prep
%setup -q -n UniConvertor-%{version}
%patch0 -p1

%build
CFLAGS="%{rpmcflags}" \
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# plugins/Filters/*.py must stay (they contain plugins info as comments)
find $RPM_BUILD_ROOT%{py_sitedir}/uniconvertor -name '*.py' | grep -v 'plugins/Filters/[^/]*\.py$' | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README src/COPYRIGHTS
%attr(755,root,root) %{_bindir}/uniconv
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
%{py_sitedir}/uniconvertor/app/plugins
%{py_sitedir}/uniconvertor/app/scripts
%{py_sitedir}/uniconvertor/app/utils
%{py_sitedir}/uniconvertor/app/VERSION
%{py_sitedir}/uniconvertor/app/__init__.py[co]
%{py_sitedir}/uniconvertor/share
%{py_sitedir}/UniConvertor-*.egg-info
