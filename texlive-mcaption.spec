# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mcaption
# catalog-date 2009-03-14 02:18:31 +0100
# catalog-license lppl
# catalog-version 3.0
Name:		texlive-mcaption
Version:	3.0
Release:	1
Summary:	Put captions in the margin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mcaption
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcaption.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcaption.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcaption.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The mcaption package provides an mcaption environment which
puts figure or table captions in the margin. The package works
with the standard classes and with the KOMA-Script document
classes scrartcl, scrreprt and scrbook. The package requires
the changepage package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mcaption/mcaption.sty
%doc %{_texmfdistdir}/doc/latex/mcaption/CHANGES
%doc %{_texmfdistdir}/doc/latex/mcaption/README
%doc %{_texmfdistdir}/doc/latex/mcaption/example.tex
%doc %{_texmfdistdir}/doc/latex/mcaption/mcaption.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mcaption/mcaption.dtx
%doc %{_texmfdistdir}/source/latex/mcaption/mcaption.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
