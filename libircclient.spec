%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define devname %mklibname -d -s ircclient

Summary:	C library to create IRC clients
Name:		libircclient
Version:	1.10
Release:	2
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.ulduzsoft.com/libircclient/
Source0:	http://downloads.sourceforge.net/libircclient/%{name}-%{version}.tar.gz
Patch0:		libircclient-1.5-include-rfc.patch
#Patch1:		libircclient-1.9-openssl-1.1.patch
#Patch2:		libircclient-1.9-buildfixes.patch
BuildRequires:	pkgconfig(openssl)

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

#----------------------------------------------------------------------------

%package -n	%{devname}
Summary:	C library to create IRC clients
Group:		Development/C
Provides:	%{name}-static-devel = %{EVRD}

%description -n	%{devname}
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

%files -n %{devname}
%doc LICENSE README Changelog THANKS
%{_libdir}/*.a
%{_includedir}/*.h

#----------------------------------------------------------------------------

%prep
%autosetup -p1
#%%autopatch -p1
mv configure.in configure.ac
autoreconf -f

%build
%configure \
	--enable-openssl \
	--enable-ipv6
%make LDFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_libdir}
cp src/%{name}.a %{buildroot}%{_libdir}/

mkdir -p %{buildroot}%{_includedir}
cp include/*.h %{buildroot}%{_includedir}

