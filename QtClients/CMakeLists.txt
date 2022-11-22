cmake_minimum_required(VERSION 3.16)
project(Lab5 VERSION 1.0 LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOUIC ON)

find_package(QT NAMES Qt5 Qt6 REQUIRED COMPONENTS Core)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Gui Network)
find_package(Qt${QT_VERSION_MAJOR} OPTIONAL_COMPONENTS Widgets)

qt_standard_project_setup()

qt_add_executable(Lab5 WIN32 MACOSX_BUNDLE
    asm2204/st08/dialog220408.cpp  asm2204/st08/dialog220408.h
    asm2204/st08/dialog220408.ui asm2204/st08/group220408.cpp asm2204/st08/group220408.h
	

    main.cpp
    mainwindow.cpp mainwindow.h mainwindow.ui
    qrest.cpp qrest.h
)
target_compile_definitions(Lab5 PRIVATE
    QT_DEPRECATED_WARNINGS
)

target_link_libraries(Lab5 PRIVATE
    Qt::Core
    Qt::Gui
    Qt::Network
)

if((QT_VERSION_MAJOR GREATER 4))
    target_link_libraries(Lab5 PRIVATE
        Qt::Widgets
    )
endif()

install(TARGETS Lab5
    BUNDLE DESTINATION .
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

qt_generate_deploy_app_script(
    TARGET Lab5
    FILENAME_VARIABLE deploy_script
    NO_UNSUPPORTED_PLATFORM_ERROR
)
install(SCRIPT ${deploy_script})
