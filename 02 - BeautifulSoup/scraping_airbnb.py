import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.common.by import By

options = Options()
#options.add_argument('--width=400')
#options.add_argument('--height=800')

navegador = webdriver.Firefox(options=options)

navegador.get('https://www.airbnb.com.br/')

sleep(4)

inputPlace = navegador.find_element(By.ID, 'bigsearch-query-location-input')
inputPlace.send_keys('São Paulo')
inputPlace.submit()

sleep(4)

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')
print(site.prettify())


#button_stay = navegador.find_element(By.CLASS_NAME, 'bhtghtc atm_1s_glywfm atm_26_1j28jx2 atm_3f_idpfg4 atm_9j_tlke0l atm_9s_1o8liyq atm_bx_1kw7nm4 atm_gi_idpfg4 atm_l8_idpfg4 atm_r3_1kw7nm4 atm_rd_glywfm atm_vb_1wugsn5 atm_kd_glywfm atm_2d_1wg69w8 atm_5j_1tcgj5g atm_7l_1hbpp16 atm_c8_8ycq01 atm_cs_qo5vgd atm_e2_fyhuej atm_g3_exct8b atm_j3_fyhuej atm_ks_15vqwwr atm_mk_h2mmj6 atm_uc_sgxu0i atm_vh_nkobfv atm_wq_idpfg4 atm_3f_glywfm_jo46a5 atm_l8_idpfg4_jo46a5 atm_gi_idpfg4_jo46a5 atm_3f_glywfm_1icshfk atm_kd_glywfm_19774hq atm_2d_12pj79__6ldadd atm_uc_glywfm__1rrf6b5 atm_26_2a2bt1_vmtskl atm_6i_idpfg4_vmtskl atm_92_1yyfdc7_vmtskl atm_fq_idpfg4_vmtskl atm_mk_stnw88_vmtskl atm_n3_idpfg4_vmtskl atm_tk_idpfg4_vmtskl atm_uc_1rfv3yc_vmtskl atm_vz_brmitn_vmtskl atm_wq_idpfg4_vmtskl atm_uc_glywfm_vmtskl_1rrf6b5 atm_70_1rtszzq_1w3cfyq atm_70_1rtszzq_pfnrn2_1oszvuo b1tqc7mb atm_j3_uuw12j__1v156lz atm_uc_glywfm__1v156lz dir dir-ltr')
#button_stay.click()


# response = requests.get('https://www.airbnb.com.br/')



#print(site.prettify())