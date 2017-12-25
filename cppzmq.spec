Summary:	CPP-ZMQ library
Summary(pl.UTF-8):	Biblioteka CPP-ZMQ
Name:		cppzmq
Version:	4.2.2
Release:	2
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/zeromq/cppzmq/releases
Source0:	https://github.com/zeromq/cppzmq/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bd809b47296e77fe9f192bd9dafd5cc3
Patch0:		%{name}-nostatic.patch
URL:		https://github.com/zeromq/cppzmq
BuildRequires:	cmake >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	zeromq-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CPP-ZMQ is the C++ interface for 0MQ library.

%description -l pl.UTF-8
CPP-ZMQ to interfejs C++ do biblioteki ØMQ.

%package devel
Summary:	CPP-ZMQ header files
Summary(pl.UTF-8):	Pliki nagłówkowe CPP-ZMQ
Group:		Development/Libraries
Requires:	zeromq-devel >= %{version}

%description devel
Header files which constitute CPP-ZMQ library.

CPP-ZMQ is the C++ interface for 0MQ library.

%description devel -l pl.UTF-8
Pliki nagłówkowe stanowiące bibliotekę CPP-ZMQ.

CPP-ZMQ to interfejs C++ do biblioteki ØMQ.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README
%{_includedir}/zmq.hpp
%{_includedir}/zmq_addon.hpp
%{_datadir}/cmake/cppzmq
