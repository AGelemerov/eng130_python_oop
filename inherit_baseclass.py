import base_class as bc

print(bc.__multiply(5, 2))
print(bc.__divide(5, 2))
print(bc.__modulus(5, 2))
print(bc.__cm_to_m(52))
print(bc.__inch_to_cm(52))
print(bc.__m_to_feet(52))


class ImportToFiles:
    def __init__(self, name):
        print(name)


test = ImportToFiles("John🤩")
