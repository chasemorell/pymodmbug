# a minimal, self-contained example showing a possible pymodm bug

def get_patient():
    import pymodm

    pymodm.connect(
        "mongodb+srv://admin:BUywxjVcnutPCjRA@cluster0.ixssdzz.mongodb.net/"
        "test?retryWrites=true&w=majority")

    class PatientData(pymodm.MongoModel):
        medical_record_number = pymodm.fields.CharField(primary_key=True)
        patient_name = pymodm.fields.CharField()

    p = PatientData.objects.raw({'_id': "123"})

    # note that this query works when using flask.
    return p.count()


# sucessfully finds the patient (prints count of 1)
if __name__ == "__main__":
    print(get_patient())
