Name: bozorth          
Version: 0.1       
Release:        2%{?dist}
Summary: C library and Java wrapper around bozorth3 fingerprint matcher      

License: Booz Allen Hamilton       
Source0: %{name}-%{version}.tar.gz       

BuildRequires: cmake NBIS
Requires: java      

%description


%prep
%setup -q


%build
cmake . -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT
make
javac -d . *.java
jar cvf bozorth.jar com

%install
rm -rf $RPM_BUILD_ROOT
make install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/*
%{_libdir}/*
%doc

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%changelog
* Mon Mar 25 2013 Aaron Donovan <amdonov@gmail.com> 0.1-2
- Putting Java classes in the com.bah.biometrics package (amdonov@gmail.com)
- Merge branch 'master' of github.com:amdonov/bozorth (amdonov@gmail.com)
- Initial commit (amdonov@gmail.com)

* Sun Mar 24 2013 Aaron Donovan <amdonov@gmail.com> 0.1-1
- new package built with tito


