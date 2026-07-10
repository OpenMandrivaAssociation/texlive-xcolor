%global tl_name xcolor
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.02
Release:	%{tl_revision}.1
Summary:	Driver-independent color extensions for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xcolor
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package starts from the basic facilities of the color package, and
provides easy driver-independent access to several kinds of color tints,
shades, tones, and mixes of arbitrary colors. It allows a user to select
a document-wide target color model and offers complete tools for
conversion between eight color models. Additionally, there is a command
for alternating row colors plus repeated non-aligned material (like
horizontal lines) in tables. Colors can be mixed like
\color{red!30!green!40!blue}.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/dvips
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/dvips/xcolor
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/xcolor
%dir %{_datadir}/texmf-dist/source/latex/xcolor
%dir %{_datadir}/texmf-dist/tex/latex/xcolor
%doc %{_datadir}/texmf-dist/doc/latex/xcolor/ChangeLog
%doc %{_datadir}/texmf-dist/doc/latex/xcolor/README.md
%doc %{_datadir}/texmf-dist/doc/latex/xcolor/xcolor.lox
%doc %{_datadir}/texmf-dist/doc/latex/xcolor/xcolor.pdf
%doc %{_datadir}/texmf-dist/doc/latex/xcolor/xcolor1.tex
%doc %{_datadir}/texmf-dist/doc/latex/xcolor/xcolor2.pdf
%doc %{_datadir}/texmf-dist/doc/latex/xcolor/xcolor2.tex
%doc %{_datadir}/texmf-dist/doc/latex/xcolor/xcolor3.tex
%doc %{_datadir}/texmf-dist/doc/latex/xcolor/xcolor4.tex
%{_datadir}/texmf-dist/dvips/xcolor/xcolor.pro
%doc %{_datadir}/texmf-dist/source/latex/xcolor/xcolor.dtx
%doc %{_datadir}/texmf-dist/source/latex/xcolor/xcolor.ins
%{_datadir}/texmf-dist/tex/latex/xcolor/svgnam.def
%{_datadir}/texmf-dist/tex/latex/xcolor/x11nam.def
%{_datadir}/texmf-dist/tex/latex/xcolor/xcolor-2022-06-12.sty
%{_datadir}/texmf-dist/tex/latex/xcolor/xcolor.sty
