Name:           hello
Version:        1.0
Release:        1
Summary:        A simple Hello World C program package
License:        GNUv3

%description
A simple C application compiled and packaged into an RPM via GitHub Actions.

%install
mkdir -p %{buildroot}/opt/hello
install -m 755 %{_sourcedir}/hello %{buildroot}/opt/hello/hello

%files
/opt/hello/hello
