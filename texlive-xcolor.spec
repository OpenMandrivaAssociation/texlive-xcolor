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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

