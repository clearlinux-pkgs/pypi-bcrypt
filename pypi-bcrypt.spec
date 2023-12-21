#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v3
# autospec commit: c1050fe
#
Name     : pypi-bcrypt
Version  : 4.1.2
Release  : 97
URL      : https://files.pythonhosted.org/packages/72/07/6a6f2047a9dc9d012b7b977e4041d37d078b76b44b7ee4daf331c1e6fb35/bcrypt-4.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/72/07/6a6f2047a9dc9d012b7b977e4041d37d078b76b44b7ee4daf331c1e6fb35/bcrypt-4.1.2.tar.gz
Source1  : http://localhost/cgit/vendor/pypi-bcrypt/snapshot/pypi-bcrypt-2023-12-20-23-35-46.tar.xz
Summary  : Modern password hashing for your software and your servers
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT Unicode-DFS-2016 Unlicense
Requires: pypi-bcrypt-license = %{version}-%{release}
Requires: pypi-bcrypt-python = %{version}-%{release}
Requires: pypi-bcrypt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_rust)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
BuildRequires : rustc
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
bcrypt
======
.. image:: https://img.shields.io/pypi/v/bcrypt.svg
:target: https://pypi.org/project/bcrypt/
:alt: Latest Version

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
Requires: python3-core
Provides: pypi(bcrypt)

%description python3
python3 components for the pypi-bcrypt package.


