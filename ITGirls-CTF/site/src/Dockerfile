FROM debian:bullseye-slim

# Installeer docker, apache2, mod_wsgi, python3, pip3, mariadb. Maak wat
RUN apt-get update \
    && apt-get install -y docker.io apache2 \
    python3 python3-pip libapache2-mod-wsgi-py3 \
    libmariadb3 libmariadb-dev \
    && apt-get clean autoremove

# Voor debuggen
# RUN apt-get install -y nano

# Copieer alle onderdelen van de site naar de container
COPY ./app /var/www/itgirls/app/
COPY run.py itgirls.wsgi requirements.txt /var/www/itgirls/

# Copieer de vhosts naar de container
COPY ./itgirls.conf /etc/apache2/sites-available/itgirls.conf
COPY ./itgirls-ssl.conf /etc/apache2/sites-available/itgirls-ssl.conf

# Copieer ssl key en pem naar de container
COPY ./ssl/apache.pem /etc/ssl/itgirls/apache.pem
COPY ./ssl/apache.key /etc/ssl/itgirls/apache.key

# Installeer python libraries en start flask
RUN pip3 install -r /var/www/itgirls/requirements.txt \
    && python3 -m flask

# Zet SSL aan in de container
RUN a2enmod ssl

# Verander de actieve vhosts
RUN a2dissite 000-default.conf default-ssl.conf
RUN a2ensite itgirls itgirls-ssl

# Link apache config aan docker logs.
RUN ln -sf /proc/self/fd/1 /var/log/apache2/ssl_itgirls.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/ssl_itgirls_access.log 

# permissions
RUN chmod 775 -R /var/www/itgirls/* \
    && chown -R www-data:www-data /var/www/itgirls/* \
    && chown -R www-data:www-data /etc/apache2/sites-enabled/* \
    && chmod 600 -R /etc/apache2/sites-enabled/*

# run apache en geef www-data rechten tot de socket
CMD chown www-data /var/run/docker.sock; apache2ctl -D FOREGROUND;