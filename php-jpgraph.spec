Summary:	Class for creating esientific and business charts, works with php5
Summary(pl):	Klasa do tworzenia naukowych i biznesowych wykresów, dzia³a z php5
Name:		jpgraph2
Version:	2.0
Release:	2
License:	QPL
Group:		Libraries
#Source0Download: http://www.aditus.nu/jpgraph/jpdownload.php
Source0:	http://members.chello.se/jpgraph/jpgdownloads/jpgraph-%{version}.tar.gz
# Source0-md5:	343c355a5c50cdbae49706cba20083ea
Patch0:		%{name}-config.patch
URL:		http://www.aditus.nu/jpgraph/
BuildRequires:	unzip
Requires:	%{_datadir}/fonts/TTF
Requires:	php(gd)
Requires:	php-common >= 4:5.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpsharedir	%{_datadir}/php

%description
JpGraph is a fully OO graph library which makes it easy to both draw a
"quick and dirty" graph with a minimum of code and quite complex
graphs which requires a very fine grain of control. The library tries
to assign sensible default values for most parameters hence making the
learning curve quite flat since for most of the time very few commands
is required to draw graphs with a pleasing aesthetic look.

Note: The 2.x series is only for PHP5. It will not work on PHP4.

%description -l pl
JpGraph to w pe³ni obiektowo zorientowana biblioteka u³atwiaj±ca
tworzenie zarówno prostych (,,na szybko'') jak i skomplikowanych,
wymagaj±cych precyzji grafik. Biblioteka próbuje przypisaæ sensowne
warto¶ci domy¶lne dla wiêkszo¶ci parametrów, aby uczyniæ krzyw± nauki
w miarê p³ask±, jako ¿e w wiêkszo¶ci przypadków wystarcza u¿ycie kilku
poleceñ do rysowania estetycznie wygl±daj±cych grafik.

Uwaga: wersje 2.x s± tylko dla PHP5, nie bêd± dzia³aæ z PHP4.

%prep
%setup  -q -n jpgraph-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

install src/*.*		$RPM_BUILD_ROOT%{_phpsharedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* docs/*
%{_phpsharedir}/%{name}
