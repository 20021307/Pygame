import cx_Freeze

executables = [cx_Freeze.Executable("vislice.py")]

cx_Freeze.setup(
    name="Vislice",
    options={"build_exe": {"packages":["pygame", "random", "os", "webbrowser"],
                           "include_files": ["img/1.png", "img/2.png", "img/3.png", "img/4.png", "img/5.png",
                                              "img/6.png", "img/7.png", "img/8.png", "img/9.png", "img/10.png",
                                              "OpenSans-Regular.ttf"]}},
    executables = executables
)
