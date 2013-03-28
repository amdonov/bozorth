Name: bozorth          
Version: 0.1       
Release:        3%{?dist}
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
* Thu Mar 28 2013 Aaron Donovan <amdonov@gmail.com> 0.1-3
- Removing executable that was added briefly for testing (amdonov@gmail.com)
- Changed the way I interact with the bozorth3 library Rather than use text-
  based x, y, theta, quality data, I pass in a struct xyt_struct sized block of
  data. This has the advantage of making templates all the same size, reduces
  load time, and makes memory interactions between Java and C easier
  (amdonov@gmail.com)

* Mon Mar 25 2013 Aaron Donovan <amdonov@gmail.com> 0.1-2
- Putting Java classes in the com.bah.biometrics package (amdonov@gmail.com)
- Merge branch 'master' of github.com:amdonov/bozorth (amdonov@gmail.com)
- Initial commit (amdonov@gmail.com)

* Sun Mar 24 2013 Aaron Donovan <amdonov@gmail.com> 0.1-1
- new package built with tito


