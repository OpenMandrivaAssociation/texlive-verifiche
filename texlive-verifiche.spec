Name:		texlive-verifiche
Version:	64425
Release:	1
Summary:	A LaTeX package to typeset (Italian) high school tests
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verifiche
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verifiche.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verifiche.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verifiche.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The purpose of this package is to manage the exercises for a
test, their points, levels of difficulty, and solutions. Some
typical formats of exercises are already implemented: Plain
exercise "Complete the Text" "True or false" Closed questions
Open questions "Find the error"

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/verifiche
%{_texmfdistdir}/tex/latex/verifiche
%doc %{_texmfdistdir}/doc/latex/verifiche

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
