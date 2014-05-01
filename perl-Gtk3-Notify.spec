%define	modname	Gtk3-Notify
%define	modver	0.01

%define perl_glib_require 1.240

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1

Summary:	Perl module for libnotify
License:	LGPLv2+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	%{modname}-%{modver}.tar.gz

BuildArch:	noarch

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Glib::Object::Introspection)
BuildRequires:	perl(Gtk3)
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::Depends) >= 0.300
BuildRequires:	perl-Glib-Object-Introspection >= 0.002
Requires:	typelib(Notify) = 0.7

%description
This module provides the Perl bindings for libnotify.

Libnotify is a library that sends desktop notifications to a notification
daemon, as defined in the Desktop Notifications spec. These notifications can
be used to inform the user about an event or display some form of information
without getting in the user's way.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make OPTIMIZE="%{optflags}"

%install
%makeinstall_std

%files
%doc COPYING Changes META.json META.yml MYMETA.yml README
%{perl_vendorlib}/Gtk3/Notify*
%{_mandir}/*/*
