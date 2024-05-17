from enum import Enum

import pandas as pd
from pandera import Column, DataFrameSchema


class PublicationsCSVCols(str, Enum):
    ID_IMPORT = "id"
    TITLE = "title"
    AUTHOR = "1st_author_name"
    # ab hier optionale Felder
    ID_SCOPUS = "id_scopus"
    ID_CROSSREF = "id_wos"
    ABSTRACT = "abstract"
    DOI = "doi"
    YEAR = "year"
    URL = "url"
    PAGES = "pages"
    TYPE = "type"
    LANG = "lang"
    VOLUME = "volume"
    ISSUE = "issue"
    ISSN = "issn"
    JOURNAL = "journal"
    DISCIPLINES = "disciplines"
    AUTHOR_SCOPUS_ID = "1st_author_scopus_id"
    AUTHOR_AFFILIATION_NAME = "1st_author_affiliation_name"
    AUTHOR_AFFILIATION_COUNTRY = "1st_author_affiliation_country"
    CO_AUTHORS = "co_authors"
    CREATED_AT = "created_at"
    KEYWORDS = "keywords"
    CITATIONS_COUNT = "citations_count"
    REFERENCES_CROSSREF_ID = "references_crossref_id"
    REFERENCES_SCOPUS_ID = "references_scopus_id"
    CITATION_LATEST = "citation_latest"
    RESEARCH_METHOD = "research_method"
    SITE_DESCRIPTION = "site_description"
    SPATIAL_SCALE = "spatial_scale"
    TEMPORAL_SCALE = "temporal_scale"
    GROUND_TRUTH = "ground_truth"
    NOTES = "notes"
    SOURCE = "source"
    CITATION_COUNT = "citation_count"


