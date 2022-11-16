Name:		texlive-pyluatex
Version:	63491
Release:	1
Summary:	Execute Python code on the fly in your LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pyluatex
License:	mit lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pyluatex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pyluatex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
PyLuaTeX allows you to execute Python code and to include the
resulting output in your LaTeX documents in a single
compilation run. LaTeX documents must be compiled with LuaLaTeX
for this to work. PyLuaTeX runs a Python InteractiveInterpreter
(actually several if you use different sessions) in the
background for on-the-fly code execution. Python code from your
LaTeX file is sent to the background interpreter through a TCP
socket. This approach allows your Python code to be executed
and the output to be integrated in your LaTeX file in a single
compilation run. No additional processing steps are needed. No
intermediate files have to be written. No placeholders have to
be inserted.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/pyluatex
%doc %{_texmfdistdir}/doc/lualatex/pyluatex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
