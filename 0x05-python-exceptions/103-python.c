#include <Python.h>
#include <stdio.h>

/**
 *  * print_python_list - Print basic info about Python lists
 *   * @p: Python object pointer
 *    */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *obj;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}

/**
 *  * print_python_bytes - Print basic info about Python bytes
 *   * @p: Python object pointer
 *    */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02x", str[i]);
	printf("\n");
}

/**
 *  * print_python_float - Print basic info about Python float objects
 *   * @p: Python object pointer
 *    */
void print_python_float(PyObject *p)
{
	PyObject *str_obj;
	char *str;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	str_obj = PyObject_Str(p);
	str = PyUnicode_AsUTF8(str_obj);
	printf("  value: %s\n", str);
}
