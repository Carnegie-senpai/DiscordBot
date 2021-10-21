from os.path import exists
from commands.daddy import daddy
from commands.error import error
from commands.help import help
from commands.insult import insult
from commands.mock import mock
from commands.shutdown import shutdown
from commands.wake_on_lan import wake
if exists("./assets/training_vector_file") and exists("./assets/trained_model_output") and exists("./assets/pickled_genre"):
    from commands.movie import movie
else:
    print("Movie classifier assets missing, starting without movie command enabled")