class PublicationsCSVClassValidator:
    """The schema to use when validating incoming CSV files for generation requests."""

    PUBLICATIONS_SCHEMA = DataFrameSchema(
        {
            PublicationsCSVCols.ID_IMPORT: Column(int),
            PublicationsCSVCols.TITLE: Column(str),
            PublicationsCSVCols.AUTHOR: Column(str),
            PublicationsCSVCols.ID_SCOPUS: Column(float, nullable=True),
            PublicationsCSVCols.ID_CROSSREF: Column(float, nullable=True),
            PublicationsCSVCols.ABSTRACT: Column(str, nullable=True),
            PublicationsCSVCols.DOI: Column(str, nullable=True),
            PublicationsCSVCols.YEAR: Column(float, nullable=True),
            PublicationsCSVCols.URL: Column(str, nullable=True),
            PublicationsCSVCols.PAGES: Column(str, nullable=True),
            PublicationsCSVCols.TYPE: Column(str, nullable=True),
            PublicationsCSVCols.LANG: Column(str, nullable=True),
            PublicationsCSVCols.VOLUME: Column(str, nullable=True),
            PublicationsCSVCols.ISSUE: Column(str, nullable=True),
            PublicationsCSVCols.ISSN: Column(str, nullable=True),
            PublicationsCSVCols.JOURNAL: Column(str, nullable=True),
            PublicationsCSVCols.DISCIPLINES: Column(str, nullable=True),
            PublicationsCSVCols.AUTHOR_SCOPUS_ID: Column(str, nullable=True),
            PublicationsCSVCols.AUTHOR_AFFILIATION_NAME: Column(str, nullable=True),
            PublicationsCSVCols.AUTHOR_AFFILIATION_COUNTRY: Column(str, nullable=True),
            PublicationsCSVCols.CO_AUTHORS: Column(str, nullable=True),
            PublicationsCSVCols.CREATED_AT: Column(str, nullable=True),
            PublicationsCSVCols.KEYWORDS: Column(str, nullable=True),
            PublicationsCSVCols.CITATIONS_COUNT: Column(float, nullable=True),
            PublicationsCSVCols.REFERENCES_CROSSREF_ID: Column(str, nullable=True),
            PublicationsCSVCols.REFERENCES_SCOPUS_ID: Column(str, nullable=True),
            PublicationsCSVCols.CITATION_LATEST: Column(str, nullable=True),
            PublicationsCSVCols.RESEARCH_METHOD: Column(str, nullable=True),
            PublicationsCSVCols.SITE_DESCRIPTION: Column(str, nullable=True),
            PublicationsCSVCols.SPATIAL_SCALE: Column(str, nullable=True),
            PublicationsCSVCols.TEMPORAL_SCALE: Column(str, nullable=True),
            PublicationsCSVCols.GROUND_TRUTH: Column(float, nullable=True),
            PublicationsCSVCols.NOTES: Column(str, nullable=True),
            PublicationsCSVCols.SOURCE: Column(str, nullable=True),
            PublicationsCSVCols.CITATION_COUNT: Column(float, nullable=True),
        },
        coerce=True,
    )

    def validate(df: pd.DataFrame) -> bool:
        df[PublicationsCSVCols.GROUND_TRUTH] = pd.to_numeric(df[PublicationsCSVCols.GROUND_TRUTH], errors='coerce')
        df[PublicationsCSVCols.TEMPORAL_SCALE] = pd.to_numeric(df[PublicationsCSVCols.TEMPORAL_SCALE], errors='coerce')
        PublicationsCSVClassValidator.PUBLICATIONS_SCHEMA.validate(df)
        return True

    def clean_up(df: pd.DataFrame) -> pd.DataFrame:
        def string_to_list(x):
            result_array = str(x).replace(']', '').replace('[', '').replace("'", '').replace('"', '').split(",")
            if result_array == ['nan']:
                return None
            return list(map(str.strip, result_array))

        def cleanup_string(x):
            if x == 'nan' or not isinstance(x, str):
                return None
            return str.strip(x)[0:255]

        def cleanup_text(x):
            if x == 'nan' or not isinstance(x, str):
                return None
            return str.strip(x)

        def cleanup_boolean(x):
            if x != x:
                return None
            elif x == 1:
                return True
            else:
                return False

        def cleanup_numbers(x):
            if x != x:
                return None
            return x

        df = df.copy()
        df[PublicationsCSVCols.TITLE] = df[PublicationsCSVCols.TITLE].apply(cleanup_string)
        df[PublicationsCSVCols.AUTHOR] = df[PublicationsCSVCols.AUTHOR].apply(cleanup_string)
        df[PublicationsCSVCols.DOI] = df[PublicationsCSVCols.DOI].apply(cleanup_string)

        # Text fields
        df[PublicationsCSVCols.ABSTRACT] = df[PublicationsCSVCols.ABSTRACT].apply(cleanup_text)
        df[PublicationsCSVCols.CITATION_LATEST] = df[PublicationsCSVCols.CITATION_LATEST].apply(cleanup_text)
        df[PublicationsCSVCols.SITE_DESCRIPTION] = df[PublicationsCSVCols.SITE_DESCRIPTION].apply(cleanup_text)
        df[PublicationsCSVCols.NOTES] = df[PublicationsCSVCols.NOTES].apply(cleanup_text)
        # String fields
        df[PublicationsCSVCols.PAGES] = df[PublicationsCSVCols.PAGES].apply(cleanup_string)
        df[PublicationsCSVCols.URL] = df[PublicationsCSVCols.URL].apply(cleanup_string)
        df[PublicationsCSVCols.TYPE] = df[PublicationsCSVCols.TYPE].apply(cleanup_string)
        df[PublicationsCSVCols.LANG] = df[PublicationsCSVCols.LANG].apply(cleanup_string)
        df[PublicationsCSVCols.VOLUME] = df[PublicationsCSVCols.VOLUME].apply(cleanup_string)
        df[PublicationsCSVCols.ISSUE] = df[PublicationsCSVCols.ISSUE].apply(cleanup_string)
        df[PublicationsCSVCols.ISSN] = df[PublicationsCSVCols.ISSN].apply(cleanup_string)
        df[PublicationsCSVCols.JOURNAL] = df[PublicationsCSVCols.JOURNAL].apply(cleanup_string)
        df[PublicationsCSVCols.AUTHOR_AFFILIATION_NAME] = df[PublicationsCSVCols.AUTHOR_AFFILIATION_NAME].apply(cleanup_string)
        df[PublicationsCSVCols.AUTHOR_AFFILIATION_COUNTRY] = df[PublicationsCSVCols.AUTHOR_AFFILIATION_COUNTRY].apply(cleanup_string)
        df[PublicationsCSVCols.REFERENCES_CROSSREF_ID] = df[PublicationsCSVCols.REFERENCES_CROSSREF_ID].apply(
            lambda x: string_to_list(x) if x else None
        )
        df[PublicationsCSVCols.SPATIAL_SCALE] = df[PublicationsCSVCols.SPATIAL_SCALE].apply(cleanup_string)
        df[PublicationsCSVCols.SOURCE] = df[PublicationsCSVCols.SOURCE].apply(cleanup_string)
        # Array fields
        df[PublicationsCSVCols.DISCIPLINES] = df[PublicationsCSVCols.DISCIPLINES].apply(lambda x: string_to_list(x) if x else None)
        df[PublicationsCSVCols.CO_AUTHORS] = df[PublicationsCSVCols.CO_AUTHORS].apply(lambda x: string_to_list(x) if x else None)
        df[PublicationsCSVCols.KEYWORDS] = df[PublicationsCSVCols.KEYWORDS].apply(lambda x: string_to_list(x) if x else None)
        df[PublicationsCSVCols.REFERENCES_SCOPUS_ID] = df[PublicationsCSVCols.REFERENCES_SCOPUS_ID].apply(lambda x: string_to_list(x) if x else None)
        df[PublicationsCSVCols.RESEARCH_METHOD] = df[PublicationsCSVCols.RESEARCH_METHOD].apply(
            lambda x: None if (x == 'nan' or isinstance(x, float)) else str.strip(x)[0:255]
        )
        # Number fields
        df[PublicationsCSVCols.ID_IMPORT] = df[PublicationsCSVCols.ID_IMPORT].apply(cleanup_numbers)
        df[PublicationsCSVCols.ID_SCOPUS] = df[PublicationsCSVCols.ID_SCOPUS].apply(cleanup_numbers)
        df[PublicationsCSVCols.ID_CROSSREF] = df[PublicationsCSVCols.ID_CROSSREF].apply(cleanup_numbers)
        df[PublicationsCSVCols.YEAR] = df[PublicationsCSVCols.YEAR].apply(cleanup_numbers)
        df[PublicationsCSVCols.AUTHOR_SCOPUS_ID] = df[PublicationsCSVCols.AUTHOR_SCOPUS_ID].apply(cleanup_numbers)
        df[PublicationsCSVCols.CITATION_COUNT] = df[PublicationsCSVCols.CITATION_COUNT].apply(cleanup_numbers)
        df[PublicationsCSVCols.CITATIONS_COUNT] = df[PublicationsCSVCols.CITATIONS_COUNT].apply(cleanup_numbers)
        df[PublicationsCSVCols.TEMPORAL_SCALE] = df[PublicationsCSVCols.TEMPORAL_SCALE].apply(cleanup_numbers)
        # boolean columns
        df[PublicationsCSVCols.GROUND_TRUTH] = df[PublicationsCSVCols.GROUND_TRUTH].apply(cleanup_boolean)
        return df
