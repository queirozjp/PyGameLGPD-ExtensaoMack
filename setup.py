import cx_Freeze

executables = [cx_Freeze.Executable('lgpd.py')]

cx_Freeze.setup(
    name = "Privacidade em Jogo",
    options = {'build_exe' : {'packages': ['pygame'],
                             'include_files': ['Images']}},
    executables = executables
)