Summary:	Class for creating esientific and business charts, works with php5
Summary(pl.UTF-8):	Klasa do tworzenia naukowych i biznesowych wykresów, działa z php5
Name:		jpgraph2
Version:	2.3.4
Release:	3
License:	QPL 1.0
Group:		Libraries
# Source0Download: http://www.aditus.nu/jpgraph/jpdownload.php
Source0:	http://hem.bredband.net/jpgraph2/jpgraph-%{version}.tar.gz
# Source0-md5:	4500906d756dc395a992866e483591ae
Patch0:		%{name}-config.patch
URL:		http://www.aditus.nu/jpgraph/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	php(gd)
Requires:	php-common >= 4:5.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{php_data_dir}/%{name}

%description
JpGraph is a fully OO graph library which makes it easy to both draw a
"quick and dirty" graph with a minimum of code and quite complex
graphs which requires a very fine grain of control. The library tries
to assign sensible default values for most parameters hence making the
learning curve quite flat since for most of the time very few commands
is required to draw graphs with a pleasing aesthetic look.

Note: The 2.x series is only for PHP5. It will not work on PHP4.

%description -l pl.UTF-8
JpGraph to w pełni obiektowo zorientowana biblioteka ułatwiająca
tworzenie zarówno prostych (,,na szybko'') jak i skomplikowanych,
wymagających precyzji grafik. Biblioteka próbuje przypisać sensowne
wartości domyślne dla większości parametrów, aby uczynić krzywą nauki
w miarę płaską, jako że w większości przypadków wystarcza użycie kilku
poleceń do rysowania estetycznie wyglądających grafik.

Uwaga: wersje 2.x są tylko dla PHP5, nie będą działać z PHP4.

%prep
%setup  -q -n jpgraph-%{version}
%patch0 -p1

%{__sed} -i -e 's#img/img/img/img/img/img/#img/#g' docs/html/*.html
%{__sed} -i -e 's#\.\./#../img/#g' docs/html/*/*.html

mv src/*.txt .
mv src/Examples .

%{__sed} -i -e 's,include ("../\(.*\)");,require_once "jpgraph2/\1";,' Examples/*.php
%{__sed} -i -e 's,include_once ("../\(.*\)");,require_once "jpgraph2/\1";,' Examples/*.php
%{__sed} -i -e 's,include "../\(.*\)";,require_once "jpgraph2/\1";,' Examples/*.php

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -a src/* $RPM_BUILD_ROOT%{_appdir}
cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* docs/* CHANGELOG*.txt
%{_appdir}
%{_examplesdir}/%{name}-%{version}
