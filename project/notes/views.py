from coreapi import Error
from rest_framework.decorators import api_view
from rest_framework.response import Response
from project.notes.documents import get_notes, get_note
from project.notes.models import Note
from project.notes.serializers import AddNoteSerializer, EditNoteSerializer


@api_view(['GET', 'POST'])
def note_list(request):
    if request.method == 'POST':
        serializer = AddNoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Note.objects.create(
            description=serializer.validated_data['description'],
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
        error = Error(['This note no longer exists.'])
        return Response(error, status=404)

    if request.method == 'DELETE':
        instance.delete()
        return Response(status=204)

    elif request.method == 'PUT':
        serializer = EditNoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.update(**serializer.validated_data)

    doc = get_note(instance)
    return Response(doc)
