from Cheetah.compile import compile_to_class

from constants import LOCAL_SRC


tmpl = compile_to_class(LOCAL_SRC)()
run = tmpl.respond
