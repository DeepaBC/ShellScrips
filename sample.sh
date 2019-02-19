#!/bin/bash

echo 'msg = "ello world"' > hello
echo 'echo $msg' >> hello
chmod 700 hello
./hello
