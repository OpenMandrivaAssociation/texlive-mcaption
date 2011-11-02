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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The mcaption package provides an mcaption environment which
puts figure or table captions in the margin. The package works
with the standard classes and with the KOMA-Script document
classes scrartcl, scrreprt and scrbook. The package requires
the changepage package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
