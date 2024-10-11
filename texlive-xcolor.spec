Name:		texlive-xcolor
Version:	72484
Release:	1
Summary:	Driver-independent color extensions for LaTeX and pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xcolor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides easy driver-independent access to several kinds of
color tints, shades, tones, and mixes of arbitrary colors. It
allows a user to select a document-wide target color model and
offers complete tools for conversion between eight color
models. Additionally, there is a command for alternating row
colors plus repeated non-aligned material (like horizontal
lines) in tables. Colors can be mixed like
\color{red!30!green!40!blue}.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/xcolor
%{_texmfdistdir}/tex/latex/xcolor
%doc %{_texmfdistdir}/doc/latex/xcolor
#- source
%doc %{_texmfdistdir}/source/latex/xcolor

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
