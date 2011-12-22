%define develname %mklibname -d -s ircclient

Summary:	C library to create IRC clients
Name:		libircclient
Version: 	1.3
Release: 	%mkrel 1
License: 	GPLv2
Group:		System/Libraries
URL: 		http://libircclient.sourceforge.net/index.html
Source0:	%{name}-%{version}.tar.gz
Patch0:		libircclient-1.3-headers.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
libircclient is a small but powerful library that implements the client-server
IRC protocol. It is designed to be small, fast, portable and compatible to RFC
standards, and most IRC clients. libircclient features include:

 * Full multi-threading support.
 * Single threads handles all the IRC processing.
 * Support for single-threaded applications, and socket-based
   applications, which use select()
 * Synchronous and asynchronous interfaces.
 * CTCP support with optional build-in reply code.
 * Flexible DCC support, including both DCC chat, and DCC file transfer.
 * Can both initiate and react to initiated DCC.
 * Can accept or decline DCC sessions asynchronously.
 * Plain C interface and implementation (possible to use from C++ code,
   obviously)
 * Compatible with RFC 1459 and most IRC clients.
 * Good documentation and examples available.

%package -n	%{develname}
Summary:	C library to create IRC clients
Group:		Development/C
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n	%{develname}
libircclient is a small but powerful library that implements the client-server
IRC protocol. It is designed to be small, fast, portable and compatible to RFC
standards, and most IRC clients. libircclient features include:

 * Full multi-threading support.
 * Single threads handles all the IRC processing.
 * Support for single-threaded applications, and socket-based
   applications, which use select()
 * Synchronous and asynchronous interfaces.
 * CTCP support with optional build-in reply code.
 * Flexible DCC support, including both DCC chat, and DCC file transfer.
 * Can both initiate and react to initiated DCC.
 * Can accept or decline DCC sessions asynchronously.
 * Plain C interface and implementation (possible to use from C++ code,
   obviously)
 * Compatible with RFC 1459 and most IRC clients.
 * Good documentation and examples available.

%prep
%setup -q
%patch0 -p1 -b .headers

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_libdir}
%__cp src/%{name}.a %{buildroot}%{_libdir}/

%__mkdir_p %{buildroot}%{_includedir}/%{name}
%__cp include/*.h %{buildroot}%{_includedir}/%{name}/

%clean
rm -rf %{buildroot}

%files -n %{develname}
%defattr(-,root,root)
%doc LICENSE README Changelog THANKS doc/html
%{_libdir}/*.a
%{_includedir}/%{name}

