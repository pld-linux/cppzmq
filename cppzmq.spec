Summary:	CPP-ZMQ library
Summary(pl.UTF-8):	Biblioteka CPP-ZMQ
Name:		cppzmq
Version:	4.9.0
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/zeromq/cppzmq/releases
Source0:	https://github.com/zeromq/cppzmq/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	80f3400f5d6cc48cee0fe1a045d78718
URL:		https://github.com/zeromq/cppzmq
BuildRequires:	cmake >= 3.11
BuildRequires:	pkgconfig
BuildRequires:	zeromq-devel >= 4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CPP-ZMQ is the C++ interface for 0MQ library.

%description -l pl.UTF-8
CPP-ZMQ to interfejs C++ do biblioteki ØMQ.

%package devel
Summary:	CPP-ZMQ header files
Summary(pl.UTF-8):	Pliki nagłówkowe CPP-ZMQ
Group:		Development/Libraries
Requires:	zeromq-devel >= 4

%description devel
Header files which constitute CPP-ZMQ library.

CPP-ZMQ is the C++ interface for 0MQ library.

%description devel -l pl.UTF-8
Pliki nagłówkowe stanowiące bibliotekę CPP-ZMQ.

CPP-ZMQ to interfejs C++ do biblioteki ØMQ.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# use arch-independent pkg-config dir, so package can be noarch
install -d $RPM_BUILD_ROOT%{_npkgconfigdir}
%{__mv} $RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc $RPM_BUILD_ROOT%{_npkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/zmq.hpp
%{_includedir}/zmq_addon.hpp
%{_npkgconfigdir}/cppzmq.pc
%{_datadir}/cmake/cppzmq
