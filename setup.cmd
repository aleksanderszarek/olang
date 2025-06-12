@echo off
echo "    
echo "      ______         __
echo "     /      \       /  |
echo "    /$$$$$$  |      $$ |        ______   _______    ______
echo "    $$ |  $$ |      $$ |       /      \ /       \  /      \
echo "    $$ |  $$ |      $$ |       $$$$$$  |$$$$$$$  |/$$$$$$  |
echo "    $$ |  $$ |      $$ |       /    $$ |$$ |  $$ |$$ |  $$ |
echo "    $$ \__$$ |      $$ |_____ /$$$$$$$ |$$ |  $$ |$$ \__$$ |
echo "    $$    $$/       $$       |$$    $$ |$$ |  $$ |$$    $$ |
echo "     $$$$$$/        $$$$$$$$/  $$$$$$$/ $$/   $$/  $$$$$$$ |
echo "                                                  /  \__$$ |
echo "                                                  $$    $$/
echo "                                                   $$$$$$/
echo.
echo.
echo.
echo.
echo Welcome to O Lang, the best language for learning Assembly.
echo This language is meant to introduce you to low-level programming as a middleman between languages like C++ and Assembly.
echo After the installation, you will be able to create .o files and run them on your machine.
echo.
echo Installing Python ...
python_bin.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
powershell "start python install.py -v runAs"