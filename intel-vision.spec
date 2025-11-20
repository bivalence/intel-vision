Name:           intel-vision
Summary:        Metadata package for Intel vision drivers
Version:        2025112.WW46.3_25_ptl_pv
Release:        2%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/intel/vision-drivers

BuildRequires:  systemd-rpm-macros
Provides:       intel-vision-kmod-common = %{version}
Requires:       kernel(x86-64) > 6.16.12-200
Requires:       intel-vision-kmod

BuildArch:      noarch


%description
This is the metadata package for Intel vision drivers.


%changelog
* Thu Nov 20 2025 Ben Matteson <bmatteso@us.ibm.com> - WW46.3_25_ptl_pv-2
- Update spec file

* Thu Oct 30 2025 Ben Matteson <bmatteso@us.ibm.com> - WW46.3_25_ptl_pv-1
- Update to WW46.3_25_ptl_pv
