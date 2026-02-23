#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SISTEMA DE LOGIN SEGURO
=======================
Un sistema de autenticación robusto con validaciones múltiples
y diseño atractivo en consola.

Características:
- Validación de credenciales
- Políticas de contraseñas seguras
- Límite de intentos
- Interfaz de usuario amigable
- Código modular y bien estructurado
"""

import time
import getpass
from colorama import init, Fore, Back, Style

# Inicializar colorama para colores en consola
init(autoreset=True)

# =============================================================================
# CONFIGURACIÓN DEL SISTEMA
# =============================================================================

class ConfiguracionLogin:
    """Clase de configuración para el sistema de login"""
    
    # Credenciales válidas (en producción, esto vendría de una base de datos)
    USUARIO_VALIDO = "admin"
    CONTRASEÑA_VALIDA = "Admin2026"
    
    # Configuración de seguridad
    MAX_INTENTOS = 3
    MIN_LONGITUD_CONTRASEÑA = 8
    TIEMPO_BLOQUEO = 3  # segundos
    
    # Mensajes del sistema
    MENSAJES = {
        'bienvenida': f"""
{Fore.CYAN}{'='*60}
{Fore.YELLOW}🔐 SISTEMA DE LOGIN SEGURO v1.0 🔐
{Fore.CYAN}{'='*60}
{Fore.WHITE}Bienvenido al sistema de autenticación
Por favor, ingresa tus credenciales
{Fore.CYAN}{'='*60}{Style.RESET_ALL}
""",
        'exito': f"""
{Fore.GREEN}✅ ACCESO CONCEDIDO ✅
{Fore.WHITE}Bienvenido al sistema, administrador
{Fore.GREEN}{'='*60}{Style.RESET_ALL}
""",
        'bloqueo': f"""
{Fore.RED}⛔ SISTEMA BLOQUEADO ⛔
{Fore.WHITE}Has excedido el número de intentos permitidos
Por favor, intenta más tarde
{Fore.RED}{'='*60}{Style.RESET_ALL}
"""
    }

# =============================================================================
# VALIDADORES DE CONTRASEÑA
# =============================================================================

class ValidadorContraseña:
    """Clase encargada de validar la fortaleza de las contraseñas"""
    
    def __init__(self):
        self.errores = []
    
    def validar_longitud(self, contraseña):
        """
        Valida que la contraseña tenga al menos 8 caracteres
        
        Args:
            contraseña (str): La contraseña a validar
        
        Returns:
            bool: True si es válida, False si no
        """
        if len(contraseña) < ConfiguracionLogin.MIN_LONGITUD_CONTRASEÑA:
            mensaje = f"{Fore.RED}❌ La contraseña debe tener mínimo {ConfiguracionLogin.MIN_LONGITUD_CONTRASEÑA} caracteres"
            print(mensaje)
            self.errores.append(mensaje)
            return False
        return True
    
    def validar_numeros(self, contraseña):
        """
        Valida que la contraseña contenga al menos un número
        
        Args:
            contraseña (str): La contraseña a validar
        
        Returns:
            bool: True si es válida, False si no
        """
        if not any(caracter.isdigit() for caracter in contraseña):
            mensaje = f"{Fore.RED}❌ La contraseña debe tener al menos un número"
            print(mensaje)
            self.errores.append(mensaje)
            return False
        return True
    
    def validar_letras(self, contraseña):
        """
        Valida que la contraseña contenga al menos una letra
        
        Args:
            contraseña (str): La contraseña a validar
        
        Returns:
            bool: True si es válida, False si no
        """
        if not any(caracter.isalpha() for caracter in contraseña):
            mensaje = f"{Fore.RED}❌ La contraseña debe contener al menos una letra"
            print(mensaje)
            self.errores.append(mensaje)
            return False
        return True
    
    def validar_caracteres_especiales(self, contraseña):
        """
        Valida que la contraseña solo contenga caracteres alfanuméricos
        
        Args:
            contraseña (str): La contraseña a validar
        
        Returns:
            bool: True si es válida, False si no
        """
        if not contraseña.isalnum():
            mensaje = f"{Fore.RED}❌ Solo se permiten caracteres alfanuméricos (sin espacios ni símbolos)"
            print(mensaje)
            self.errores.append(mensaje)
            return False
        return True
    
    def validar_sin_espacios(self, texto):
        """
        Valida que el texto no contenga espacios
        
        Args:
            texto (str): El texto a validar
        
        Returns:
            bool: True si es válido, False si no
        """
        if " " in texto:
            mensaje = f"{Fore.RED}❌ No se permiten espacios en blanco"
            print(mensaje)
            self.errores.append(mensaje)
            return False
        return True
    
    def validar_todo(self, contraseña):
        """
        Ejecuta todas las validaciones de contraseña
        
        Args:
            contraseña (str): La contraseña a validar
        
        Returns:
            bool: True si todas las validaciones pasan, False si no
        """
        self.errores = []
        
        validaciones = [
            self.validar_longitud(contraseña),
            self.validar_numeros(contraseña),
            self.validar_letras(contraseña),
            self.validar_caracteres_especiales(contraseña)
        ]
        
        return all(validaciones)

# =============================================================================
# SISTEMA DE LOGIN PRINCIPAL
# =============================================================================

class SistemaLogin:
    """Clase principal que maneja el proceso de autenticación"""
    
    def __init__(self):
        self.validador = ValidadorContraseña()
        self.intentos_restantes = ConfiguracionLogin.MAX_INTENTOS
        self.usuario_ingresado = ""
        self.contraseña_ingresada = ""
    
    def mostrar_bienvenida(self):
        """Muestra el mensaje de bienvenida del sistema"""
        print(ConfiguracionLogin.MENSAJES['bienvenida'])
    
    def solicitar_credenciales(self):
        """
        Solicita al usuario que ingrese sus credenciales
        
        Returns:
            tuple: (usuario, contraseña) ingresados por el usuario
        """
        print(f"{Fore.CYAN}📝 INGRESA TUS CREDENCIALES:{Style.RESET_ALL}")
        print("-" * 40)
        
        usuario = input(f"{Fore.WHITE}👤 Usuario: {Style.RESET_ALL}")
        contraseña = getpass.getpass(f"{Fore.WHITE}🔑 Contraseña: {Style.RESET_ALL}")
        
        print("-" * 40)
        
        return usuario, contraseña
    
    def validar_credenciales(self, usuario, contraseña):
        """
        Valida las credenciales ingresadas
        
        Args:
            usuario (str): Usuario ingresado
            contraseña (str): Contraseña ingresada
        
        Returns:
            bool: True si las credenciales son válidas, False si no
        """
        # Validar formato del usuario
        if not self.validador.validar_caracteres_especiales(usuario):
            return False
        
        # Validar sin espacios
        if not self.validador.validar_sin_espacios(usuario):
            return False
        
        # Validar formato de la contraseña
        if not self.validador.validar_todo(contraseña):
            return False
        
        # Validar sin espacios en contraseña
        if not self.validador.validar_sin_espacios(contraseña):
            return False
        
        return True
    
    def autenticar(self, usuario, contraseña):
        """
        Verifica si las credenciales coinciden con las almacenadas
        
        Args:
            usuario (str): Usuario a verificar
            contraseña (str): Contraseña a verificar
        
        Returns:
            bool: True si la autenticación es exitosa, False si no
        """
        if usuario != ConfiguracionLogin.USUARIO_VALIDO:
            print(f"{Fore.RED}❌ Usuario incorrecto{Style.RESET_ALL}")
            return False
        
        if contraseña != ConfiguracionLogin.CONTRASEÑA_VALIDA:
            print(f"{Fore.RED}❌ Contraseña incorrecta{Style.RESET_ALL}")
            return False
        
        return True
    
    def ejecutar(self):
        """
        Método principal que ejecuta el flujo completo del login
        """
        self.mostrar_bienvenida()
        
        while self.intentos_restantes > 0:
            # Mostrar intentos restantes
            print(f"{Fore.YELLOW}Intentos restantes: {self.intentos_restantes}{Style.RESET_ALL}\n")
            
            # Solicitar credenciales
            usuario, contraseña = self.solicitar_credenciales()
            
            # Validar formato
            if not self.validar_credenciales(usuario, contraseña):
                self.intentos_restantes -= 1
                print(f"\n{Fore.YELLOW}⚠️  Por favor, corrige los errores mostrados{Style.RESET_ALL}")
                
                if self.intentos_restantes > 0:
                    print(f"{Fore.CYAN}Esperando {ConfiguracionLogin.TIEMPO_BLOQUEO} segundos...{Style.RESET_ALL}")
                    time.sleep(ConfiguracionLogin.TIEMPO_BLOQUEO)
                continue
            
            # Autenticar
            if self.autenticar(usuario, contraseña):
                print(ConfiguracionLogin.MENSAJES['exito'])
                return True
            else:
                self.intentos_restantes -= 1
                
                if self.intentos_restantes > 0:
                    print(f"\n{Fore.YELLOW}⏳ {ConfiguracionLogin.TIEMPO_BLOQUEO} segundos para nuevo intento...{Style.RESET_ALL}")
                    time.sleep(ConfiguracionLogin.TIEMPO_BLOQUEO)
        
        # Si llegamos aquí, se acabaron los intentos
        print(ConfiguracionLogin.MENSAJES['bloqueo'])
        return False

# =============================================================================
# PUNTO DE ENTRADA PRINCIPAL
# =============================================================================

def main():
    """
    Función principal del programa
    """
    try:
        # Crear instancia del sistema de login
        sistema = SistemaLogin()
        
        # Ejecutar el sistema
        resultado = sistema.ejecutar()
        
        # Mensaje final
        if resultado:
            print(f"{Fore.GREEN}✨ Sesión iniciada correctamente{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}👋 Saliendo del sistema...{Style.RESET_ALL}")
            
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}⚠️  Programa interrumpido por el usuario{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error inesperado: {e}{Style.RESET_ALL}")
    finally:
        print(f"\n{Fore.CYAN}Gracias por usar el sistema. ¡Hasta luego!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
