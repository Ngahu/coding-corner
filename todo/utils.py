import random
import string


def shortcode_generator(size=7,chars=string.ascii_uppercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(size))



def create_shortcode(instance,size=7):
    #save the code
    new_code = shortcode_generator(size=size)

    #make sure the code doesnt exist

    Klass = instance.__class__ #get the instance class
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return shortcode_generator(size=size)
    
    return new_code