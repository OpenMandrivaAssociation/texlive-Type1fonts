# revision 19603
# category Package
# catalog-ctan /info/Type1fonts/fontinstallationguide
# catalog-date 2010-08-29 15:39:11 +0200
# catalog-license fdl
# catalog-version 2.14
Name:		texlive-Type1fonts
Version:	2.14
Release:	9
Summary:	Font installation guide
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/Type1fonts/fontinstallationguide
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/Type1fonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/Type1fonts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.14-2
+ Revision: 757166
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.14-1
+ Revision: 719825
- texlive-Type1fonts
- texlive-Type1fonts
- texlive-Type1fonts
- texlive-Type1fonts
- texlive-Type1fonts

