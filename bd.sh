#!/bin/bash
echo "Start build"
dts devel build -f -H tuduck4.local
echo "Start deploy"
dts devel run -f -H tuduck4.local
echo "finished up"