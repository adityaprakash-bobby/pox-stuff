
/* Bool object interface */

#ifndef Py_BOOLOBJECT_H
#define Py_BOOLOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

#define PyBoolObject PyIntObject

#define Py_False ((PyObject *) &_Py_ZeroStruct)
#define Py_True ((PyObject *) &_Py_TrueStruct)

/* Macros for returning Py_True or Py_False, respectively */
#define Py_RETURN_TRUE return Py_INCREF(Py_True), Py_True
#define Py_RETURN_FALSE return Py_INCREF(Py_False), Py_False

#define PyBool_Check(op) ((op)->ob_type == &PyBool_Type)

#ifdef __cplusplus
}
#endif
#endif /* !Py_BOOLOBJECT_H */
