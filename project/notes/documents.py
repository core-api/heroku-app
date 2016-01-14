from coreapi import Document, Link, Field


def get_notes(queryset):
    """
    Return the top level Document object, containing all the note instances.
    """
    return Document(
        url='/',
        title='Notes',
        content={
            'notes': [
                get_note(instance) for instance in queryset
            ],
            'add_note': Link(action='post', fields=[Field('description', required=True)])
        }
    )


def get_note(instance):
    """
    Return a Document object for a single note instance.
    """
    return Document(
        url='/%s' % instance.pk,
        title='Note',
        content={
            'description': instance.description,
            'complete': instance.complete,
            'edit': Link(action='put', fields=['description', 'complete']),
            'delete': Link(action='delete')
        }
    )
