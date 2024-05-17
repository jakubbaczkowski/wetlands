import pandas as pd
from app.publications_upload_validation import PublicationsCSVClassValidator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import ProfileUser, Publications, UserStats
from .publications_upload_validation import PublicationsCSVCols
from .serializers import UploadSerializer, UserSerializer


# Create your views here.
def index(request):

    return render(request, 'index.html')


def singleview(request):
    return render(request, 'singleview.html')


def homepage(request):
    return render(request, "homepage.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            cur_user = request.user
            ProfileUser.objects.get_or_create(
                user=cur_user, username=cur_user.username, first_name=cur_user.first_name, last_name=cur_user.last_name, email=cur_user.email
            )
            return redirect('index')
        else:
            messages.error(request, ("Einloggen fehlgeschlagen, ungültiger Benutzername oder Passwort."))
            return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def write_to_db(self, df) -> int:
        count_new_publications = 0
        for _, row in df.iterrows():
            if Publications.objects.filter(id_import=row[PublicationsCSVCols.ID_IMPORT]).exists():
                continue

            pub = Publications(
                id_import=row[PublicationsCSVCols.ID_IMPORT],
                title=row[PublicationsCSVCols.TITLE],
                first_author_name=row[PublicationsCSVCols.AUTHOR],
                id_scopus=(row[PublicationsCSVCols.ID_SCOPUS]),
                id_crossref=row[PublicationsCSVCols.ID_CROSSREF],
                abstract=row[PublicationsCSVCols.ABSTRACT],
                doi=row[PublicationsCSVCols.DOI],
                year=row[PublicationsCSVCols.YEAR],
                url=row[PublicationsCSVCols.URL],
                pages=row[PublicationsCSVCols.PAGES],
                type=row[PublicationsCSVCols.TYPE],
                lang=row[PublicationsCSVCols.LANG],
                volume=row[PublicationsCSVCols.VOLUME],
                issue=row[PublicationsCSVCols.ISSUE],
                issn=row[PublicationsCSVCols.ISSN],
                journal=row[PublicationsCSVCols.JOURNAL],
                disciplines=row[PublicationsCSVCols.DISCIPLINES],
                first_author_scopus_id=row[PublicationsCSVCols.AUTHOR_SCOPUS_ID],
                first_author_affiliation_name=row[PublicationsCSVCols.AUTHOR_AFFILIATION_NAME],
                first_author_affiliation_country=row[PublicationsCSVCols.AUTHOR_AFFILIATION_COUNTRY],
                co_authors=row[PublicationsCSVCols.CO_AUTHORS],
                created_at=row[PublicationsCSVCols.CREATED_AT],
                keywords=row[PublicationsCSVCols.KEYWORDS],
                citations_count=row[PublicationsCSVCols.CITATIONS_COUNT],
                references_crossref_id=row[PublicationsCSVCols.REFERENCES_CROSSREF_ID],
                references_scopus_id=row[PublicationsCSVCols.REFERENCES_SCOPUS_ID],
                citation_latest=row[PublicationsCSVCols.CITATION_LATEST],
                research_method=row[PublicationsCSVCols.RESEARCH_METHOD],
                site_description=row[PublicationsCSVCols.SITE_DESCRIPTION],
                spatial_scale=row[PublicationsCSVCols.SPATIAL_SCALE],
                temporal_scale=row[PublicationsCSVCols.TEMPORAL_SCALE],
                ground_truth=row[PublicationsCSVCols.GROUND_TRUTH],
                notes=row[PublicationsCSVCols.NOTES],
                source=row[PublicationsCSVCols.SOURCE],
                citation_count=row[PublicationsCSVCols.CITATION_COUNT],
            )

            pub.save()
            count_new_publications += 1

        return count_new_publications

    def check_content_type(self, content_type) -> bool:
        if not (content_type == "text/csv" or content_type == "application/vnd.ms-excel"):
            return Response("Only csv files are allowed")

        return True

    def create(self, request):
        file_uploaded = request.FILES.get("file_uploaded")
        # check if the file is a csv file
        self.check_content_type(file_uploaded.content_type)

        # read the csv file into a pandas dataframe
        df = pd.read_csv(file_uploaded)

        # validate the csv file columns
        try:
            PublicationsCSVClassValidator.validate(df)
        except Exception as e:
            return Response(f"CSV file is not valid {e}")

        # clean up the csv file to fit our DB schema
        df = PublicationsCSVClassValidator.clean_up(df)

        # write the publications to the DB
        count_new_publications = self.write_to_db(df)

        response = f"Added {count_new_publications} new publications. You now have {Publications.objects.all().__len__()} Publications in your DB."
        return Response(response)
