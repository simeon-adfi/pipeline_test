Name:           hello
Version:        1.0
Release:        1%{?dist}
Summary:        A simple Hello World C program package
License:        GNUv3
Source0:	hello-%{version}.tar.gz

%description
A simple C application compiled and packaged into an RPM via GitHub Actions.

%prep
%setup

%build
make

%install
mkdir -p %{buildroot}/opt/hello
install -m 755 hello %{buildroot}/opt/hello/hello

%files
/opt/hello/hello
