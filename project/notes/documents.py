from coreapi import Document, Link, required


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
            'add_note': Link(trans='action', fields=[required('description')])
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
            'description': intance.description,
            'complete': instance.complete,
            'edit': Link(trans='update', fields=['description', 'complete']),
            'delete': Link(trans='delete')
        }
    )
