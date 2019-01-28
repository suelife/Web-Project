from django.apps import apps

def getField(appname,modelname):
    modelobj = apps.get_model(appname,modelname)
    ayfield=[]
    for field in modelobj._meta.fields:  
        if field.verbose_name != field.name:
            ayfield.append(field.verbose_name)
    return ayfield
    