
/* Tuple object interface */

#ifndef Py_TUPLEOBJECT_H
#define Py_TUPLEOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    PyObject_VAR_HEAD
    PyObject *ob_item[1];
    /* ob_item contains space for 'ob_size' elements.
     * Items must normally not be NULL, except during construction when
     * the tuple is not yet visible outside the function that builds it.
     */
} PyTupleObject;

PyAPI_FUNC(PyObject *) PyTuple_New(Py_ssize_t size);
PyAPI_FUNC(void) _PyPy_tuple_dealloc(PyObject *);

/* defined in varargswrapper.c */
PyAPI_FUNC(PyObject *) PyTuple_Pack(Py_ssize_t, ...);


/* Macro, trading safety for speed */
#define PyTuple_GET_ITEM(op, i) (((PyTupleObject *)(op))->ob_item[i])
#define PyTuple_GET_SIZE(op)    Py_SIZE(op)

/* Macro, *only* to be used to fill in brand new tuples */
#define PyTuple_SET_ITEM(op, i, v) (((PyTupleObject *)(op))->ob_item[i] = v)

#define PyTuple_Check(op) \
		 PyType_FastSubclass((op)->ob_type, Py_TPFLAGS_TUPLE_SUBCLASS)
#define PyTuple_CheckExact(op) ((op)->ob_type == &PyTuple_Type)

#ifdef __cplusplus
}
#endif
#endif /* !Py_TUPLEOBJECT_H */