%prep
%setup -q -n bcrypt-4.1.2
cd %{_builddir}
tar xf %{_sourcedir}/pypi-bcrypt-2023-12-20-23-35-46.tar.xz
cd %{_builddir}/bcrypt-4.1.2
mkdir -p ./vendor
cp -r %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/* %{_builddir}/bcrypt-4.1.2/./vendor
mkdir -p .cargo
echo '[source.crates-io]' >> .cargo/config.toml
echo 'replace-with = "vendored-sources"' >> .cargo/config.toml
echo '[source.vendored-sources]' >> .cargo/config.toml
echo 'directory = "vendor"' >> .cargo/config.toml
pushd ..
cp -a bcrypt-4.1.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703172272
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-bcrypt
cp %{_builddir}/bcrypt-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/autocfg/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/autocfg/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/e6d32072ef5f584a805b429ecbd4eec428316dde || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/base64/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/base64/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/bcrypt-pbkdf/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/7492aeed05866a8879f4690198f778701b9f45b0 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/bcrypt-pbkdf/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/0acaab6c0e4e1633c9bdcb3aaa1ca4c285782291 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/bcrypt/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/2a334270f25a6852d9d5a3c03de644d24232be0c || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/bitflags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/bitflags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/block-buffer/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/422e6fd980775f9997ed6735c28a14ad20c222e8 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/block-buffer/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/aca18f6eebf597377e59fff1f0e6adbadcdcf97b || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/blowfish/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/422e6fd980775f9997ed6735c28a14ad20c222e8 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/blowfish/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5d0631a1d115284efc3e440446c50ef12978a5ec || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/byteorder/COPYING %{buildroot}/usr/share/package-licenses/pypi-bcrypt/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/byteorder/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/byteorder/UNLICENSE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/cfg-if/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/cfg-if/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/cipher/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/422e6fd980775f9997ed6735c28a14ad20c222e8 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/cipher/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/708e756c9120bcaf2c0a1d240b2418ee908e2d87 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/cpufeatures/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/422e6fd980775f9997ed6735c28a14ad20c222e8 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/cpufeatures/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/388871ab0ab7f8ba6aaa0d444a5153f15c918cdb || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/crypto-common/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/422e6fd980775f9997ed6735c28a14ad20c222e8 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/crypto-common/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/7ca2c807379211b3ca6b04f10723088ca423c4fe || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/digest/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/422e6fd980775f9997ed6735c28a14ad20c222e8 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/digest/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/9c6e81caeb170dd5501d39895df9efb657c3c86b || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/generic-array/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/cb74eb831db08b7fe98f84b59c9bda195e5a3588 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/getrandom/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/getrandom/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/d74ad13f1402c35008f22bc588a6b8199ed164d3 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/heck/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/heck/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/60c3522081bf15d7ac1d4c5a63de425ef253e87a || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/indoc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/indoc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/inout/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/422e6fd980775f9997ed6735c28a14ad20c222e8 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/inout/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/e03b48c8e0c3b1ab53f81d9913b997d6c82b4829 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/libc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/libc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/36d69bcb88153a640740000efe933b009420ce7e || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/lock_api/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/lock_api/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/memoffset/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/02bf11a87b9bbacedf2fcf4856af3b933faef82e || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/once_cell/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/once_cell/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/parking_lot/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/parking_lot/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/parking_lot_core/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/parking_lot_core/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pbkdf2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/422e6fd980775f9997ed6735c28a14ad20c222e8 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pbkdf2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/f792d4a36017520577d0e8d4f28d6c39fc682a4f || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pyo3-build-config/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pyo3-build-config/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pyo3-ffi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pyo3-ffi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pyo3-macros-backend/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pyo3-macros-backend/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pyo3-macros/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pyo3-macros/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pyo3/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pyo3/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pyo3/pyo3-runtime/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/pyo3/pyo3-runtime/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/959ce149b1615b8bff3437f59282396756987859 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/redox_syscall/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/a00165152c82ea55b9fc254890dc8860c25e3bb6 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/scopeguard/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/scopeguard/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/f498d95a48889a0b1432e420e6754881eff1d593 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/sha2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/422e6fd980775f9997ed6735c28a14ad20c222e8 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/sha2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/1741e5596832e62cd0791301fc9dcf4b9d0bc2c9 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/smallvec/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/smallvec/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/c61640f6c218caf86d1b8072e09668a8362dba04 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/subtle/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/145c27c874c444c902ad2af6164fcc30231fa7a8 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/target-lexicon/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/f137043e018f2024e0414a9153ea728c203ae8e5 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/typenum/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/481e4be7d70c11ee3f6e04a59a0e5afccc551db2 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/typenum/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/69facfd64b2a7aa4a22c917ef10cd96e41b75b87 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/typenum/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5984f5244c7bc13bf15a5bea823c04ec0bbc714f || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/unicode-ident/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/unicode-ident/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/unicode-ident/LICENSE-UNICODE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/583a5eebcf6119730bd96922e8a0faecf7faf720 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/unindent/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/unindent/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/version_check/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/version_check/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/cfcb552ef0afbe7ccb4128891c0de00685988a4b || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/wasi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/wasi/LICENSE-Apache-2.0_WITH_LLVM-exception %{buildroot}/usr/share/package-licenses/pypi-bcrypt/f137043e018f2024e0414a9153ea728c203ae8e5 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/wasi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows-targets/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-bcrypt/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows-targets/license-mit %{buildroot}/usr/share/package-licenses/pypi-bcrypt/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_aarch64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-bcrypt/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_aarch64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pypi-bcrypt/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_aarch64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-bcrypt/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_aarch64_msvc/license-mit %{buildroot}/usr/share/package-licenses/pypi-bcrypt/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_i686_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-bcrypt/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_i686_gnu/license-mit %{buildroot}/usr/share/package-licenses/pypi-bcrypt/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_i686_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-bcrypt/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_i686_msvc/license-mit %{buildroot}/usr/share/package-licenses/pypi-bcrypt/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_x86_64_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-bcrypt/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_x86_64_gnu/license-mit %{buildroot}/usr/share/package-licenses/pypi-bcrypt/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_x86_64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-bcrypt/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_x86_64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pypi-bcrypt/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_x86_64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-bcrypt/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/windows_x86_64_msvc/license-mit %{buildroot}/usr/share/package-licenses/pypi-bcrypt/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/zeroize/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-bcrypt/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/pypi-bcrypt-2023-12-20-23-35-46/zeroize/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-bcrypt/f24fdeaeee4c59532e32b7c6517d34c8927526fe || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-bcrypt/02bf11a87b9bbacedf2fcf4856af3b933faef82e
/usr/share/package-licenses/pypi-bcrypt/0acaab6c0e4e1633c9bdcb3aaa1ca4c285782291
/usr/share/package-licenses/pypi-bcrypt/145c27c874c444c902ad2af6164fcc30231fa7a8
/usr/share/package-licenses/pypi-bcrypt/1741e5596832e62cd0791301fc9dcf4b9d0bc2c9
/usr/share/package-licenses/pypi-bcrypt/2a334270f25a6852d9d5a3c03de644d24232be0c
/usr/share/package-licenses/pypi-bcrypt/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-bcrypt/36d69bcb88153a640740000efe933b009420ce7e
/usr/share/package-licenses/pypi-bcrypt/388871ab0ab7f8ba6aaa0d444a5153f15c918cdb
/usr/share/package-licenses/pypi-bcrypt/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/pypi-bcrypt/422e6fd980775f9997ed6735c28a14ad20c222e8
/usr/share/package-licenses/pypi-bcrypt/481e4be7d70c11ee3f6e04a59a0e5afccc551db2
/usr/share/package-licenses/pypi-bcrypt/4c8990add9180fc59efa5b0d8faf643c9709501e
/usr/share/package-licenses/pypi-bcrypt/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/pypi-bcrypt/583a5eebcf6119730bd96922e8a0faecf7faf720
/usr/share/package-licenses/pypi-bcrypt/5984f5244c7bc13bf15a5bea823c04ec0bbc714f
/usr/share/package-licenses/pypi-bcrypt/5bb5828e544f63bd76c1b7112981a1ad86ae77f9
/usr/share/package-licenses/pypi-bcrypt/5d0631a1d115284efc3e440446c50ef12978a5ec
/usr/share/package-licenses/pypi-bcrypt/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c
/usr/share/package-licenses/pypi-bcrypt/60c3522081bf15d7ac1d4c5a63de425ef253e87a
/usr/share/package-licenses/pypi-bcrypt/689ec0681815ecc32bee639c68e7740add7bd301
/usr/share/package-licenses/pypi-bcrypt/69facfd64b2a7aa4a22c917ef10cd96e41b75b87
/usr/share/package-licenses/pypi-bcrypt/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a
/usr/share/package-licenses/pypi-bcrypt/708e756c9120bcaf2c0a1d240b2418ee908e2d87
/usr/share/package-licenses/pypi-bcrypt/7492aeed05866a8879f4690198f778701b9f45b0
/usr/share/package-licenses/pypi-bcrypt/7ca2c807379211b3ca6b04f10723088ca423c4fe
/usr/share/package-licenses/pypi-bcrypt/959ce149b1615b8bff3437f59282396756987859
/usr/share/package-licenses/pypi-bcrypt/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
/usr/share/package-licenses/pypi-bcrypt/9c6e81caeb170dd5501d39895df9efb657c3c86b
/usr/share/package-licenses/pypi-bcrypt/9f3c36d2b7d381d9cf382a00166f3fbd06783636
/usr/share/package-licenses/pypi-bcrypt/a00165152c82ea55b9fc254890dc8860c25e3bb6
/usr/share/package-licenses/pypi-bcrypt/a3b3a65335e78bde163f84d599fa899776552994
/usr/share/package-licenses/pypi-bcrypt/aca18f6eebf597377e59fff1f0e6adbadcdcf97b
/usr/share/package-licenses/pypi-bcrypt/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2
/usr/share/package-licenses/pypi-bcrypt/c61640f6c218caf86d1b8072e09668a8362dba04
/usr/share/package-licenses/pypi-bcrypt/cb74eb831db08b7fe98f84b59c9bda195e5a3588
/usr/share/package-licenses/pypi-bcrypt/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/pypi-bcrypt/cfcb552ef0afbe7ccb4128891c0de00685988a4b
/usr/share/package-licenses/pypi-bcrypt/d74ad13f1402c35008f22bc588a6b8199ed164d3
/usr/share/package-licenses/pypi-bcrypt/dd445710e6e4caccc4f8a587a130eaeebe83f6f6
/usr/share/package-licenses/pypi-bcrypt/e03b48c8e0c3b1ab53f81d9913b997d6c82b4829
/usr/share/package-licenses/pypi-bcrypt/e6d32072ef5f584a805b429ecbd4eec428316dde
/usr/share/package-licenses/pypi-bcrypt/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
/usr/share/package-licenses/pypi-bcrypt/f137043e018f2024e0414a9153ea728c203ae8e5
/usr/share/package-licenses/pypi-bcrypt/f24fdeaeee4c59532e32b7c6517d34c8927526fe
/usr/share/package-licenses/pypi-bcrypt/f498d95a48889a0b1432e420e6754881eff1d593
/usr/share/package-licenses/pypi-bcrypt/f792d4a36017520577d0e8d4f28d6c39fc682a4f
/usr/share/package-licenses/pypi-bcrypt/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
