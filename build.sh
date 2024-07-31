#!/bin/sh

# Compilar o módulo Cython
python setup.py build_ext --inplace


gcc -Wall -fPIC -c csv_operations_to_so.c -o csv_operations.o -I/usr/include/python3.12
gcc -shared -o csv_operations.so csv_operations.o

# Compilar o programa C
gcc -o main main.c -I/usr/include/python3.8 -L. -lpython3.8 -lcsv_operations

# Rodar o programa compilado
./main
