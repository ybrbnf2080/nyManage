FROM kicsikrumpli/wine-pyinstaller



COPY main.sh .


RUN wine pip install virtualenv 


RUN chmod +x main.sh
ENTRYPOINT [ "./main.sh" ] 
