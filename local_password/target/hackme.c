#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    // Hardcoded password
    const char *hardcoded_password = "secret123";

    // Check if a password is provided as a command-line argument
    if (argc != 2) {
        printf("Usage: %s <password>\n", argv[0]);
        return 1;
    }

    // Compare the provided password with the hardcoded password
    if (strcmp(argv[1], hardcoded_password) == 0) {
        printf("Access Granted\n");
    } else {
        printf("Access Denied\n");
    }

    return 0;
}

