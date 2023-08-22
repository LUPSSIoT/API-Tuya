import tinytuya

                           #   DEVICE_ID_HERE        IP_ADDRESS_HERE    LOCAL_KEY_HERE
d = tinytuya.OutletDevice('ebd300c7530ef165c9p865', '192.168.18.159', 'Qk}JRELq%e2H~|+>')
d.set_version(3.4)  # Atualizar para a versão do dispositivo que esta no final do devices.jason gerado pelo wizard
data = d.status() 
print('Device status: %r' % data)   # Mostra o status do dispositivo no caso: temperatura, umidade e a porcentagem da bateria



# Install TinyTuya
# python -m pip install tinytuya

# Upgrade TinyTuya
#pip install --upgrade tinytuya

# Run Setup Wizard:
# python -m tinytuya wizard