x11-pot
=======

* Simulate right and left keyboard keys with a potentiometer (x11 environment)
* Just connect the middle pin of the pot to the pin A0 then

build the simple x11 extension (in ext directory)

```
ruby extconf.rb
make && nake install
```

install ruby serial port gem

```
gem install serialport
```

finally
```
ruby steering_wheel.rb
```

* You may play super tux cart with this :D
