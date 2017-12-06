#!/bin/bash
./latex-docker/dockercmd.sh /bin/sh -c "pdflatex front.tex && pdflatex front.tex && pdflatex idcard.tex && pdflatex idcard.tex"