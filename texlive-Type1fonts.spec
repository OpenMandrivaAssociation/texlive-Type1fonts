# revision 19603
# category Package
# catalog-ctan /info/Type1fonts/fontinstallationguide
# catalog-date 2010-08-29 15:39:11 +0200
# catalog-license fdl
# catalog-version 2.14
Name:		texlive-Type1fonts
Version:	2.14
Release:	1
Summary:	Font installation guide
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/Type1fonts/fontinstallationguide
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/Type1fonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/Type1fonts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This guide discusses the most common scenarios you are likely
to encounter when installing Type 1 PostScript fonts. While the
individual tools employed in the installation process are
documented well, the actual difficulty most users are facing
when trying to install new fonts is understanding how to put
all the pieces together. This is what this guide is about.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/fonts/Type1fonts/README
%doc %{_texmfdistdir}/doc/fonts/Type1fonts/examples.zip
%doc %{_texmfdistdir}/doc/fonts/Type1fonts/fontinstallationguide.pdf
%doc %{_texmfdistdir}/doc/fonts/Type1fonts/fontinstallationguide.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
