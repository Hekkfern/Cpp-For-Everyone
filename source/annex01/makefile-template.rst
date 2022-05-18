#########################
Makefile template
#########################

For a project structure like this:

.. code-block:: none
    :linenos:

    .
    ├── include
    │   ├── dir1
    │   │   ├── file1.hpp
    │   │   └── file2.hpp
    │   ├── dir2
    │   │   ├── file3.hpp
    │   │   └── file4.hpp
    ├── Makefile
    └── src
        ├── dir1
        │   ├── file1.cpp
        │   └── file2.cpp
        └── dir2
            ├── file3.cpp
            └── file4.cpp


A suitable *Makefile* to use looks like this:

.. code-block:: make
    :linenos:

    CXX      := CXX
    CXXFLAGS := -std=c++20 -pedantic -Wall -Wextra -Werror
    LDFLAGS  :=
    BUILD    := ./build
    OBJ_DIR  := $(BUILD)/objects
    APP_DIR  := $(BUILD)/apps
    TARGET   := my_app_name
    INCLUDE  := -Iinclude/
    SRC      :=                    \
        $(wildcard src/dir1/*.cpp) \
        $(wildcard src/dir2/*.cpp)

    OBJECTS  := $(SRC:%.cpp=$(OBJ_DIR)/%.o)
    DEPENDENCIES \
            := $(OBJECTS:.o=.d)

    all: build $(APP_DIR)/$(TARGET)

    $(OBJ_DIR)/%.o: %.cpp
        @mkdir -p $(@D)
        $(CXX) $(CXXFLAGS) $(INCLUDE) -c $< -MMD -o $@

    $(APP_DIR)/$(TARGET): $(OBJECTS)
        @mkdir -p $(@D)
        $(CXX) $(CXXFLAGS) -o $(APP_DIR)/$(TARGET) $^ $(LDFLAGS)

    -include $(DEPENDENCIES)

    .PHONY: all build clean debug release info

    build:
        @mkdir -p $(APP_DIR)
        @mkdir -p $(OBJ_DIR)

    debug: CXXFLAGS += -DDEBUG -g
    debug: all

    release: CXXFLAGS += -O2
    release: all

    clean:
        -@rm -rvf $(OBJ_DIR)/*
        -@rm -rvf $(APP_DIR)/*

    info:
        @echo "[*] Application dir: ${APP_DIR}     "
        @echo "[*] Object dir:      ${OBJ_DIR}     "
        @echo "[*] Sources:         ${SRC}         "
        @echo "[*] Objects:         ${OBJECTS}     "
        @echo "[*] Dependencies:    ${DEPENDENCIES}"
