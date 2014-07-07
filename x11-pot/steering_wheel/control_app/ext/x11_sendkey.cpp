#include <ruby/ruby.h>
#include "sendkey.hpp"

extern "C" {
  
  VALUE rb_x11_sendKey(VALUE self, VALUE keyCode)
  {

    if(sendKey(NUM2UINT(keyCode))) return Qtrue;
    return Qfalse;
  }

  void Init_x11_sendkey()
  {
    VALUE module = rb_define_module("X11");  
    //VALUE event_class = rb_define_class_under(module, "Event", rb_cObject);

    rb_define_singleton_method(module, "sendKey", (VALUE (*) (...)) rb_x11_sendKey, 1);
  }
  
}