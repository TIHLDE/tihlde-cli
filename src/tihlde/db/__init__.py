from .init import init_db
from tihlde.db.sentences import (
    insert_sentence,
    get_all_sentences,
    delete_sentence,
    delete_all_sentences
)
from tihlde.db.files import (
    get_all_files,
    insert_file,
    delete_file,
    delete_all_files,
    get_file
)