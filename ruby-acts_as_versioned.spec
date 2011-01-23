Summary:	Adds simple versioning to an ActiveRecord module
Summary(pl.UTF-8):	Proste wersjonowanie dla modułu ActiveRecord
Name:		ruby-acts_as_versioned
Version:	0.2.3
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/7053/acts_as_versioned-%{version}.tgz
# Source0-md5:	16350fe3521463f3820ff984a4689b72
URL:		http://ar-versioned.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.3.1
Requires:	ruby-ActiveRecord
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library adds simple versioning to an ActiveRecord module.

%description -l pl.UTF-8
Ta biblioteka dodaje proste wersjonowanie do modułu ActiveRecord.

%prep
%setup -q -n acts_as_versioned-%{version}
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/*
