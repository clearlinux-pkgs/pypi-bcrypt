#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : pypi-bcrypt
Version  : 3.2.2
Release  : 83
URL      : https://files.pythonhosted.org/packages/e8/36/edc85ab295ceff724506252b774155eff8a238f13730c8b13badd33ef866/bcrypt-3.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/36/edc85ab295ceff724506252b774155eff8a238f13730c8b13badd33ef866/bcrypt-3.2.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/e8/36/edc85ab295ceff724506252b774155eff8a238f13730c8b13badd33ef866/bcrypt-3.2.2.tar.gz.asc
Summary  : Modern password hashing for your software and your servers
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-bcrypt-filemap = %{version}-%{release}
Requires: pypi-bcrypt-lib = %{version}-%{release}
Requires: pypi-bcrypt-license = %{version}-%{release}
Requires: pypi-bcrypt-python = %{version}-%{release}
Requires: pypi-bcrypt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cffi)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
bcrypt
======
.. image:: https://img.shields.io/pypi/v/bcrypt.svg
:target: https://pypi.org/project/bcrypt/
:alt: Latest Version

%package filemap
Summary: filemap components for the pypi-bcrypt package.
Group: Default

%description filemap
filemap components for the pypi-bcrypt package.


%package lib
Summary: lib components for the pypi-bcrypt package.
Group: Libraries
Requires: pypi-bcrypt-license = %{version}-%{release}
Requires: pypi-bcrypt-filemap = %{version}-%{release}

%description lib
lib components for the pypi-bcrypt package.


%package license
Summary: license components for the pypi-bcrypt package.
Group: Default

%description license
license components for the pypi-bcrypt package.


%package python
Summary: python components for the pypi-bcrypt package.
Group: Default
Requires: pypi-bcrypt-python3 = %{version}-%{release}

%description python
python components for the pypi-bcrypt package.


%package python3
Summary: python3 components for the pypi-bcrypt package.
Group: Default
Requires: pypi-bcrypt-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(bcrypt)
Requires: pypi(cffi)

%description python3
python3 components for the pypi-bcrypt package.


%prep
%setup -q -n bcrypt-3.2.2
cd %{_builddir}/bcrypt-3.2.2
pushd ..
cp -a bcrypt-3.2.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656361061
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-bcrypt
cp %{_builddir}/bcrypt-3.2.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-bcrypt

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-bcrypt/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
