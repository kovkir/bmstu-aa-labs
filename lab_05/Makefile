CC := g++
CFLAGS := -std=c++17 -Wall -Werror -pedantic 

CFILES_DIR := ./src
CFILES := $(wildcard $(CFILES_DIR)/*.cpp)

INC_DIR := ./inc
INCLUDES := $(wildcard $(INC_DIR)/*.h)
INCLUDES += $(wildcard $(INC_DIR)/*.hpp)

OBJ_DIR := ./out
OBJECTS := $(CFILES:$(CFILES_DIR)/%.cpp=$(OBJ_DIR)/%.o)

APP = app.exe
GR = ./src/graph.py

.PHONY : clean run graph

$(APP): $(OBJECTS)
	@$(CC) $^ -o $@

$(OBJ_DIR):
	@mkdir -p $@

$(OBJ_DIR)/%.o: $(CFILES_DIR)/%.cpp $(INCLUDES) $(OBJ_DIR)
	@$(CC) $(CFLAGS) -c $< -o $@ 

run: $(APP)
	@./$^

graph: $(GR)
	@python3 ./$^

clean:
	@$(RM) $(OBJ_DIR)/*.o *.exe
 