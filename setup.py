import cx_Freeze

executables = [cx_Freeze.Executable(script="batalhaaerea.py",icon="assets/saikomene.ico")]

cx_Freeze.setup(
    name="Batalha Aerea",
    options={"build_exe": {"packages":["pygame"],
                            "include_files":["assets"]}},
    executables = executables

)