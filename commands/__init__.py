from os.path import exists
from commands.daddy import daddy
from commands.error import error
from commands.help import help
from commands.insult import insult
from commands.mock import mock
from commands.shutdown import shutdown
from commands.wake_on_lan import wake
from commands.music import play#, clear, queue, remove, stop
tvf = exists("./assets/training_vector_file")
tmo = exists("./assets/trained_model_output")
pg = exists("./assets/pickled_genres")
if tvf and tmo and pg:
    from commands.movie import movie
else:
    print("Movie classifier assets missing, starting without movie command enabled: ")
    if (not tvf):
        print("./assets/training_vector_file is missing")
    if (not tmo):
        print("./assets/trained_model_output is missing")
    if (not pg):
        print("./assets/pickled_genres is missing")