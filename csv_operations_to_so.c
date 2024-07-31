#include <Python.h>

int processCsv(int argc, char *argv[]) {
    PyObject *pModule, *pFunc, *pArgs, *pValue;

    if (argc < 4) {
        fprintf(stderr, "Usage: %s <script.py> <arg1> <arg2> ...\n", argv[0]);
        return 1;
    }

    Py_Initialize();

    // Importando um módulo Python personalizado
    pModule = PyImport_ImportModule("csv_operations");
    if (pModule == NULL) {
        PyErr_Print();
        Py_Finalize();
        return 1;
    }

    // Obtendo a função processCsvFile do módulo importado
    pFunc = PyObject_GetAttrString(pModule, "processCsvFile");
    if (!pFunc || !PyCallable_Check(pFunc)) {
        if (PyErr_Occurred())
            PyErr_Print();
        fprintf(stderr, "Cannot find function 'processCsvFile'\n");
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
        Py_Finalize();
        return 1;
    }

    // Criando argumentos para a chamada da função
    pArgs = PyTuple_New(argc - 1);
    for (int i = 1; i < argc; ++i) {
        PyTuple_SetItem(pArgs, i - 1, PyUnicode_FromString(argv[i]));
    }

    // Chamando a função e obtendo o resultado
    pValue = PyObject_CallObject(pFunc, pArgs);
    
    if (pValue != NULL) {
        // Exibir ou utilizar o resultado, se necessário
        Py_DECREF(pValue);
    } else {
        PyErr_Print();
    }

    // Liberando memória e finalizando o interpretador Python
    Py_DECREF(pArgs);
    Py_DECREF(pFunc);
    Py_DECREF(pModule);

    Py_Finalize();
    return 0;
}


int processCsvFile(int argc, char *argv[]) {
    PyObject *pModule, *pFunc, *pArgs, *pValue;

    if (argc < 4) {
        fprintf(stderr, "Usage: %s <script.py> <arg1> <arg2> ...\n", argv[0]);
        return 1;
    }

    Py_Initialize();

    // Importando um módulo Python personalizado
    pModule = PyImport_ImportModule("csv_operations");
    if (pModule == NULL) {
        PyErr_Print();
        Py_Finalize();
        return 1;
    }

    // Obtendo a função processCsvFile do módulo importado
    pFunc = PyObject_GetAttrString(pModule, "processCsvFile");
    if (!pFunc || !PyCallable_Check(pFunc)) {
        if (PyErr_Occurred())
            PyErr_Print();
        fprintf(stderr, "Cannot find function 'processCsvFile'\n");
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
        Py_Finalize();
        return 1;
    }

    // Criando argumentos para a chamada da função
    pArgs = PyTuple_New(argc - 1);
    for (int i = 1; i < argc; ++i) {
        PyTuple_SetItem(pArgs, i - 1, PyUnicode_FromString(argv[i]));
    }

    // Chamando a função e obtendo o resultado
    pValue = PyObject_CallObject(pFunc, pArgs);
    
    if (pValue != NULL) {
        // Exibir ou utilizar o resultado, se necessário
        Py_DECREF(pValue);
    } else {
        PyErr_Print();
    }

    // Liberando memória e finalizando o interpretador Python
    Py_DECREF(pArgs);
    Py_DECREF(pFunc);
    Py_DECREF(pModule);

    Py_Finalize();
    return 0;
}

