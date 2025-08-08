from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

def afip(dni, password):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    
    ChromeService('chromedriver.exe')
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get("https://auth.afip.gob.ar/contribuyente_/login.xhtml")
    wait = WebDriverWait(driver, 20)
    
    login(driver, wait, dni, password)
    
    sworn_declaration(driver, wait)
    
    # Esperar a que aparezca el botón "Ingresar" dentro del panel "Libro IVA Digital"
    wait.until(EC.element_to_be_clickable((By.ID,"btnLibroVentas"))).click()
    
    import_and_download(wait)
    
    time.sleep(0.5)
    buy_book = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//a[contains(text(), 'Continuar al Libro Compras') and contains(@class, 'btn-success')]"
    )))
    buy_book.click()
    
    import_and_download(wait)
    time.sleep(3)
    driver.quit()

def login(driver, wait, dni, password):
    first_name = wait.until(EC.presence_of_element_located((By.NAME, "F1:username")))
    first_name = driver.find_element(By.NAME, "F1:username")
    first_name.clear()
    first_name.send_keys(dni)
    next_button = driver.find_element(By.NAME, "F1:btnSiguiente")
    next_button.click()
    
    passwordInput = wait.until(EC.presence_of_element_located((By.NAME, "F1:password")))
    passwordInput = driver.find_element(By.NAME, "F1:password")
    passwordInput.clear()
    passwordInput.send_keys(password)
    login_button = driver.find_element(By.NAME, "F1:btnIngresar")
    login_button.click()
    
def sworn_declaration(driver, wait):
    # Esperar que cargue el menú principal
    wait.until(EC.presence_of_element_located((By.ID, "serviciosMasUtilizados")))

    # Esperar que aparezca "Portal IVA" y hacer clic
    portal_iva = wait.until(EC.presence_of_element_located((
        By.XPATH, "//h3[text()='Portal IVA']"
    )))

    # Hacer clic en el contenedor del "Portal IVA"
    # Hacer clic en el contenedor del "Portal IVA"
    portal_iva.click()

    # Esperar a que se abra la nueva pestaña
    wait.until(lambda d: len(d.window_handles) > 1)

    # Cambiar a la nueva pestaña
    driver.switch_to.window(driver.window_handles[-1])

    # Esperar que cargue el botón "Ingresar" en "Nueva declaración jurada"
    wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//h3[span[text()='Nueva declaración jurada']]/../../div[@class='media-right']//button[span[text()='Ingresar']]"
        ))
    ).click()
    
    # Esperar que el select sea clickeable
    wait.until(EC.element_to_be_clickable((By.ID, "periodo"))).click()

    # Esperar que aparezcan las opciones con valores
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#periodo option[value]")))

    # Obtener las opciones
    options = driver.find_elements(By.CSS_SELECTOR, "#periodo option[value]")

    # Clickear la segunda opción válida (índice 1 = mes anterior)
    options[1].click()
    
    # Esperar a que el botón sea clickeable (por clase y texto)
    continuar_button = wait.until(
        EC.element_to_be_clickable((
            By.XPATH, "//button[span[text()='Continuar']]"
        ))
    )

    # Hacer clic en el botón
    continuar_button.click()
    
    # Esperar a que aparezca el botón "Ingresar" dentro del panel correcto
    ingresar_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//h3[span[text()='Registración y declaración']]/../../div[@class='media-right']//button[span[text()='Ingresar']]"
        ))
    )

    # Hacer clic en el botón
    ingresar_btn.click()
    
def import_and_download(wait):
    # Esperar a que el botón esté presente y hacer click en "Importar"
    wait.until(EC.element_to_be_clickable((By.ID, "btnDropdownImportar"))).click()

    # Esperar y hacer click en "Importar desde ARCA"
    wait.until(EC.element_to_be_clickable((By.ID, "lnkImportarAFIP"))).click()
    
    wait.until(EC.element_to_be_clickable((By.ID, "btnImportarAFIPImportar"))).click()
    
    time.sleep(6)
    # Esperar que el botón de cierre esté visible y hacer click
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='btnTareasCerrar']//button[contains(text(), 'Cerrar')]")))
    close_button.click()

    # Esperar que el modal desaparezca completamente
    wait.until(EC.invisibility_of_element_located((By.ID, "modalTareas")))
    time.sleep(1)
    
    # Esperar y hacer clic en el botón "Excel"
    excel_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[@class='dt-buttons btn-group']//button[span[text()='Excel']]"
        ))
    )
    excel_btn.click()