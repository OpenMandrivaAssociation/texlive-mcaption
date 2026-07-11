%global tl_name mcaption
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0
Release:	%{tl_revision}.1
Summary:	Put captions in the margin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mcaption
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcaption.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcaption.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcaption.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The mcaption package provides an mcaption environment which puts figure
or table captions in the margin. The package works with the standard
classes and with the KOMA-Script document classes scrartcl, scrreprt and
scrbook. The package requires the changepage package.

