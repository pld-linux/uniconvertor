# fix noarch (py_sitescriptdir) if really noarch or use optflags
Summary:	vector graphics translator
Summary(pl.UTF-8):	Konwerter grafiki wektorowej
Name:		uniconvertor
Version:	1.0.0
Release:	0.1
License:	LGPL
Group:		Applications/Graphics
Source0:	http://sk1project.org/downloads/uniconvertor/%{name}-%{version}.tar.gz
# Source0-md5:	e334c28f42820784d6a9445173e082a0
URL:		http://sk1project.org/modules.php?name=Products&product=uniconvertor
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
#BuildArch:	noarch ???
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UniConvertor is a universal vector graphics translator.

%description -l pl.UTF-8
UniConvertor jest uniwersalnym konwerterem grafiki wektorowej.

%prep
%setup -q -n UniConvertor-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/uniconv
%{py_sitedir}/%{name}
