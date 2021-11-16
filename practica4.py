from ftplib import FTP
import telnetlib

def obtenerAchivo(fileName,ip):
    fileConfig = 'startup-config'
    ftp = FTP(ip)
    ftp.login('rcp','rcp') 
    ftp.retrbinary("RETR " + fileConfig, open(fileName, 'wb').write)
    ftp.quit()
def subirArchivo(fileName,ip):
    fileConfig = 'startup-config'
    ftp = FTP(ip)
    ftp.login('rcp','rcp') 
    ftp.storbinary('STOR '+ fileConfig, open(fileName, 'rb'))
    ftp.quit()

def generarArchivoConf(ip):
    tn = telnetlib.Telnet(ip)
    tn.read_until(b":", timeout=10) 
    tn.write(b'rcp\n')
    tn.read_until(b":", timeout=10) 
    tn.write(b'rcp\n')
    tn.read_until(b">", timeout=10) 
    tn.write(b'enable\n')
    tn.read_until(b"#", timeout=10) 
    tn.write(b'configure\n')
    tn.read_until(b"#", timeout=10)
    tn.write(b'copy running-config startup-config\n')
    tn.read_until(b"#", timeout=10) 
    tn.close()
while(1):
    print("Selecciona una opcion:")
    print("1)Generar archivo de configuracion")
    print("2)Obtener un archivo")
    print("3)Aplicar un archivo de configuracion")
    op = input()
    if(op == '1'):
        print('Ingresa la IP del router:')
        ip = input()
        generarArchivoConf(ip)
    if(op == '2'):
        print('Ingresa un nombre para guardarlo en el equipo:')
        filename = input()
        print('Ingresa la IP del router:')
        ip = input()
        obtenerAchivo(filename,ip)
    if(op == '3'):
        print('Ingresa el nombre del archivo:')
        filename = input()
        print('Ingresa la IP del router:')
        ip = input()
        subirArchivo(filename,ip)

