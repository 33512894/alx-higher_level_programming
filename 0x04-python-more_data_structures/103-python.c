#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
    char *string;
    long int size, i, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(p);
    string = PyBytes_AS_STRING(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    limit = (size >= 10) ? 10 : size + 1;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++)
    {
        printf(" %02x", (unsigned char)string[i]);
    }

    printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
    long int size, i;
    PyListObject *list;
    PyObject *obj;

    size = PyList_GET_SIZE(p);
    list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        obj = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj))
        {
            print_python_bytes(obj);
        }
    }
}    
