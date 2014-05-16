%define upstream_name weathermap
%define __noautoreq /usr/bin/php

Name:       cacti-plugin-%{upstream_name}
Version:    0.97a
Release:    2
Summary:    Weathermap plugin for cacti

License:    GPL
Group:      Monitoring
Url:        http://www.network-weathermap.com/
Source0:    http://www.network-weathermap.com/files/php-weathermap-%{version}.zip
Requires:   cacti
BuildArch:  noarch

%description
Weathermap is a network visualisation tool, to take data you already have and
show you an overview of your network in map form.
"The map is in use by a Infrastructure team and coupled with the Cacti Thold
plugin for alert generation. The map monitors a collection of Leased,SDSL and
ADSL lines."
Support is built in for RRD, MRTG (RRD and old log-format), and tab-delimited
text files. Other sources are via plugins or external scripts.

%prep
%setup -q -n weathermap

%install

install -d -m 755 %{buildroot}%{_datadir}/cacti/plugins/weathermap
cp -ap * %{buildroot}%{_datadir}/cacti/plugins/weathermap

pushd %{buildroot}%{_datadir}/cacti/plugins/weathermap
rm -f CHANGES README COPYING
popd

%clean

%files
%doc CHANGES COPYING README
%{_datadir}/cacti/plugins/weathermap
