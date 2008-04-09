Summary:	Orbited is an HTTP daemon that is optimized for long-lasting comet connections
Summary(pl.UTF-8):	Orbited - demon HTTP zoptymalizowany pod kątem długotrwałych połączeń
Name:		orbited
Version:	0.3.2
Release:	2
License:	MIT
Group:		Networking/Daemons
Source0:	http://pypi.python.org/packages/source/o/orbited/%{name}-%{version}.tar.gz
# Source0-md5:	967e16235756702312101076fb67f606
URL:		http://brbx.com/orbited/index.html
BuildRequires:	libevent-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	python-pyevent
Requires:	python-rel
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orbited is an HTTP daemon that is optimized for long-lasting comet
connections. It is designed to be easily integrated with new and
existing applications. Orbited allows you to write real-time web
applications, such as a chat room or instant messaging client, without
using any external plugins like Flash or Java.

%description -l pl.UTF-8
Orbited to demon HTTP zoptymalizowany pod kątem długotrwałych połączeń
"kometowych". Jest zaprojektowany z myślą o łatwej integracji z nowymi
i istniejącymi aplikacjami. Pozwala na tworzenie aplikacji WWW
działających w czasie rzeczywistym, takie jak chaty czy komunikatory
bez wykorzystywania zewnętrznych wtyczek w stylu Flasha czy Javy.

%prep
%setup -q

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/orbited
%attr(755,root,root) %{_bindir}/orbited_daemonized
%attr(755,root,root) %{_bindir}/revolved
%{py_sitescriptdir}/orbited
%{py_sitescriptdir}/orbited-*.egg-info
