#include <stdio.h>
#include "Python.h"

// Declaração das funções externas do arquivo .so
extern int processCsv(int argc, char *argv[]);
extern int processCsvFile(int argc, char *argv[]);

void processCsv(const char csv[], const char selectedColumns[], const char rowFilterDefinitions[]) {
   int result1 = processCsv(argc, argv);
    printf("Result of processCsv: %d\n", result1);

}

void processCsvFile(const char csvFilePath[], const char selectedColumns[], const char rowFilterDefinitions[]) {
   int result2 = processCsvFile(argc, argv);
    printf("Result of processCsvFile: %d\n", result2);
}