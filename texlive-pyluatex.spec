%global tl_name pyluatex
%global tl_revision 78739

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7.0
Release:	%{tl_revision}.1
Summary:	Execute Python code on the fly in your LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/pyluatex
License:	mit lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pyluatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pyluatex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
PyLuaTeX allows you to execute Python code and to include the resulting
output in your LaTeX documents in a single compilation run. LaTeX
documents must be compiled with LuaLaTeX for this to work. PyLuaTeX runs
a Python InteractiveInterpreter (actually several if you use different
sessions) in the background for on-the-fly code execution. Python code
from your LaTeX file is sent to the background interpreter through a TCP
socket. This approach allows your Python code to be executed and the
output to be integrated in your LaTeX file in a single compilation run.
No additional processing steps are needed. No intermediate files have to
be written. No placeholders have to be inserted.

