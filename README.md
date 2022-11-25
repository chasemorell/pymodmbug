# pymodm bug?


`get_patient()` only works when called from within `db_interface.py`


Example:

`outside.py` calls get_patient() function from `db_interface`. This doesn't work. 

How to run:

This works (sucessfully finds 1 document):
`python3 db_interface.py`

This doesn't work (finds 0 documents):
`python3 outside.py`

