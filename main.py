# =====Terminal Command: pip install pywhatkit===== #

# =====Imports===== #
import pywhatkit as pwk
# =====Imports===== #

# =====Enviar mensagem Whats | Send message Whats===== #
# =====Main===== #

# =====Tentar rodar | Try run===== #
try:
     
     # =====Dados tel,msg,hora,minuto,fechar?,após segundos | Data tel,msg,hour,minute,close?,after seconds===== #
     pwk.sendwhatmsg_instantly("+55119123456789", "Oi, teste?", 20, 50, True, 5)
     
     # =====Dados tel,msg,instantaneo | Data tel,msg,instantaneous===== #
     pwk.sendwhatmsg_instantly("+55119123456789", "Oi, teste?")
     
     # =====Printar Sucesso | Print Sucess===== #
     print("Mensagem Enviada!")
     
# =====Excessão não rodar | Exception don't work===== #     
except: 
     
     # =====Printar erro | Print error===== #
     print("Erro! Mensagem não enviada!")
     
# =====Main===== #
