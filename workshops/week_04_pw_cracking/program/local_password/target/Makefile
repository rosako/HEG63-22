# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -std=c11

# Target binary name
TARGET = hackme

# Default rule to build the program
all: $(TARGET)

# Rule to build the target
$(TARGET): hackme.c
	$(CC) $(CFLAGS) -o $(TARGET) hackme.c

# Clean up generated files
clean:
	rm -f $(TARGET)

# Phony targets to avoid conflicts with files
.PHONY: all clean

