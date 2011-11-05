# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xcolor
# catalog-date 2007-01-21 23:54:12 +0100
# catalog-license lppl
# catalog-version 2.11
Name:		texlive-xcolor
Version:	2.11
Release:	1
Summary:	Driver-independent color extensions for LaTeX and pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xcolor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides easy driver-independent access to several kinds of
color tints, shades, tones, and mixes of arbitrary colors. It
allows a user to select a document-wide target color model and
offers complete tools for conversion between eight color
models. Additionally, there is a command for alternating row
colors plus repeated non-aligned material (like horizontal
lines) in tables. Colors can be mixed like
\color{red!30!green!40!blue}.

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
%{_texmfdistdir}/dvips/xcolor/xcolor.pro
%{_texmfdistdir}/tex/latex/xcolor/svgnam.def
%{_texmfdistdir}/tex/latex/xcolor/x11nam.def
%{_texmfdistdir}/tex/latex/xcolor/xcolor.sty
%doc %{_texmfdistdir}/doc/latex/xcolor/ChangeLog
%doc %{_texmfdistdir}/doc/latex/xcolor/README
%doc %{_texmfdistdir}/doc/latex/xcolor/xcolor.lox
%doc %{_texmfdistdir}/doc/latex/xcolor/xcolor.pdf
%doc %{_texmfdistdir}/doc/latex/xcolor/xcolor1.tex
%doc %{_texmfdistdir}/doc/latex/xcolor/xcolor2.pdf
%doc %{_texmfdistdir}/doc/latex/xcolor/xcolor2.tex
%doc %{_texmfdistdir}/doc/latex/xcolor/xcolor3.tex
%doc %{_texmfdistdir}/doc/latex/xcolor/xcolor4.tex
#- source
%doc %{_texmfdistdir}/source/latex/xcolor/xcolor.dtx
%doc %{_texmfdistdir}/source/latex/xcolor/xcolor.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
