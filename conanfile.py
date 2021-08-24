from conans import ConanFile


class CppStarterProject(ConanFile):
    # Note: options are copied from CMake boolean options.
    # When turned off, CMake sometimes passes them as empty strings.
    options = {
        "cpp_starter_use_imgui": ["ON", "OFF", ""],
        "cpp_starter_use_sdl": ["ON", "OFF", ""]
    }
    name = "CppStarterProject"
    version = "0.1"
    requires = (
        "catch2/2.13.3",
        "docopt.cpp/0.6.2",
        "fmt/6.2.1",
        "spdlog/1.5.0",
    )
    generators = "cmake", "gcc", "txt"

    def requirements(self):
        if self.options.cpp_starter_use_imgui == "ON":
            self.requires("imgui-sfml/2.1@bincrafters/stable")
        if self.options.cpp_starter_use_sdl == "ON":
            self.requires("sdl2/2.0.10@bincrafters/stable")
