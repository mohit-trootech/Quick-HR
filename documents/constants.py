# Document App Constants
from django.utils.translation import gettext_noop as _


class Constants:
    """Basic Document Constants"""

    DOCUMENT_UPLOAD_PATH = "documents/{id}/{file}"


class VerboseName:
    """ "Document model verbose names"""

    DOCUMENT = _("Document")
    DOCUMENTS = _("Documents")
    DOCFILE = _("Docfile")
