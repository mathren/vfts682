(TeX-add-style-hook
 "VFTS682_MNRASL"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("mnras" "a4paper" "fleqn" "usenatbib")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("xcolor" "usenames" "dvipsnames")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "mnras"
    "mnras10"
    "newtxtext"
    "newtxmath"
    "fontenc"
    "ae"
    "aecompl"
    "graphicx"
    "amsmath"
    "amssymb"
    "hyperref"
    "xcolor"
    "url"
    "multirow")
   (TeX-add-symbols
    '("Secref" 1)
    '("Tabref" 1)
    '("Figref" 1)
    '("Eqref" 1)
    '("newtext" 1)
    '("SdM" 1)
    "kms"
    "Msun"
    "Lsun"
    "Myr"
    "masyr")
   (LaTeX-add-labels
    "firsxtpage"
    "sec:intro"
    "sec:sample"
    "tab:star_param"
    "tab:vfts682"
    "fig:dist"
    "fig:main"
    "data:gaia"
    "sec:results"
    "eq:kin_age"
    "sec:discussion"
    "lastpage")
   (LaTeX-add-bibliographies
    "bibliography/vfts682")
   (LaTeX-add-xcolor-definecolors
    "Wildstrawberry"))
 :latex)

