

class Contact:
    def __init__(self,first_name,last_name,email_address=None,phonenumber=None,display_name='masked'):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address
        self.phonenumber = phonenumber
        self.display_name = display_name

    def __eq__(self, other):
        if self.email and other.email:
            return self.email == other.email
        if self.phonenumber and other.phonenumber:
            return self.phonenumber == other.phonenumber
        if self.first_name == other.first_name and self.last_name == self.last_name:
            return True
        return False

    def __repr__(self):
        instance_attr = []

        for key in self.__dict__:
            value = "'{}'".format(self.__dict__[key])
            instance_attr.extend([key,value])

        return_instance = 'Contact({})'.format('{}={},' * (len(instance_attr) // 2)).replace(',)', ')')

        return return_instance.format(*instance_attr)

    def __str__(self):
        return self.last_name[0] + self.first_name[0]

    @staticmethod
    def _obfuscate(string):
        string_length = len(string)
        string_ofuscated = string[:string_length // 2].ljust(string_length, '*')

        return string_ofuscated

    def __format__(self,format_spec):
        if format_spec == 'unmasked':
            return repr(self)
        elif format_spec == 'masked':
            instance_attr = []
            for key in self.__dict__:
                value = self.__dict__[key]
                value = self._obfuscate(value) if value != 'display_name' else value
                instance_attr.extend([key, value])

            return_instance = 'Contact({})'.format('{}={},' * (len(instance_attr) // 2)).replace(',)', ')')

            return return_instance.format(*instance_attr)
        else:
            raise '{} is not a valid format. Choose "masked" or "unmasked"!'.format(format_spec)

    def __hash__(self):
        return hash((self.first_name,self.last_name,self.display_name,self.email,self.phonenumber,self.__class__))

instance = Contact(first_name='breno',
                   last_name='benevides',
                   email_address='brenoitalolima@yahoo.com',
                   phonenumber='+55 85 997344976',
                   display_name='masked'
                   )

instance2 = Contact(first_name='breno',
                   last_name='benevides',
                   email_address='brenoitalolima@yahoo.com',
                   phonenumber='+55 85 997344976',
                   display_name='masked'
                   )

print(hash(instance) == hash(instance2))

