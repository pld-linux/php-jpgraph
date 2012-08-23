Summary:	Class for creating esientific and business charts, works with php5
Summary(pl.UTF-8):	Klasa do tworzenia naukowych i biznesowych wykresów, działa z php5
Name:		php-jpgraph
Version:	3.0.7
Release:	3
License:	QPL 1.0
Group:		Libraries
# Source0Download: http://www.aditus.nu/jpgraph/jpdownload.php
Source0:	http://hem.bredband.net/jpgraph2/jpgraph-%{version}.tar.bz2
# Source0-md5:	63acd2f8ec5ad5f7408b07d1098d5508
Patch0:		jpgraph-config.patch
URL:		http://www.aditus.nu/jpgraph/
BuildRequires:	sed >= 4.0
Requires:	php(core) >= 5.1.0
Requires:	php(gd)
Obsoletes:	jpgraph2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/jpgraph
%define		_phpdocdir	%{_docdir}/phpdoc

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

%package phpdoc
Summary:	Online manual for jpgraph
Summary(pl.UTF-8):	Dokumentacja online do jpgraph
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Documentation for jpgraph.

%description phpdoc -l pl.UTF-8
Dokumentacja do jpgraph.

%package demo
Summary:	Demo for jpgraph
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jpgraph
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description demo
Samples for jpgraph.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu jpgraph.

%prep
%setup -q -c
%patch0 -p1

# avoid 1970 in file dates
find -newer README  -o -print | xargs touch --reference %{SOURCE0}

mv src/Examples .

# rm? some test code?
mv src/contour_dev Examples

%{__sed} -i -e 's,include ("../\(.*\)");,require_once "jpgraph/\1";,' Examples/*.php
%{__sed} -i -e "s,require_once ('../\(.*\)');,require_once 'jpgraph/\1';," Examples/*.php

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a src/* $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_phpdocdir}
cp -a docportal $RPM_BUILD_ROOT%{_phpdocdir}/jpgraph

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%dir %{_appdir}
%dir %{_appdir}/lang
%{_appdir}/jpgraph.php
%{_appdir}/jpgraph_*.php
%{_appdir}/jpg-config.inc.php
%{_appdir}/gd_image.inc.php
%{_appdir}/imgdata_*.inc.php

%{_appdir}/flag_mapping
%{_appdir}/flags.dat
%{_appdir}/flags_*.dat

%lang(de) %{_appdir}/lang/de.inc.php
%lang(en) %{_appdir}/lang/en.inc.php
%{_appdir}/lang/prod.inc.php

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/*

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
