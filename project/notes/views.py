from rest_framework.decorators import api_view
from rest_framework.response import Response
from project.notes.documents import get_notes, get_note
from project.notes.models import Note


@api_view(['GET', 'POST'])
def note_list(request):
    if request.method == 'POST':
        Note.objects.create(
            description=str(request.data['description']),
            complete=False
        )

    queryset = Note.objects.all()
    doc = get_notes(queryset)
    return Response(doc)


@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, pk):
    try:
        instance = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=404)

    if request.method == 'DELETE':
        instance.delete()
        return Response(status=204)

    elif request.method == 'PUT':
        if 'description' in request.data:
            instance.description = str(request.data['description'])
        if 'complete' in request.data:
            instance.complete = bool(request.data['complete'])
        instance.save()

    doc = get_note(instance)
    return Response(doc)
