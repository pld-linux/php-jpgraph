Summary:	Class for creating esientific and business charts, works with php5
Summary(pl.UTF-8):	Klasa do tworzenia naukowych i biznesowych wykresów, działa z php5
Name:		php-jpgraph
Version:	3.0.6
Release:	2
License:	QPL 1.0
Group:		Libraries
# Source0Download: http://www.aditus.nu/jpgraph/jpdownload.php
Source0:	http://hem.bredband.net/jpgraph2/jpgraph-%{version}.tar.bz2
# Source0-md5:	7af412c576b70b65480c02f7e837fdc8
Patch0:		jpgraph-config.patch
URL:		http://www.aditus.nu/jpgraph/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	php-common >= 4:5.1.0
Requires:	php-gd
Obsoletes:	jpgraph2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{php_data_dir}/jpgraph

%description
JpGraph is a fully OO graph library which makes it easy to both draw a
"quick and dirty" graph with a minimum of code and quite complex
graphs which requires a very fine grain of control. The library tries
to assign sensible default values for most parameters hence making the
learning curve quite flat since for most of the time very few commands
is required to draw graphs with a pleasing aesthetic look.

%description -l pl.UTF-8
JpGraph to w pełni obiektowo zorientowana biblioteka ułatwiająca
tworzenie zarówno prostych (,,na szybko'') jak i skomplikowanych,
wymagających precyzji grafik. Biblioteka próbuje przypisać sensowne
wartości domyślne dla większości parametrów, aby uczynić krzywą nauki
w miarę płaską, jako że w większości przypadków wystarcza użycie kilku
poleceń do rysowania estetycznie wyglądających grafik.

%prep
%setup -q -c
%patch0 -p1

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
%doc README* docportal/*
%dir %{_appdir}
%dir %{_appdir}/lang
%{_appdir}/jpgraph.php
%{_appdir}/jpgraph_*.php
%{_appdir}/jpg-config.inc.php
%{_appdir}/flag_mapping
%{_appdir}/flags.dat
%{_appdir}/flags_*.dat
%{_appdir}/gd_image.inc.php
%{_appdir}/imgdata_*.inc.php

# rm? some test code?
%{_appdir}/contour_dev

%lang(de) %{_appdir}/lang/de.inc.php
%lang(en) %{_appdir}/lang/en.inc.php
%{_appdir}/lang/prod.inc.php
%{_examplesdir}/%{name}-%{version}
