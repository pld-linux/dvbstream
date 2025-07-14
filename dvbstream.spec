Summary:	MPEG-2 streaming over LAN
Name:		dvbstream
Version:	0.8.2
Release:	2
License:	GPL v2+
Group:		Networking
Source0:	http://www.orcas.net/dvbstream/%{name}-%{version}.tar.bz2
# Source0-md5:	7d5fcc3b3ac8089eae1bc28c87ce290c
Patch0:		format-security.patch
URL:		http://www.orcas.net/dvbstream/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package can be used to broadcast program or transport stream
(entire or up to 8 PIDs) over LAN using the RTP protocol. Even though
this is enhanced version of original program, there are newer projects
based on dvbstream, like mumudvb.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install dumprtp dvbstream rtpfeed ts_filter $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TELNET *.sh
%attr(755,root,root) %{_bindir}/dumprtp
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/rtpfeed
%attr(755,root,root) %{_bindir}/ts_filter
