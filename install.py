import os
import shutil
import sys
install_path = "C:\\Program Files\\OLang"
files_to_copy = [
    'OLang/main.py',
    'OLang/instructions.py',
    'OLang/structures.py',
    'OLang/commands',
]
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def copy_files():
    for file in files_to_copy:
        src = os.path.join(os.getcwd(), file)
        dest = os.path.join(install_path, file)
        if os.path.isdir(src):
            if not os.path.exists(dest):
                create_directory(dest)
            else:
                for item in os.listdir(src):
                    s = os.path.join(src, item)
                    d = os.path.join(dest, item)
                    if os.path.isdir(s):
                        shutil.copytree(s, d, dirs_exist_ok=True)
                    else:
                        shutil.copy2(s, d)
        else:
            dest_dir = os.path.dirname(dest)
            if not os.path.exists(dest_dir):
                create_directory(dest_dir)
            shutil.copy2(src, dest)
def set_file_association():
    import winreg
    try:
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, ".o")
        winreg.SetValue(key, "", winreg.REG_SZ, "OLangFile")
        winreg.CloseKey(key)
        program_path = os.path.join(install_path, "OLang", "main.py")
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, "OLangFile\\shell\\open\\command")
        file_type = ".o"
        command_key = r"Software\Classes" + file_type + r"\shell\open\command" 
        new_command = f"cmd.exe /k title OLang && \"{sys.executable}\" \"{program_path}\" \"%1\""
        winreg.SetValue(key, command_key, winreg.REG_SZ, new_command)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Failed to set file association: {e}")
def install():
    print( "" )
    print( "  ______         __" )
    print( " /      \       /  |" )
    print( "/$$$$$$  |      $$ |        ______   _______    ______  " )
    print( "$$ |  $$ |      $$ |       /      \ /       \  /      \ " )
    print( "$$ |  $$ |      $$ |       $$$$$$  |$$$$$$$  |/$$$$$$  |" )
    print( "$$ |  $$ |      $$ |       /    $$ |$$ |  $$ |$$ |  $$ |" )
    print( "$$ \__$$ |      $$ |_____ /$$$$$$$ |$$ |  $$ |$$ \__$$ |" )
    print( "$$    $$/       $$       |$$    $$ |$$ |  $$ |$$    $$ |" )
    print( " $$$$$$/        $$$$$$$$/  $$$$$$$/ $$/   $$/  $$$$$$$ |" )
    print( "                                              /  \__$$ |" )
    print( "                                              $$    $$/" )
    print( "                                               $$$$$$/\n\n\n" )

    print("Creating directories...")
    create_directory(install_path)
    print("Copying files...")
    copy_files()
    print("Setting file association...")
    set_file_association()
    print("OLang has been successfully installed!")
    input("Press ENTER to exit...")
if __name__ == "__main__":
    install()