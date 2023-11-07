#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints basic info about py
 *
 * @p: PyObject list
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	long int size, idx;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (idx = 0; idx < size; idx++)
	{
		item = PyList_GetItem(p, idx);
		printf("Element %ld: %s\n", idx, Py_TYPE(item)->tp_name);
	}
}
