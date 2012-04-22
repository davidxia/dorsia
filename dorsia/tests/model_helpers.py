"""
Helper functions for testing Django model classes.
"""

def modelHasField( modelClass, fieldName ):
    return fieldName in modelClass._meta.get_all_field_names()

