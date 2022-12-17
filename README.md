# MysqlBruteForce

Este es un script simple, que dado dos archivos, uno con usuarios y otro con contraseñas, intente hacer un ataque por fuerza bruta.

## Instrucciones para poder iniciar el codigo
Instalamos pip
```bash
$sudo apt install python3-pip
```
Instalamos PyMysql
```bash
$sudo pip install PyMySQL
```
Ejecutamos
```bash
$python3 mysqlBF.py -url <url> -udict <fichero de usuarios> -pdict <fichero de contraseñas>  -port <puerto>

```
## Ejemplo para atacar localhost en el puerto 8888
```bash
python3 mysqlBF.py -url localhost -udict users.txt -pdict password.txt  -port 8888

```
El archivo password.txt contiene las 10M de contraseñas mas usadas de este link:[https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt)
