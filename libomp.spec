Name: libomp
Version: 4.0.0
Release: 1%{?dist}
Summary: OpenMP runtime for llvm/clang

License: NCSA
URL: http://openmp.llvm.org	
Source0: http://llvm.org/releases/%{version}/openmp-%{version}.src.tar.xz

BuildRequires: cmake
BuildRequires: elfutils-libelf-devel
BuildRequires: perl
BuildRequires: perl-Data-Dumper
BuildRequires: perl-Encode

Requires: elfutils-libelf

%description
OpenMP runtime for clang.

%package devel
Summary: OpenMP header files

%description devel
OpenMP header files.

%prep
%autosetup -n openmp-%{version}.src -p1

%build
mkdir -p _build
cd _build

%cmake .. \
	-DLIBOMP_INSTALL_ALIASES=OFF \
%if 0%{?__isa_bits} == 64
	-DLIBOMP_LIBDIR_SUFFIX=64 \
%else
	-DLIBOMP_LIBDIR_SUFFIX= \
%endif

%make_build


%install
cd _build
%make_install


%files
%{_libdir}/libomp.so

%files devel
%{_includedir}/omp.h

%changelog
* Mon May 15 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-1
- Initial version.
