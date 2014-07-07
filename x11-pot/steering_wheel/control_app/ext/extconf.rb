require 'mkmf'

have_library('X11')

create_makefile("x11_sendkey")
