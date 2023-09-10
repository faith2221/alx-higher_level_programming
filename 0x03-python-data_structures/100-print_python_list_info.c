#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic information about Python lists.
 * @p: A pyObject list.
 */

void print_python_list_info(PyObject *p)
{
	PyObject *item;
	int size = Py_SIZE(p);
	int alloc = ((PyListObject *)p)->allocated;
	int i = 0;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		item = PyList_Getltem(p, i);
		printf("%s\n, Py_TYPE(item)->tp_name);
	}
}
